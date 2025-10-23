#!/usr/bin/env python3
"""
String manipulation utilities.
Demonstrates common string operations.
"""


def reverse_string(text):
    """Reverse a string."""
    return text[::-1]


def capitalize_words(text):
    """Capitalize first letter of each word."""
    return text.title()


def count_words(text):
    """Count words in a string."""
    return len(text.split())


def remove_whitespace(text):
    """Remove extra whitespace from string."""
    return ' '.join(text.split())


def is_palindrome(text):
    """Check if string is a palindrome."""
    cleaned = text.lower().replace(' ', '')
    return cleaned == cleaned[::-1]


def main():
    """Demonstrate string operations."""
    test_string = "Hello World"
    
    print(f"Original: {test_string}")
    print(f"Reversed: {reverse_string(test_string)}")
    print(f"Capitalized: {capitalize_words(test_string)}")
    print(f"Word count: {count_words(test_string)}")
    print(f"Is 'racecar' a palindrome? {is_palindrome('racecar')}")


if __name__ == "__main__":
    main()
