"""
Transpose Matrix - Flip rows and columns in a 2D list

🎯 Problem: Convert rows to columns and columns to rows
"""


def transpose_traditional(matrix):
    """Traditional approach with nested loops"""
    result = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        result.append(row)
    return result


def transpose(matrix):
    """One-liner solution using zip and unpacking"""
    return list(zip(*matrix))


# 📝 Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original matrix:")
for row in matrix:
    print(row)

transposed = transpose(matrix)
print("\nTransposed matrix:")
for row in transposed:
    print(row)

# 🎯 Real-world example: Analyzing data by columns
sales_data = [
    ["Jan", "Feb", "Mar"],
    [100, 150, 200],
    [80, 120, 180]
]

# Convert to analyze by month instead of by metric
by_month = transpose(sales_data)
print("\nData organized by month:")
for month_data in by_month:
    print(f"Month: {month_data[0]}, Sales: {month_data[1]}, "
          f"Profit: {month_data[2]}")

# 💡 When to use:
# - Matrix operations in math/science
# - Converting row-based to column-based data
# - Image processing (rotating images)
# - Data analysis and pivot operations