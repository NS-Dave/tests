#!/usr/bin/env python3
"""
Simple Hello World script for testing purposes.
"""


def greet(name="World"):
    """Return a greeting message."""
    return f"Hello, {name}!"


def main():
    """Main function."""
    print(greet())
    print(greet("Copilot"))


if __name__ == "__main__":
    main()
