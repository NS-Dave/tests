# Contributing Guide

## Adding New Scripts

### Python Scripts
1. Add your script to `scripts/python/`
2. Include a docstring with description
3. Make the script executable with shebang: `#!/usr/bin/env python3`
4. Add corresponding tests in `tests/`

### JavaScript Scripts
1. Add your script to `scripts/javascript/`
2. Include JSDoc comments
3. Make the script executable with shebang: `#!/usr/bin/env node`
4. Export functions for testing
5. Add corresponding tests in `tests/`

### Shell Scripts
1. Add your script to `scripts/shell/`
2. Add comments explaining functionality
3. Make executable: `chmod +x your_script.sh`
4. Use proper shebang: `#!/bin/bash`

## Writing Tests

### Python Tests (unittest)
```python
import unittest
from module import function

class TestFunction(unittest.TestCase):
    def test_case(self):
        self.assertEqual(function(input), expected_output)
```

### JavaScript Tests (Jest)
```javascript
const { function } = require('../scripts/javascript/module');

describe('Function', () => {
  test('description', () => {
    expect(function(input)).toBe(expected_output);
  });
});
```

## Code Style

### Python
- Follow PEP 8
- Use docstrings
- Type hints are encouraged

### JavaScript
- Use modern ES6+ syntax
- Add JSDoc comments
- Prefer const/let over var

### Shell
- Use meaningful variable names
- Add comments for complex logic
- Quote variables properly
