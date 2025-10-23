#!/usr/bin/env node
/**
 * Simple Hello World script for testing purposes.
 */

function greet(name = "World") {
  return `Hello, ${name}!`;
}

function main() {
  console.log(greet());
  console.log(greet("Copilot"));
}

if (require.main === module) {
  main();
}

module.exports = { greet };
