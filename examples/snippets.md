# Snippets Collection

Common code snippets for testing and reference.

## Error Handling

### Python
```python
try:
    result = risky_operation()
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    cleanup()
```

### JavaScript
```javascript
try {
  const result = riskyOperation();
} catch (error) {
  console.error('Error:', error.message);
} finally {
  cleanup();
}
```

## Data Structures

### Python Dictionary
```python
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
```

### JavaScript Object
```javascript
const person = {
  name: "John",
  age: 30,
  city: "New York"
};
```

## API Patterns

### RESTful Endpoint (Python Flask)
```python
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())
```

### RESTful Endpoint (JavaScript Express)
```javascript
app.get('/api/users/:userId', (req, res) => {
  const userId = req.params.userId;
  User.findById(userId)
    .then(user => res.json(user))
    .catch(err => res.status(404).json({ error: 'User not found' }));
});
```
