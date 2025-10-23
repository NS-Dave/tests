#!/bin/bash
# Simple Hello World script for testing purposes

greet() {
    local name="${1:-World}"
    echo "Hello, ${name}!"
}

main() {
    greet
    greet "Copilot"
}

main "$@"
