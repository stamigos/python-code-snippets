"""
Dictionary Merging - Combine multiple dictionaries into one

🎯 Problem: You need to merge multiple dictionaries, with later ones overriding earlier ones.
"""


# ❌ Traditional approach (multiple lines)
def merge_traditional(dict1, dict2, dict3):
    result = dict1.copy()
    result.update(dict2)
    result.update(dict3)
    return result

# ✅ One-liner solution (Python 3.9+)
def merge(*dicts):
    """Merge multiple dictionaries"""
    return {k: v for d in dicts for k, v in d.items()}


# 🔥 Alternative using dictionary unpacking (Python 3.5+)
def merge_unpack(*dicts):
    """Alternative using dictionary unpacking"""
    if not dicts:
        return {}
    return {**dict()} | {k: v for d in dicts for k, v in d.items()}


# Even cleaner with walrus operator (Python 3.8+)
def merge_clean(*dicts):
    """Clean merge using dictionary union"""
    return dict() | {k: v for d in dicts for k, v in d.items()}

# 📝 Example usage
config_defaults = {"theme": "light", "font_size": 12, "auto_save": True}
user_preferences = {"theme": "dark", "font_size": 14}
session_settings = {"auto_save": False, "last_file": "project.py"}

# Merge all configurations
final_config = merge(config_defaults, user_preferences, session_settings)
print(f"Final config: {final_config}")
# Output: {'theme': 'dark', 'font_size': 14, 'auto_save': False, 'last_file': 'project.py'}


# 🎯 Real-world example: API response merging
api_response_1 = {"user_id": 123, "name": "Alice", 
                  "email": "alice@example.com"}
api_response_2 = {"user_id": 123, "last_login": "2024-01-15", 
                   "premium": True}
api_response_3 = {"user_id": 123, "email": "alice.new@example.com"}

complete_user = merge(api_response_1, api_response_2, api_response_3)
print(f"Complete user data: {complete_user}")

# 💡 When to use:
# - Configuration management
# - API response combining
# - Default values with overrides
# - Data transformation pipelines 