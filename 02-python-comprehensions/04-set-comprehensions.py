"""
Set Comprehensions - Create unique collections efficiently

🎯 Problem: Generate sets with unique elements from iterables
"""


def create_set_traditional(items):
    """Traditional approach with loops"""
    result = set()
    for item in items:
        result.add(item.upper())
    return result


def create_set_comprehension(items):
    """Set comprehension approach"""
    return {item.upper() for item in items}


# 📝 Example usage
words = ["apple", "banana", "apple", "cherry", "banana"]
unique_upper = create_set_comprehension(words)
print(f"Original: {words}")
print(f"Unique uppercase: {unique_upper}")
# Output: {'APPLE', 'BANANA', 'CHERRY'}


# 🎯 Real-world example: Data cleaning
user_emails = [
    "alice@company.com",
    "bob@company.com",
    "ALICE@COMPANY.COM",  # Duplicate in different case
    "charlie@company.com",
    "bob@company.com"     # Exact duplicate
]

# Clean and deduplicate emails
clean_emails = {email.lower().strip() for email in user_emails}
print(f"Clean unique emails: {clean_emails}")

# Extract domains
domains = {email.split('@')[1] for email in user_emails}
print(f"Unique domains: {domains}")


# 🔢 Mathematical set operations
numbers1 = [1, 2, 3, 4, 5, 2, 3]
numbers2 = [3, 4, 5, 6, 7, 4, 5]

# Create unique sets
set1 = {num for num in numbers1}
set2 = {num for num in numbers2}
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

# Set operations
intersection = {num for num in numbers1 if num in numbers2}
print(f"Intersection: {intersection}")

# Squares of unique numbers
unique_squares = {num**2 for num in numbers1}
print(f"Unique squares: {unique_squares}")


# 🎨 Set comprehensions with conditions
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 8]

# Even numbers only
even_set = {num for num in data if num % 2 == 0}
print(f"Unique even numbers: {even_set}")

# Prime numbers (simple check)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_set = {num for num in data if is_prime(num)}
print(f"Prime numbers: {prime_set}")


# 🔤 String processing with sets
text = "Hello World! How are you today?"

# Unique characters
unique_chars = {char for char in text}
print(f"Unique characters: {unique_chars}")

# Unique vowels
vowels = {char.lower() for char in text if char.lower() in 'aeiou'}
print(f"Unique vowels: {vowels}")

# Unique words (case-insensitive)
words = text.split()
unique_words = {word.lower().strip('!?.,') for word in words}
print(f"Unique words: {unique_words}")


# 📊 Data analysis with sets
students = [
    {"name": "Alice", "subjects": ["Math", "Science"]},
    {"name": "Bob", "subjects": ["Math", "History"]},
    {"name": "Charlie", "subjects": ["Science", "History", "Art"]},
    {"name": "Diana", "subjects": ["Math", "Science", "Art"]}
]

# All unique subjects
all_subjects = {
    subject 
    for student in students 
    for subject in student["subjects"]
}
print(f"All subjects: {all_subjects}")

# Students taking Math
math_students = {
    student["name"] 
    for student in students 
    if "Math" in student["subjects"]
}
print(f"Math students: {math_students}")


# 🚀 Advanced set patterns
# Cartesian product with filtering
colors = ["red", "green", "blue"]
sizes = ["small", "medium", "large"]

# Valid combinations (exclude some)
valid_combinations = {
    (color, size) 
    for color in colors 
    for size in sizes 
    if not (color == "red" and size == "large")
}
print(f"Valid combinations: {valid_combinations}")

# Unique lengths
sentences = [
    "Hello world",
    "Python is great",
    "Short",
    "This is a longer sentence",
    "Hello world"  # Duplicate
]

unique_lengths = {len(sentence) for sentence in sentences}
print(f"Unique sentence lengths: {unique_lengths}")


# 🔍 Finding duplicates using sets
def find_duplicates(items):
    """Find duplicate items in a list"""
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return duplicates

data_with_dupes = [1, 2, 3, 2, 4, 5, 3, 6, 7, 1]
dupes = find_duplicates(data_with_dupes)
print(f"Duplicates: {dupes}")

# Using set comprehension to find duplicates
from collections import Counter
counts = Counter(data_with_dupes)
duplicates_comp = {item for item, count in counts.items() if count > 1}
print(f"Duplicates (comprehension): {duplicates_comp}")


# 📈 Performance comparison
import time

large_list = list(range(100000)) * 2  # Create duplicates

# Traditional set creation
start = time.time()
result1 = set()
for item in large_list:
    result1.add(item * 2)
traditional_time = time.time() - start

# Set comprehension
start = time.time()
result2 = {item * 2 for item in large_list}
comp_time = time.time() - start

print(f"\nPerformance comparison:")
print(f"Traditional: {traditional_time:.4f}s")
print(f"Set comprehension: {comp_time:.4f}s")
print(f"Speedup: {traditional_time/comp_time:.2f}x faster")


# 💡 When to use:
# - Removing duplicates with transformation
# - Mathematical set operations
# - Data deduplication and cleaning
# - Finding unique elements
# - Fast membership testing 