"""
Filter Dictionary - Filter dictionary items by condition

🎯 Problem: Keep only dictionary items that meet specific criteria
"""


def filter_dict_traditional(data, condition):
    """Traditional approach with loops"""
    result = {}
    for key, value in data.items():
        if condition(key, value):
            result[key] = value
    return result


def filter_dict(data, condition):
    """One-liner solution using dictionary comprehension"""
    return {k: v for k, v in data.items() if condition(k, v)}


# 📝 Example usage
scores = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'Diana': 96,
    'Eve': 88
}

# Filter students with scores >= 90
high_scorers = filter_dict(scores, lambda k, v: v >= 90)
print(f"High scorers (>=90): {high_scorers}")

# 🎯 Real-world example: API response filtering
user_data = {
    'user_123': {'name': 'Alice', 'active': True, 'premium': False},
    'user_456': {'name': 'Bob', 'active': False, 'premium': True},
    'user_789': {'name': 'Charlie', 'active': True, 'premium': True},
    'user_101': {'name': 'Diana', 'active': True, 'premium': False}
}

# Filter active premium users
active_premium = filter_dict(
    user_data, 
    lambda k, v: v['active'] and v['premium']
)
print(f"\nActive premium users: {active_premium}")

# 🔢 Common filtering patterns
def filter_by_value(data, condition):
    """Filter dictionary by value only"""
    return {k: v for k, v in data.items() if condition(v)}

def filter_by_key(data, condition):
    """Filter dictionary by key only"""
    return {k: v for k, v in data.items() if condition(k)}

# Examples of common patterns
products = {
    'laptop': 999,
    'phone': 599,
    'tablet': 299,
    'watch': 199
}

# Filter expensive items (>= 500)
expensive = filter_by_value(products, lambda v: v >= 500)
print(f"\nExpensive products: {expensive}")

# Filter items with short names (<= 5 chars)
short_names = filter_by_key(products, lambda k: len(k) <= 5)
print(f"Products with short names: {short_names}")

# 💡 When to use:
# - Data cleaning and preprocessing
# - API response filtering
# - Configuration management
# - User permission filtering
# - Database query result processing 