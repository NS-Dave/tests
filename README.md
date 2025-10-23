# Test Scripts Repository

A comprehensive repository for testing scripts and code blocks with GitHub Copilot.

## 📁 Repository Structure

```
.
├── scripts/          # Executable scripts in various languages
│   ├── python/       # Python scripts
│   ├── javascript/   # JavaScript/Node.js scripts
│   ├── shell/        # Bash/shell scripts
│   └── misc/         # Other language scripts
├── tests/            # Test files for the scripts
├── examples/         # Code block examples and snippets
└── docs/             # Additional documentation
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- Node.js 14+
- Bash shell

### Installation

1. Clone the repository:
```bash
git clone https://github.com/NS-Dave/tests.git
cd tests
```

2. Install Node.js dependencies:
```bash
npm install
```

## 🧪 Running Scripts

### Python Scripts
```bash
# Run hello world
python3 scripts/python/hello_world.py

# Run calculator
python3 scripts/python/calculator.py
```

### JavaScript Scripts
```bash
# Run hello world
node scripts/javascript/hello_world.js

# Run calculator
node scripts/javascript/calculator.js

# Or use npm scripts
npm run run:hello-js
npm run run:calc-js
```

### Shell Scripts
```bash
# Make scripts executable
chmod +x scripts/shell/*.sh

# Run hello world
./scripts/shell/hello_world.sh

# Run system info
./scripts/shell/system_info.sh
```

## 🧪 Running Tests

### Python Tests
```bash
# Run all Python tests
python3 -m unittest discover tests

# Run specific test
python3 tests/test_calculator.py
```

### JavaScript Tests
```bash
# Run all Jest tests
npm test

# Run with coverage
npm run test:coverage

# Run in watch mode
npm run test:watch
```

## 📚 Available Scripts

### Python Scripts
- `hello_world.py` - Simple greeting script
- `calculator.py` - Basic calculator operations

### JavaScript Scripts
- `hello_world.js` - Simple greeting script
- `calculator.js` - Basic calculator operations

### Shell Scripts
- `hello_world.sh` - Simple greeting script
- `system_info.sh` - Display system information

## 📖 Examples

Check the `examples/` directory for:
- `code_blocks.md` - Various code block examples in different languages
- `snippets.md` - Common code snippets and patterns

## 🤝 Contributing

This is a test repository for Copilot experimentation. Feel free to:
- Add new scripts in any language
- Create new test files
- Add example code blocks
- Improve documentation

## 📝 Testing with Copilot

This repository is designed to test:
1. **Script Generation** - Let Copilot suggest new scripts
2. **Test Creation** - Generate tests for existing scripts
3. **Code Completion** - Test autocomplete features
4. **Refactoring** - Improve existing code with Copilot
5. **Documentation** - Generate comments and docs

## 🎯 Use Cases

- Learning GitHub Copilot features
- Testing Copilot's code generation capabilities
- Experimenting with different programming languages
- Creating a reference library of common patterns
- Validating Copilot suggestions

## 📄 License

MIT License - feel free to use this repository for learning and testing.
