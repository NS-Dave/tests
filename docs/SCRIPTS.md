# Script Index

This document provides an overview of all available scripts in this repository.

## Python Scripts

### hello_world.py
- **Location**: `scripts/python/hello_world.py`
- **Purpose**: Simple greeting script demonstrating basic functions
- **Usage**: `python3 scripts/python/hello_world.py`
- **Tests**: `tests/test_hello_world.py`

### calculator.py
- **Location**: `scripts/python/calculator.py`
- **Purpose**: Basic arithmetic operations (add, subtract, multiply, divide)
- **Usage**: `python3 scripts/python/calculator.py`
- **Tests**: `tests/test_calculator.py`

### string_utils.py
- **Location**: `scripts/python/string_utils.py`
- **Purpose**: String manipulation utilities (reverse, capitalize, word count, palindrome check)
- **Usage**: `python3 scripts/python/string_utils.py`

### file_operations.py
- **Location**: `scripts/python/file_operations.py`
- **Purpose**: File I/O operations including JSON handling
- **Usage**: `python3 scripts/python/file_operations.py`

## JavaScript Scripts

### hello_world.js
- **Location**: `scripts/javascript/hello_world.js`
- **Purpose**: Simple greeting script demonstrating basic functions
- **Usage**: `node scripts/javascript/hello_world.js`
- **Tests**: `tests/hello_world.test.js`

### calculator.js
- **Location**: `scripts/javascript/calculator.js`
- **Purpose**: Basic arithmetic operations (add, subtract, multiply, divide)
- **Usage**: `node scripts/javascript/calculator.js`
- **Tests**: `tests/calculator.test.js`

### file_operations.js
- **Location**: `scripts/javascript/file_operations.js`
- **Purpose**: Async file I/O operations including JSON handling
- **Usage**: `node scripts/javascript/file_operations.js`

## Shell Scripts

### hello_world.sh
- **Location**: `scripts/shell/hello_world.sh`
- **Purpose**: Simple greeting script in Bash
- **Usage**: `./scripts/shell/hello_world.sh`

### system_info.sh
- **Location**: `scripts/shell/system_info.sh`
- **Purpose**: Display system information (hostname, OS, disk usage, etc.)
- **Usage**: `./scripts/shell/system_info.sh`

### backup_file.sh
- **Location**: `scripts/shell/backup_file.sh`
- **Purpose**: Create timestamped backup of files
- **Usage**: `./scripts/shell/backup_file.sh <filename>`

## Running All Tests

### Python Tests
```bash
python3 -m unittest discover tests -v
```

### JavaScript Tests
```bash
npm test
```

## Adding New Scripts

Please refer to [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding new scripts.
