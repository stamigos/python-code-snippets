"""
Multiple Conditions - Complex filtering with logical operators

🎯 Problem: Apply multiple criteria for sophisticated data filtering
"""


def complex_filter_traditional(data):
    """Traditional approach with multiple conditions"""
    result = []
    for item in data:
        if (item["age"] >= 18 and 
            item["score"] >= 80 and 
            item["active"] == True and
            len(item["name"]) > 3):
            result.append(item)
    return result


def complex_filter_comprehension(data):
    """Comprehension with multiple conditions"""
    return [
        item for item in data
        if (item["age"] >= 18 and 
            item["score"] >= 80 and 
            item["active"] == True and
            len(item["name"]) > 3)
    ]


# 📝 Example usage
students = [
    {"name": "Alice", "age": 20, "score": 85, "active": True},
    {"name": "Bob", "age": 17, "score": 90, "active": True},
    {"name": "Charlie", "age": 19, "score": 75, "active": True},
    {"name": "Diana", "age": 21, "score": 95, "active": False},
    {"name": "Eve", "age": 22, "score": 88, "active": True}
]

qualified = complex_filter_comprehension(students)
print(f"Qualified students: {qualified}")


# 🎯 Real-world example: E-commerce product filtering
def is_discounted(product):
    """Check if product has discount"""
    return product.get("discount", 0) > 0

def in_stock(product):
    """Check if product is in stock"""
    return product.get("stock", 0) > 0

def is_featured(product):
    """Check if product is featured"""
    return product.get("featured", False)

products = [
    {"name": "Laptop", "price": 1000, "discount": 10, "stock": 5, "featured": True, "rating": 4.5},
    {"name": "Mouse", "price": 30, "discount": 0, "stock": 0, "featured": False, "rating": 4.0},
    {"name": "Keyboard", "price": 80, "discount": 15, "stock": 10, "featured": True, "rating": 4.2},
    {"name": "Monitor", "price": 300, "discount": 0, "stock": 3, "featured": False, "rating": 4.8},
    {"name": "Headphones", "price": 150, "discount": 20, "stock": 8, "featured": True, "rating": 4.3}
]

# Multiple AND conditions
premium_products = [
    product for product in products
    if (product["price"] > 100 and 
        product["rating"] >= 4.0 and
        in_stock(product) and
        is_featured(product))
]
print(f"Premium products: {[p['name'] for p in premium_products]}")

# Multiple OR conditions
special_offers = [
    product for product in products
    if (is_discounted(product) or 
        is_featured(product) or
        product["rating"] >= 4.5)
]
print(f"Special offers: {[p['name'] for p in special_offers]}")

# Complex mixed conditions
best_deals = [
    product for product in products
    if ((is_discounted(product) and product["discount"] >= 15) or
        (product["price"] < 100 and product["rating"] >= 4.0)) and
        in_stock(product)
]
print(f"Best deals: {[p['name'] for p in best_deals]}")


# 🔢 Numeric range conditions
def is_in_range(value, min_val, max_val):
    """Check if value is in range"""
    return min_val <= value <= max_val

def is_prime(n):
    """Check if number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = range(1, 101)

# Multiple numeric conditions
special_numbers = [
    n for n in numbers
    if (n % 2 == 0 and  # Even
        n % 3 == 0 and  # Divisible by 3
        is_in_range(n, 10, 90) and  # In range
        n % 5 != 0)  # Not divisible by 5
]
print(f"Special numbers: {special_numbers}")

# Prime numbers in specific ranges
categorized_primes = {
    "small": [n for n in numbers if is_prime(n) and n < 20],
    "medium": [n for n in numbers if is_prime(n) and 20 <= n < 50],
    "large": [n for n in numbers if is_prime(n) and n >= 50]
}
print(f"Categorized primes: {categorized_primes}")


# 🎨 String-based conditions
def contains_vowels(text):
    """Check if text contains vowels"""
    return any(char in 'aeiouAEIOU' for char in text)

def starts_with_capital(text):
    """Check if text starts with capital letter"""
    return text[0].isupper() if text else False

def has_numbers(text):
    """Check if text contains numbers"""
    return any(char.isdigit() for char in text)

words = [
    "Hello", "world", "Python3", "coding", "AI", "123test",
    "javascript", "HTML5", "CSS", "React", "vue", "Angular"
]

# Complex string filtering
filtered_words = [
    word for word in words
    if (len(word) >= 4 and
        contains_vowels(word) and
        starts_with_capital(word) and
        not has_numbers(word))
]
print(f"Filtered words: {filtered_words}")

# Technology stack filtering
tech_stack = [
    word for word in words
    if (len(word) >= 3 and
        (word.lower().endswith('s') or  # Plural or JavaScript
         word.lower().endswith('html') or
         word.lower().endswith('css') or
         'script' in word.lower()))
]
print(f"Tech stack: {tech_stack}")


# 📊 Date and time conditions
from datetime import datetime, timedelta

def is_weekend(date):
    """Check if date is weekend"""
    return date.weekday() >= 5

def is_business_hours(hour):
    """Check if hour is business hours"""
    return 9 <= hour <= 17

def is_recent(date, days=7):
    """Check if date is recent"""
    return (datetime.now() - date).days <= days

# Generate sample dates
base_date = datetime(2024, 1, 1)
dates = [base_date + timedelta(days=i) for i in range(30)]

# Filter dates with multiple conditions
business_weekdays = [
    date for date in dates
    if (not is_weekend(date) and
        date.day % 2 == 0 and  # Even days
        date.weekday() < 4)  # Monday to Thursday
]
print(f"Business weekdays: {len(business_weekdays)} dates")

# Event scheduling
events = [
    {"name": "Meeting", "date": datetime(2024, 1, 15, 10, 0), "priority": "high"},
    {"name": "Call", "date": datetime(2024, 1, 15, 14, 30), "priority": "medium"},
    {"name": "Review", "date": datetime(2024, 1, 16, 16, 0), "priority": "low"},
    {"name": "Planning", "date": datetime(2024, 1, 17, 9, 30), "priority": "high"}
]

# Filter events
important_events = [
    event for event in events
    if (event["priority"] in ["high", "medium"] and
        not is_weekend(event["date"]) and
        is_business_hours(event["date"].hour))
]
print(f"Important events: {[e['name'] for e in important_events]}")


# 🚀 Advanced conditional patterns
def satisfies_all_conditions(item, conditions):
    """Check if item satisfies all conditions"""
    return all(condition(item) for condition in conditions)

def satisfies_any_condition(item, conditions):
    """Check if item satisfies any condition"""
    return any(condition(item) for condition in conditions)

# Define condition functions
def is_expensive(product):
    return product["price"] > 500

def is_highly_rated(product):
    return product["rating"] >= 4.5

def is_on_sale(product):
    return product.get("discount", 0) > 0

# Apply conditions dynamically
high_end_conditions = [is_expensive, is_highly_rated]
bargain_conditions = [is_on_sale, lambda p: p["price"] < 200]

high_end_products = [
    product for product in products
    if satisfies_all_conditions(product, high_end_conditions)
]
print(f"High-end products: {[p['name'] for p in high_end_products]}")

bargain_products = [
    product for product in products
    if satisfies_any_condition(product, bargain_conditions)
]
print(f"Bargain products: {[p['name'] for p in bargain_products]}")


# 🎯 Conditional transformations
def categorize_student(student):
    """Categorize student based on multiple criteria"""
    if student["score"] >= 90 and student["age"] >= 18:
        return "Excellent Adult"
    elif student["score"] >= 80 and student["active"]:
        return "Good Active"
    elif student["score"] >= 70:
        return "Average"
    else:
        return "Needs Improvement"

# Apply conditional transformations
categorized_students = [
    {
        "name": student["name"],
        "category": categorize_student(student),
        "eligible": (student["age"] >= 18 and 
                    student["score"] >= 80 and 
                    student["active"])
    }
    for student in students
    if student["score"] >= 60  # Minimum score requirement
]
print(f"Categorized students: {categorized_students}")


# 📈 Performance considerations
import time

# Large dataset for performance testing
large_dataset = [
    {"id": i, "value": i, "category": i % 5, "active": i % 2 == 0}
    for i in range(100000)
]

# Simple condition
start = time.time()
simple_result = [item for item in large_dataset if item["value"] > 50000]
simple_time = time.time() - start

# Multiple conditions
start = time.time()
complex_result = [
    item for item in large_dataset
    if (item["value"] > 50000 and
        item["category"] in [1, 2, 3] and
        item["active"] and
        item["id"] % 10 == 0)
]
complex_time = time.time() - start

print(f"\nPerformance comparison:")
print(f"Simple condition: {simple_time:.4f}s, {len(simple_result)} items")
print(f"Multiple conditions: {complex_time:.4f}s, {len(complex_result)} items")


# 💡 When to use:
# - Complex data filtering
# - Business rule implementation
# - Data validation
# - Multi-criteria decision making
# - Quality assurance checks
# - Advanced search functionality
# - Data categorization and segmentation 