/**
 * Tests for the calculator module.
 */
const { add, subtract, multiply, divide } = require('../scripts/javascript/calculator');

describe('Calculator', () => {
  describe('add', () => {
    test('adds two positive numbers', () => {
      expect(add(5, 3)).toBe(8);
    });

    test('adds positive and negative', () => {
      expect(add(-1, 1)).toBe(0);
    });

    test('adds zeros', () => {
      expect(add(0, 0)).toBe(0);
    });
  });

  describe('subtract', () => {
    test('subtracts two numbers', () => {
      expect(subtract(10, 5)).toBe(5);
    });

    test('subtracts resulting in negative', () => {
      expect(subtract(5, 10)).toBe(-5);
    });

    test('subtracts zeros', () => {
      expect(subtract(0, 0)).toBe(0);
    });
  });

  describe('multiply', () => {
    test('multiplies two positive numbers', () => {
      expect(multiply(3, 4)).toBe(12);
    });

    test('multiplies negative and positive', () => {
      expect(multiply(-2, 3)).toBe(-6);
    });

    test('multiplies by zero', () => {
      expect(multiply(0, 100)).toBe(0);
    });
  });

  describe('divide', () => {
    test('divides two numbers', () => {
      expect(divide(10, 2)).toBe(5);
    });

    test('divides resulting in decimal', () => {
      expect(divide(10, 3)).toBeCloseTo(3.333333, 5);
    });

    test('throws error on division by zero', () => {
      expect(() => divide(10, 0)).toThrow('Cannot divide by zero');
    });
  });
});
