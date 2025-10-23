#!/usr/bin/env python3
"""
File operations example script.
Demonstrates reading, writing, and processing files.
"""
import os
import json


def read_file(filename):
    """Read and return contents of a file."""
    with open(filename, 'r') as f:
        return f.read()


def write_file(filename, content):
    """Write content to a file."""
    with open(filename, 'w') as f:
        f.write(content)


def read_json(filename):
    """Read and parse a JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)


def write_json(filename, data):
    """Write data to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)


def main():
    """Demonstrate file operations."""
    # Example data
    data = {
        "name": "Test Data",
        "values": [1, 2, 3, 4, 5],
        "active": True
    }
    
    print("File Operations Example")
    print(f"Sample data: {data}")


if __name__ == "__main__":
    main()
