# Example Code Blocks

This directory contains various example code blocks for testing with Copilot.

## Python Examples

### Basic Function
```python
def greet(name):
    return f"Hello, {name}!"
```

### List Comprehension
```python
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
```

### Class Definition
```python
class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, value):
        self.result += value
        return self.result
    
    def reset(self):
        self.result = 0
```

## JavaScript Examples

### Arrow Functions
```javascript
const add = (a, b) => a + b;
const greet = name => `Hello, ${name}!`;
```

### Async/Await
```javascript
async function fetchData(url) {
  try {
    const response = await fetch(url);
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}
```

### Array Methods
```javascript
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(x => x * 2);
const evens = numbers.filter(x => x % 2 === 0);
const sum = numbers.reduce((acc, x) => acc + x, 0);
```

## Shell Examples

### Basic Loop
```bash
for i in {1..5}; do
    echo "Number: $i"
done
```

### File Processing
```bash
while IFS= read -r line; do
    echo "Processing: $line"
done < input.txt
```

### Conditional
```bash
if [ -f "file.txt" ]; then
    echo "File exists"
else
    echo "File not found"
fi
```
