"""
List Flattening - Convert nested lists into a single flat list

🎯 Problem: You have a list of lists and want to combine them into one flat list.
"""

import time


def flatten_traditional(nested_list):
    """Traditional approach (multiple lines)"""
    result = []
    for sublist in nested_list:
        for item in sublist:
            result.append(item)
    return result


def flatten(nested_list):
    """One-liner solution"""
    return [item for sublist in nested_list for item in sublist]


# 📝 Example usage
nested_data = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(f"Original: {nested_data}")
print(f"Flattened: {flatten(nested_data)}")
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 🔥 Alternative using sum() for shallow nesting
def flatten_sum(nested_list):
    """Alternative using sum() for shallow nesting"""
    return sum(nested_list, [])

# 📊 Performance comparison

large_nested = [[i] * 100 for i in range(100)]

# Time the comprehension approach
start = time.time()
result1 = [item for sublist in large_nested for item in sublist]
comprehension_time = time.time() - start

# Time the sum approach
start = time.time()
result2 = sum(large_nested, [])
sum_time = time.time() - start

print(f"Comprehension time: {comprehension_time:.4f}s")
print(f"Sum time: {sum_time:.4f}s")
print(f"Results equal: {result1 == result2}")

# 💡 When to use:
# - Processing nested data structures
# - Converting 2D coordinates to 1D
# - Merging sublists from different sources
# - Preparing data for machine learning algorithms 