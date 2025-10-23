# Testing Guide

## Overview
This repository includes tests for Python and JavaScript scripts using unittest and Jest respectively.

## Python Testing

### Running Tests
```bash
# Run all tests
python3 -m unittest discover tests

# Run specific test file
python3 tests/test_calculator.py

# Run with verbose output
python3 -m unittest discover tests -v

# With pytest (if installed)
pytest tests/
pytest tests/ -v
pytest tests/ --cov
```

### Writing Python Tests
Use the unittest framework:
```python
import unittest

class TestMyFunction(unittest.TestCase):
    def test_something(self):
        self.assertEqual(my_function(), expected_result)
    
    def test_error_handling(self):
        with self.assertRaises(ValueError):
            my_function(invalid_input)
```

## JavaScript Testing

### Running Tests
```bash
# Run all tests
npm test

# Run with coverage
npm run test:coverage

# Watch mode for development
npm run test:watch
```

### Writing JavaScript Tests
Use Jest framework:
```javascript
describe('MyFunction', () => {
  test('does something', () => {
    expect(myFunction()).toBe(expected);
  });

  test('handles errors', () => {
    expect(() => myFunction(invalid)).toThrow();
  });
});
```

## Shell Script Testing
While formal testing frameworks exist for shell scripts, basic testing can be done by:
1. Running the script manually
2. Checking exit codes
3. Verifying output

Example:
```bash
# Run script and check exit code
./scripts/shell/hello_world.sh
echo $?  # Should be 0 for success
```

## Continuous Integration
Consider adding GitHub Actions workflow for automated testing:
```yaml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
      - name: Set up Node.js
        uses: actions/setup-node@v2
      - name: Run Python tests
        run: python3 -m unittest discover tests
      - name: Run JavaScript tests
        run: npm install && npm test
```
