"""
Conditional Comprehensions - Add filtering logic to comprehensions

🎯 Problem: Transform and filter lists simultaneously
"""


def filter_transform_traditional(numbers):
    """Traditional approach with loops"""
    result = []
    for num in numbers:
        if num % 2 == 0:  # Only even numbers
            result.append(num * 2)
    return result


def filter_transform_comprehension(numbers):
    """Comprehension with filtering"""
    return [num * 2 for num in numbers if num % 2 == 0]


# 📝 Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original: {numbers}")
print(f"Even numbers doubled: {filter_transform_comprehension(numbers)}")
# Output: [4, 8, 12, 16, 20]


# 🎯 Real-world example: Processing product data
products = [
    {"name": "Laptop", "price": 999, "category": "electronics"},
    {"name": "Book", "price": 15, "category": "books"},
    {"name": "Phone", "price": 599, "category": "electronics"},
    {"name": "Notebook", "price": 3, "category": "books"},
    {"name": "Tablet", "price": 299, "category": "electronics"}
]

# Filter expensive electronics
expensive_electronics = [
    product["name"] 
    for product in products 
    if product["category"] == "electronics" and product["price"] > 500
]
print(f"Expensive electronics: {expensive_electronics}")

# Create sale prices for books
book_sale_prices = [
    {"name": product["name"], "sale_price": product["price"] * 0.8}
    for product in products
    if product["category"] == "books"
]
print(f"Book sale prices: {book_sale_prices}")


# 🔤 String filtering patterns
words = ["apple", "banana", "cherry", "date", "elderberry"]

# Words longer than 5 characters
long_words = [word for word in words if len(word) > 5]
print(f"Long words: {long_words}")

# Words starting with vowels, capitalized
vowel_words = [word.capitalize() for word in words if word[0] in 'aeiou']
print(f"Vowel words: {vowel_words}")

# Words with specific patterns
a_words = [word.upper() for word in words if 'a' in word]
print(f"Words with 'a': {a_words}")


# 🎨 Multiple conditions
scores = [85, 92, 78, 96, 67, 88, 91, 73, 94, 82]

# High scores (A grade: 90+)
high_scores = [score for score in scores if score >= 90]
print(f"High scores: {high_scores}")

# Passing scores with bonus
passing_with_bonus = [
    score + 5 for score in scores 
    if score >= 70 and score < 90
]
print(f"Passing scores with bonus: {passing_with_bonus}")

# Complex condition
complex_filter = [
    f"Grade A: {score}" for score in scores 
    if score >= 90 and score % 2 == 0
]
print(f"Even high scores: {complex_filter}")


# 🔢 Conditional expressions (ternary operator)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Apply different transformations based on condition
transformed = [
    num * 2 if num % 2 == 0 else num * 3 
    for num in numbers
]
print(f"Conditional transform: {transformed}")

# Create labels
labels = [
    "even" if num % 2 == 0 else "odd" 
    for num in numbers
]
print(f"Labels: {labels}")


# 📊 Performance with filtering
import time

large_data = list(range(1000000))

# Traditional filtering and transformation
start = time.time()
result1 = []
for num in large_data:
    if num % 2 == 0:
        result1.append(num * 2)
traditional_time = time.time() - start

# Comprehension with condition
start = time.time()
result2 = [num * 2 for num in large_data if num % 2 == 0]
comp_time = time.time() - start

print(f"\nPerformance comparison (filtering):")
print(f"Traditional: {traditional_time:.4f}s")
print(f"Comprehension: {comp_time:.4f}s")
print(f"Speedup: {traditional_time/comp_time:.2f}x faster")


# 💡 When to use:
# - Filtering and transforming data simultaneously
# - Data cleaning and validation
# - Creating subsets with modifications
# - Conditional data processing
# - Replacing filter() + map() combinations 