#!/usr/bin/env node
/**
 * Simple calculator script for testing various operations.
 */

function add(a, b) {
  return a + b;
}

function subtract(a, b) {
  return a - b;
}

function multiply(a, b) {
  return a * b;
}

function divide(a, b) {
  if (b === 0) {
    throw new Error("Cannot divide by zero");
  }
  return a / b;
}

function main() {
  console.log(`10 + 5 = ${add(10, 5)}`);
  console.log(`10 - 5 = ${subtract(10, 5)}`);
  console.log(`10 * 5 = ${multiply(10, 5)}`);
  console.log(`10 / 5 = ${divide(10, 5)}`);
}

if (require.main === module) {
  main();
}

module.exports = { add, subtract, multiply, divide };
