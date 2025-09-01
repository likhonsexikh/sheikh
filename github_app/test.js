try {
  require('./index.js');
  console.log('Test passed: index.js can be loaded successfully.');
} catch (error) {
  console.error('Test failed: Error loading index.js:', error);
  process.exit(1);
}
