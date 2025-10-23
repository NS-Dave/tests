/**
 * Tests for the hello_world module.
 */
const { greet } = require('../scripts/javascript/hello_world');

describe('Hello World', () => {
  test('greets with default name', () => {
    expect(greet()).toBe('Hello, World!');
  });

  test('greets with custom name', () => {
    expect(greet('Copilot')).toBe('Hello, Copilot!');
  });

  test('greets with another custom name', () => {
    expect(greet('Test')).toBe('Hello, Test!');
  });
});
