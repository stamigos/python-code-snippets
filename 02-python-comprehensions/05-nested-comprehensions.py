"""
Nested Comprehensions - Handle complex data structures elegantly

🎯 Problem: Process nested lists, matrices, and multi-dimensional data
"""


def flatten_matrix_traditional(matrix):
    """Traditional approach with nested loops"""
    result = []
    for row in matrix:
        for item in row:
            result.append(item)
    return result


def flatten_matrix_comprehension(matrix):
    """Nested comprehension approach"""
    return [item for row in matrix for item in row]


# 📝 Example usage
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = flatten_matrix_comprehension(matrix)
print(f"Matrix: {matrix}")
print(f"Flattened: {flattened}")
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 🎯 Real-world example: Processing nested JSON data
employees = [
    {
        "name": "Alice",
        "departments": ["Engineering", "Research"],
        "skills": ["Python", "JavaScript", "SQL"]
    },
    {
        "name": "Bob", 
        "departments": ["Sales", "Marketing"],
        "skills": ["Excel", "PowerPoint", "Communication"]
    },
    {
        "name": "Charlie",
        "departments": ["Engineering"],
        "skills": ["Python", "Docker", "Kubernetes"]
    }
]

# Extract all skills
all_skills = [
    skill 
    for employee in employees 
    for skill in employee["skills"]
]
print(f"All skills: {all_skills}")

# Extract department-skill pairs
dept_skill_pairs = [
    (dept, skill)
    for employee in employees
    for dept in employee["departments"]
    for skill in employee["skills"]
]
print(f"Department-skill pairs: {dept_skill_pairs[:5]}...")  # Show first 5


# 🔢 Matrix operations
# Create a multiplication table
multiplication_table = [
    [i * j for j in range(1, 6)]
    for i in range(1, 6)
]
print(f"Multiplication table:")
for row in multiplication_table:
    print(row)

# Extract diagonal elements
diagonal = [
    matrix[i][i] 
    for i in range(len(matrix))
]
print(f"Diagonal elements: {diagonal}")

# Create coordinate pairs
coords = [
    (i, j) 
    for i in range(3) 
    for j in range(3)
]
print(f"Coordinate pairs: {coords}")


# 🎨 Complex nested structures
# Generate chess board positions
chess_positions = [
    f"{chr(ord('a') + col)}{row + 1}"
    for row in range(8)
    for col in range(8)
]
print(f"Chess positions (first 10): {chess_positions[:10]}")

# Create nested dictionary structure
student_grades = {
    student["name"]: {
        subject: grade
        for subject, grade in [
            ("Math", 85), ("Science", 90), ("History", 78)
        ]
    }
    for student in [
        {"name": "Alice"}, {"name": "Bob"}, {"name": "Charlie"}
    ]
}
print(f"Student grades: {student_grades}")


# 📊 Data analysis with nested comprehensions
sales_data = [
    {"region": "North", "sales": [100, 150, 200]},
    {"region": "South", "sales": [80, 120, 180]},
    {"region": "East", "sales": [90, 140, 160]},
    {"region": "West", "sales": [110, 130, 190]}
]

# Calculate total sales per region
regional_totals = [
    {"region": region["region"], "total": sum(region["sales"])}
    for region in sales_data
]
print(f"Regional totals: {regional_totals}")

# Get all individual sales figures
all_sales = [
    sale 
    for region in sales_data 
    for sale in region["sales"]
]
print(f"All sales figures: {all_sales}")

# Create region-month-sales tuples
detailed_sales = [
    (region["region"], month, sale)
    for region in sales_data
    for month, sale in enumerate(region["sales"], 1)
]
print(f"Detailed sales: {detailed_sales}")


# 🚀 Advanced nested patterns
# Cartesian product with conditions
colors = ["red", "green", "blue"]
sizes = ["S", "M", "L"]
styles = ["casual", "formal"]

# Create product variants
product_variants = [
    {"color": color, "size": size, "style": style}
    for color in colors
    for size in sizes
    for style in styles
    if not (color == "red" and style == "formal")  # Business rule
]
print(f"Product variants: {len(product_variants)} total")
print(f"Sample variants: {product_variants[:3]}")

# Create word combinations
words1 = ["quick", "slow", "fast"]
words2 = ["brown", "red", "blue"]
words3 = ["fox", "cat", "dog"]

combinations = [
    f"{w1} {w2} {w3}"
    for w1 in words1
    for w2 in words2
    for w3 in words3
]
print(f"Word combinations (first 5): {combinations[:5]}")


# 📈 Performance considerations
import time

# Large nested structure
large_matrix = [[i * j for j in range(100)] for i in range(100)]

# Traditional nested loop
start = time.time()
result1 = []
for row in large_matrix:
    for item in row:
        result1.append(item * 2)
traditional_time = time.time() - start

# Nested comprehension
start = time.time()
result2 = [item * 2 for row in large_matrix for item in row]
comp_time = time.time() - start

print(f"\nPerformance comparison (nested):")
print(f"Traditional: {traditional_time:.4f}s")
print(f"Nested comprehension: {comp_time:.4f}s")
print(f"Speedup: {traditional_time/comp_time:.2f}x faster")


# 🔄 Readable vs. complex nested comprehensions
# Good: Simple and readable
simple_nested = [
    [x * 2 for x in row] 
    for row in matrix
]
print(f"Simple nested (readable): {simple_nested}")

# Avoid: Too complex, use traditional loops instead
# complex_nested = [
#     [x * y for x in row1 for y in row2 if x > y]
#     for row1 in matrix1
#     for row2 in matrix2
#     if sum(row1) > sum(row2)
# ]


# 💡 When to use:
# - Processing nested data structures
# - Matrix and grid operations
# - Flattening multi-dimensional data
# - Creating combinations and permutations
# - JSON/API data extraction
# - Keep it readable - if too complex, use traditional loops 