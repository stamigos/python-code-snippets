"""
Comprehension with Functions - Apply custom logic elegantly

🎯 Problem: Use functions within comprehensions for complex transformations
"""

import math
import re
from datetime import datetime, timedelta


def process_with_functions_traditional(data):
    """Traditional approach with explicit function calls"""
    result = []
    for item in data:
        processed = str(item).upper()
        if len(processed) > 3:
            result.append(processed)
    return result


def process_with_functions_comprehension(data):
    """Comprehension with function calls"""
    return [str(item).upper() for item in data if len(str(item)) > 3]


# 📝 Example usage
data = ["hello", "hi", "world", "python", "code", "a"]
result = process_with_functions_comprehension(data)
print(f"Original: {data}")
print(f"Processed: {result}")
# Output: ['HELLO', 'WORLD', 'PYTHON', 'CODE']


# 🎯 Real-world example: Data validation and transformation
def validate_email(email):
    """Simple email validation"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def normalize_email(email):
    """Normalize email address"""
    return email.lower().strip()

# Process user emails
user_emails = [
    "  Alice@Company.COM  ",
    "bob@invalid",
    "charlie@example.org",
    "DIANA@COMPANY.COM",
    "invalid-email",
    "eve@test.net"
]

# Validate and normalize in one comprehension
valid_emails = [
    normalize_email(email)
    for email in user_emails
    if validate_email(email.strip())
]
print(f"Valid emails: {valid_emails}")


# 🔢 Mathematical functions in comprehensions
def is_perfect_square(n):
    """Check if number is a perfect square"""
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

def prime_factors(n):
    """Get prime factors of a number"""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

numbers = range(1, 26)

# Find perfect squares
perfect_squares = [n for n in numbers if is_perfect_square(n)]
print(f"Perfect squares: {perfect_squares}")

# Create factor mapping
factor_map = {
    n: prime_factors(n)
    for n in numbers
    if len(prime_factors(n)) > 1
}
print(f"Prime factors: {dict(list(factor_map.items())[:5])}")


# 🔤 String processing functions
def clean_text(text):
    """Remove punctuation and extra spaces"""
    cleaned = re.sub(r'[^\w\s]', '', text)
    return ' '.join(cleaned.split())

def word_count(text):
    """Count words in text"""
    return len(clean_text(text).split())

def extract_hashtags(text):
    """Extract hashtags from text"""
    return re.findall(r'#\w+', text)

# Process social media posts
posts = [
    "Having a great day! #sunny #happy",
    "Python is awesome!! #coding #python #learning",
    "Short post",
    "Love this weather... #nature #peaceful #weekend",
    "Just finished a project! #achievement #proud"
]

# Extract posts with hashtags
posts_with_tags = [
    {
        "text": post,
        "hashtags": extract_hashtags(post),
        "word_count": word_count(post)
    }
    for post in posts
    if extract_hashtags(post)  # Only posts with hashtags
]
print(f"Posts with hashtags: {posts_with_tags}")


# 📊 Data transformation functions
def calculate_age(birth_date):
    """Calculate age from birth date"""
    today = datetime.now()
    return today.year - birth_date.year - (
        (today.month, today.day) < (birth_date.month, birth_date.day)
    )

def categorize_age(age):
    """Categorize age into groups"""
    if age < 18:
        return "Minor"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"

def format_currency(amount):
    """Format number as currency"""
    return f"${amount:,.2f}"

# Process employee data
employees = [
    {"name": "Alice", "birth_date": datetime(1990, 5, 15), "salary": 75000},
    {"name": "Bob", "birth_date": datetime(1985, 8, 20), "salary": 85000},
    {"name": "Charlie", "birth_date": datetime(1975, 12, 10), "salary": 95000},
    {"name": "Diana", "birth_date": datetime(2000, 3, 25), "salary": 65000}
]

# Create employee profiles
employee_profiles = [
    {
        "name": emp["name"],
        "age": calculate_age(emp["birth_date"]),
        "category": categorize_age(calculate_age(emp["birth_date"])),
        "salary": format_currency(emp["salary"])
    }
    for emp in employees
]
print(f"Employee profiles: {employee_profiles}")


# 🚀 Advanced function patterns
def apply_discount(price, discount_percent):
    """Apply discount to price"""
    return price * (1 - discount_percent / 100)

def calculate_tax(price, tax_rate):
    """Calculate tax on price"""
    return price * (1 + tax_rate / 100)

def format_product_name(name):
    """Format product name"""
    return name.title().replace("_", " ")

# Process product catalog
products = [
    {"name": "wireless_headphones", "price": 150, "discount": 20},
    {"name": "smartphone_case", "price": 25, "discount": 15},
    {"name": "laptop_stand", "price": 50, "discount": 10},
    {"name": "usb_cable", "price": 15, "discount": 5}
]

# Calculate final prices with tax (8%)
final_prices = [
    {
        "name": format_product_name(product["name"]),
        "original_price": format_currency(product["price"]),
        "discounted_price": format_currency(
            apply_discount(product["price"], product["discount"])
        ),
        "final_price": format_currency(
            calculate_tax(
                apply_discount(product["price"], product["discount"]),
                8
            )
        )
    }
    for product in products
]
print(f"Final prices: {final_prices}")


# 🎨 Combining multiple functions
def process_text_pipeline(text):
    """Text processing pipeline"""
    # Chain multiple transformations
    return text.strip().lower().replace("_", " ").title()

def is_valid_product(product):
    """Check if product is valid"""
    return (
        product.get("name") and
        product.get("price", 0) > 0 and
        len(product.get("name", "")) > 2
    )

def enhance_product(product):
    """Enhance product with computed fields"""
    if not is_valid_product(product):
        return None
    
    return {
        "name": process_text_pipeline(product["name"]),
        "price": product["price"],
        "category": "electronics",  # Default category
        "sku": f"SKU_{product['name'][:3].upper()}_{product['price']}"
    }

# Process raw product data
raw_products = [
    {"name": "wireless_mouse", "price": 30},
    {"name": "keyboard", "price": 80},
    {"name": "a", "price": 5},  # Invalid: name too short
    {"name": "monitor", "price": 0},  # Invalid: price zero
    {"name": "webcam", "price": 45}
]

# Filter and enhance products
enhanced_products = [
    enhance_product(product)
    for product in raw_products
    if is_valid_product(product)
]
print(f"Enhanced products: {enhanced_products}")


# 🔍 Custom sorting and filtering functions
def sort_key_function(item):
    """Custom sort key"""
    return (item["priority"], item["name"])

def filter_by_criteria(item):
    """Complex filtering criteria"""
    return (
        item["priority"] > 1 and
        item["status"] == "active" and
        len(item["name"]) > 3
    )

# Process task list
tasks = [
    {"name": "review_code", "priority": 3, "status": "active"},
    {"name": "fix_bug", "priority": 2, "status": "active"},
    {"name": "write_docs", "priority": 1, "status": "inactive"},
    {"name": "test", "priority": 2, "status": "active"},
    {"name": "deploy", "priority": 3, "status": "active"}
]

# Filter and sort tasks
important_tasks = sorted(
    [task for task in tasks if filter_by_criteria(task)],
    key=sort_key_function,
    reverse=True
)
print(f"Important tasks: {important_tasks}")


# 💡 When to use:
# - Complex data transformations
# - Validation and filtering
# - Mathematical calculations
# - Text processing and formatting
# - Business logic application
# - Data pipeline operations
# - Custom sorting and grouping 