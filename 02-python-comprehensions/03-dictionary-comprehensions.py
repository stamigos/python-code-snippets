"""
Dictionary Comprehensions - Transform key-value pairs efficiently

🎯 Problem: Create or transform dictionaries from iterables
"""


def create_dict_traditional(keys, values):
    """Traditional approach with loops"""
    result = {}
    for key, value in zip(keys, values):
        result[key] = value
    return result


def create_dict_comprehension(keys, values):
    """Dictionary comprehension approach"""
    return {key: value for key, value in zip(keys, values)}


# 📝 Example usage
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

name_age_dict = create_dict_comprehension(names, ages)
print(f"Name-age mapping: {name_age_dict}")
# Output: {'Alice': 25, 'Bob': 30, 'Charlie': 35}


# 🎯 Real-world example: Processing CSV-like data
headers = ["name", "age", "city", "salary"]
employee_data = [
    ["Alice", 25, "New York", 70000],
    ["Bob", 30, "San Francisco", 85000],
    ["Charlie", 35, "Seattle", 90000]
]

# Create employee records
employees = [
    {header: value for header, value in zip(headers, employee)}
    for employee in employee_data
]
print(f"Employee records: {employees}")

# Create salary lookup
salary_lookup = {
    employee[0]: employee[3] 
    for employee in employee_data
}
print(f"Salary lookup: {salary_lookup}")


# 🔢 Common dictionary transformation patterns
numbers = [1, 2, 3, 4, 5]

# Create squares dictionary
squares = {num: num**2 for num in numbers}
print(f"Squares: {squares}")

# Create factorials
import math
factorials = {num: math.factorial(num) for num in numbers}
print(f"Factorials: {factorials}")

# String transformations
words = ["hello", "world", "python"]
word_lengths = {word: len(word) for word in words}
print(f"Word lengths: {word_lengths}")

# Character frequency
text = "hello world"
char_freq = {char: text.count(char) for char in set(text)}
print(f"Character frequency: {char_freq}")


# 🎨 Dictionary comprehensions with conditions
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 96}

# Filter high performers
high_performers = {name: score for name, score in scores.items() if score >= 90}
print(f"High performers: {high_performers}")

# Add grade letters
grades = {
    name: "A" if score >= 90 else "B" if score >= 80 else "C"
    for name, score in scores.items()
}
print(f"Grades: {grades}")

# Bonus calculation
bonuses = {
    name: score * 100 if score >= 90 else score * 50
    for name, score in scores.items()
}
print(f"Bonuses: {bonuses}")


# 🔄 Inverting dictionaries
original = {"a": 1, "b": 2, "c": 3}
inverted = {value: key for key, value in original.items()}
print(f"Original: {original}")
print(f"Inverted: {inverted}")

# Handle duplicate values when inverting
colors = {"red": "#FF0000", "green": "#00FF00", "blue": "#0000FF"}
hex_to_color = {hex_code: color for color, hex_code in colors.items()}
print(f"Hex to color: {hex_to_color}")


# 📊 Grouping data
students = [
    {"name": "Alice", "grade": "A", "subject": "Math"},
    {"name": "Bob", "grade": "B", "subject": "Math"},
    {"name": "Charlie", "grade": "A", "subject": "Science"},
    {"name": "Diana", "grade": "A", "subject": "Math"}
]

# Group by grade
from collections import defaultdict
grade_groups = defaultdict(list)
for student in students:
    grade_groups[student["grade"]].append(student["name"])

grade_dict = {grade: names for grade, names in grade_groups.items()}
print(f"Students by grade: {dict(grade_dict)}")

# Count by subject
subject_counts = {}
for student in students:
    subject = student["subject"]
    subject_counts[subject] = subject_counts.get(subject, 0) + 1

print(f"Subject counts: {subject_counts}")


# 🚀 Advanced patterns
# Nested dictionary comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
coord_dict = {
    (i, j): matrix[i][j] 
    for i in range(len(matrix)) 
    for j in range(len(matrix[i]))
}
print(f"Coordinate dictionary: {coord_dict}")

# Multiple data sources
first_names = ["John", "Jane", "Bob"]
last_names = ["Doe", "Smith", "Johnson"]
ages = [30, 25, 35]

people = {
    f"{first}_{last}": age 
    for first, last, age in zip(first_names, last_names, ages)
}
print(f"People: {people}")


# 💡 When to use:
# - Creating dictionaries from iterables
# - Transforming existing dictionaries
# - Data mapping and lookup tables
# - Configuration processing
# - JSON/API response transformation 