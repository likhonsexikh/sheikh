// examples/advanced_streaming.js

const { Sheikh } = require('sheikh-sdk');

async function main() {
    console.log('Initializing Sheikh SDK for streaming example...');

    try {
        // This assumes the SDK can connect to a local Sheikh instance running in server mode.
        const sheikh = new Sheikh({ host: 'localhost', port: 8080 });

        const prompt = 'Generate a long story about a robot exploring a new planet, in multiple paragraphs.';
        console.log(`Prompt: ${prompt}`);
        console.log('\n--- Streaming Model Response ---');

        const stream = await sheikh.generateStream(prompt, { maxTokens: 500 });

        stream.on('data', (chunk) => {
            // Process each chunk of data as it arrives
            process.stdout.write(chunk.token);
        });

        stream.on('end', () => {
            console.log('\n------------------------------');
            console.log('Stream finished.');
        });

        stream.on('error', (err) => {
            console.error('\nAn error occurred during streaming:', err);
        });

    } catch (error) {
        console.error('Failed to initialize SDK or start stream:', error.message);
        console.error('Please ensure the Sheikh runtime is running in server mode.');
    }
}

main();
