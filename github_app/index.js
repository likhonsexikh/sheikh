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

      // Placeholder for Sheikh model API call
      // In a real implementation, this would be an HTTP call to the model endpoint.
      // const sheikhResponse = await callSheikhModel(prompt);
      const sheikhResponse = "This is a placeholder review. The document looks good, but could be improved with more examples.";

      await context.octokit.issues.createComment({
        owner,
        repo,
        issue_number: pull_number,
        body: `### Review for ${file.filename}\n\n${sheikhResponse}`,
      });
    }

    return;
  });
};
