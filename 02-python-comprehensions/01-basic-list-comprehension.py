"""
Basic List Comprehension - Transform lists with elegance

🎯 Problem: Apply a transformation to every item in a list
"""

import time


def transform_traditional(numbers):
    """Traditional approach with loops"""
    result = []
    for num in numbers:
        result.append(num * 2)
    return result


def transform_comprehension(numbers):
    """List comprehension approach"""
    return [num * 2 for num in numbers]


# 📝 Example usage
numbers = [1, 2, 3, 4, 5]
print(f"Original: {numbers}")
print(f"Doubled: {transform_comprehension(numbers)}")
# Output: [2, 4, 6, 8, 10]


# 🎯 Real-world example: Processing user data
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}
]

# Extract names
names = [user["name"] for user in users]
print(f"Names: {names}")

# Calculate ages in 10 years
future_ages = [user["age"] + 10 for user in users]
print(f"Ages in 10 years: {future_ages}")

# Create email addresses
emails = [f"{user['name'].lower()}@company.com" for user in users]
print(f"Email addresses: {emails}")


# 🔢 Common transformations
data = [1, 2, 3, 4, 5]

# Mathematical operations
squares = [x**2 for x in data]
print(f"Squares: {squares}")

# String operations
words = ["hello", "world", "python"]
uppercase = [word.upper() for word in words]
print(f"Uppercase: {uppercase}")

# Type conversions
numbers_str = ["1", "2", "3", "4", "5"]
numbers_int = [int(x) for x in numbers_str]
print(f"String to int: {numbers_int}")


# 📊 Performance comparison
large_list = list(range(100000))

# Traditional loop
start = time.time()
result1 = []
for num in large_list:
    result1.append(num * 2)
loop_time = time.time() - start

# List comprehension
start = time.time()
result2 = [num * 2 for num in large_list]
comp_time = time.time() - start

print(f"\nPerformance comparison:")
print(f"Traditional loop: {loop_time:.4f}s")
print(f"List comprehension: {comp_time:.4f}s")
print(f"Speedup: {loop_time/comp_time:.2f}x faster")


# 💡 When to use:
# - Simple transformations on lists
# - Data processing and cleaning
# - Creating new lists from existing ones
# - When readability and performance matter
# - Functional programming patterns 