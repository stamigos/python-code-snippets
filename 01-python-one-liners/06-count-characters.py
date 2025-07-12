"""
Count Characters - Count occurrences of each character in a string

🎯 Problem: Get frequency count of characters in text
"""

from collections import Counter


def count_chars_traditional(text):
    """Traditional approach with dictionary"""
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts


def count_chars(text):
    """One-liner solution using Counter"""
    return dict(Counter(text))


# 📝 Example usage
text = "hello world"
char_counts = count_chars(text)
print(f"Text: '{text}'")
print(f"Character counts: {char_counts}")


# 🎯 Real-world example: Password strength analysis
def analyze_password_chars(password):
    """Analyze character distribution in password"""
    counts = count_chars(password)
    
    digits = sum(1 for c in password if c.isdigit())
    letters = sum(1 for c in password if c.isalpha())
    special = len(password) - digits - letters
    
    return {
        'total_chars': len(password),
        'unique_chars': len(counts),
        'digits': digits,
        'letters': letters,
        'special': special
    }


password = "MyP@ssw0rd123"
analysis = analyze_password_chars(password)
print(f"\nPassword analysis for '{password}':")
for key, value in analysis.items():
    print(f"  {key}: {value}")

# 🔤 Case-insensitive counting
def count_chars_case_insensitive(text):
    """Count characters ignoring case"""
    return dict(Counter(text.lower()))

text_mixed = "Hello World"
case_insensitive = count_chars_case_insensitive(text_mixed)
print(f"\nCase-insensitive count for '{text_mixed}':")
print(case_insensitive)

# 💡 When to use:
# - Text analysis and processing
# - Frequency analysis in cryptography
# - Data validation and cleaning
# - Natural language processing
# - Password strength checking 