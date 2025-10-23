#!/usr/bin/env node
/**
 * File operations example script.
 * Demonstrates reading, writing, and processing files.
 */
const fs = require('fs').promises;
const path = require('path');

async function readFile(filename) {
  return await fs.readFile(filename, 'utf-8');
}

async function writeFile(filename, content) {
  await fs.writeFile(filename, content, 'utf-8');
}

async function readJSON(filename) {
  const content = await readFile(filename);
  return JSON.parse(content);
}

async function writeJSON(filename, data) {
  const content = JSON.stringify(data, null, 2);
  await writeFile(filename, content);
}

async function main() {
  console.log('File Operations Example');
  
  const data = {
    name: 'Test Data',
    values: [1, 2, 3, 4, 5],
    active: true
  };
  
  console.log('Sample data:', data);
}

if (require.main === module) {
  main().catch(console.error);
}

module.exports = { readFile, writeFile, readJSON, writeJSON };
