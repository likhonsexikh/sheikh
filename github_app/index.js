const https = require('https');
require('dotenv').config();

/**
 * Calls the Sheikh model API to get a review.
 * @param {string} prompt The prompt to send to the model.
 * @returns {Promise<string>} The model's response.
 */
function callSheikhModel(prompt) {
  return new Promise((resolve, reject) => {
    const endpoint = new URL(process.env.SHEIKH_MODEL_ENDPOINT);
    const options = {
      hostname: endpoint.hostname,
      path: endpoint.pathname,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${process.env.SHEIKH_API_KEY}`,
      },
    };

    const req = https.request(options, (res) => {
      let data = '';
      res.on('data', (chunk) => {
        data += chunk;
      });
      res.on('end', () => {
        if (res.statusCode >= 200 && res.statusCode < 300) {
          try {
            const responseBody = JSON.parse(data);
            // Adjust this based on the actual API response structure
            resolve(responseBody[0].generated_text);
          } catch (error) {
            reject(new Error('Failed to parse model response.'));
          }
        } else {
          reject(new Error(`Model API returned status code ${res.statusCode}: ${data}`));
        }
      });
    });

    req.on('error', (error) => {
      reject(error);
    });

    req.write(JSON.stringify({ inputs: prompt }));
    req.end();
  });
}

/**
 * @param {import('probot').Probot} app
 */
module.exports = (app) => {
  app.log.info("Yay, the app was loaded!");

  app.on(["pull_request.opened", "pull_request.synchronize"], async (context) => {
    app.log.info("Pull request event received.");

    const owner = context.payload.repository.owner.login;
    const repo = context.payload.repository.name;
    const pull_number = context.payload.pull_request.number;

    const { data: files } = await context.octokit.pulls.listFiles({
      owner,
      repo,
      pull_number,
    });

    const relevantFiles = files.filter(file =>
      file.filename.endsWith('.md') ||
      file.filename.endsWith('.xml') ||
      file.filename.endsWith('.mdx')
    );

    app.log.info(`Found ${relevantFiles.length} relevant files to review.`);

    for (const file of relevantFiles) {
      const { data: content } = await context.octokit.repos.getContent({
        owner,
        repo,
        path: file.filename,
        ref: context.payload.pull_request.head.sha,
      });

      const fileContent = Buffer.from(content.content, 'base64').toString('utf8');

      app.log.info(`Reviewing file: ${file.filename}`);

      // Construct the prompt using the user's recommended format
      const prompt = `
        <instructions>
          You are a technical writer's assistant. Review the following document for clarity, style, and correctness.
          Provide feedback in a concise manner.
        </instructions>
        <thinking>
          The user wants me to review a file. I should check for common issues like typos, grammatical errors, and awkward phrasing.
          I will structure my feedback clearly.
        </thinking>
        <document>
          ${fileContent}
        </document>
        <answer>
      `;

      try {
        const sheikhResponse = await callSheikhModel(prompt);
        await context.octokit.issues.createComment({
          owner,
          repo,
          issue_number: pull_number,
          body: `### Review for ${file.filename}\n\n${sheikhResponse}`,
        });
      } catch (error) {
        app.log.error(`Failed to get review for ${file.filename}: ${error.message}`);
        await context.octokit.issues.createComment({
          owner,
          repo,
          issue_number: pull_number,
          body: `### Review for ${file.filename}\n\nSorry, I was unable to get a review for this file. Error: ${error.message}`,
        });
      }
    }
        owner,
        repo,
        issue_number: pull_number,
        body: `### Review for ${file.filename}\n\n${sheikhResponse}`,
      });
    }

    return;
  });
};
