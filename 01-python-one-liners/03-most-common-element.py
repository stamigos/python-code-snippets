"""
Find Most Common Element - Get the most frequently occurring item

🎯 Problem: You need to find which element appears most often in a list.
"""

from collections import Counter


# ❌ Traditional approach (multiple lines)
def most_common_traditional(items):
    count_dict = {}
    for item in items:
        count_dict[item] = count_dict.get(item, 0) + 1
    return max(count_dict, key=count_dict.get)


# ✅ One-liner solution
most_common = lambda items: Counter(items).most_common(1)[0][0]  # noqa: E731

# 🔥 Alternative without Counter
most_common_alt = lambda items: max(set(items), key=items.count)  # noqa: E731

# 📝 Example usage
votes = ["python", "javascript", "python", "java", "python", "javascript", "python"]
winner = most_common(votes)
print(f"Votes: {votes}")
print(f"Most popular language: {winner}")
# Output: python

# 🎯 Real-world example: Log analysis
log_levels = ["INFO", "ERROR", "INFO", "WARNING", "ERROR", "ERROR", "INFO", "CRITICAL", "ERROR"]
most_frequent_level = most_common(log_levels)
print(f"Most frequent log level: {most_frequent_level}")

# 🔢 Get top N most common
top_n_common = lambda items, n: [item for item, count in Counter(items).most_common(n)]  # noqa: E731

# Example with top 3
web_requests = ["GET", "POST", "GET", "PUT", "DELETE", "GET", "POST", "GET", "PATCH"]
top_3_methods = top_n_common(web_requests, 3)
print(f"Top 3 HTTP methods: {top_3_methods}")

# 📊 Performance comparison
import time  # noqa: E402
import random  # noqa: E402

# Generate test data
test_data = [random.choice("ABCDEFGHIJ") for _ in range(10000)]

# Time Counter approach
start = time.time()
result1 = Counter(test_data).most_common(1)[0][0]
counter_time = time.time() - start

# Time manual approach
start = time.time()
result2 = max(set(test_data), key=test_data.count)
manual_time = time.time() - start

print(f"Counter approach: {counter_time:.4f}s")
print(f"Manual approach: {manual_time:.4f}s")
print(f"Results equal: {result1 == result2}")

# 💡 When to use:
# - Data analysis and statistics
# - Finding popular items in e-commerce
# - Log analysis and monitoring
# - Survey result processing
# - Game score tracking 