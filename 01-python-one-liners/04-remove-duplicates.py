"""
Remove Duplicates Preserving Order - Deduplicate while keeping original sequence

🎯 Problem: Remove duplicate items from a list while maintaining the original order.
"""


# ❌ Traditional approach (multiple lines)
def remove_duplicates_traditional(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# ✅ One-liner solution using dict.fromkeys()
def remove_duplicates(items):
    return list(dict.fromkeys(items))

# 🔥 Alternative using list comprehension with set tracking
def remove_duplicates_alt(items):
    seen = set()
    return [x for x in items if x not in seen and not seen.add(x)]

# 📝 Example usage
playlist = ["Song A", "Song B", "Song C", "Song A", "Song D", "Song B", "Song E"]
unique_playlist = remove_duplicates(playlist)
print(f"Original playlist: {playlist}")
print(f"Unique playlist: {unique_playlist}")
# Output: ['Song A', 'Song B', 'Song C', 'Song D', 'Song E']

# 🎯 Real-world example: Processing user preferences  
user_categories = ["tech", "music", "sports", "tech", "movies", 
                   "music", "books", "sports"]
unique_categories = remove_duplicates(user_categories)
print(f"User interests: {unique_categories}")

# 📊 Performance comparison with different approaches
import time  # noqa: E402

# Generate test data
test_data = list(range(1000)) * 3  # 3000 items with duplicates

# Method 1: dict.fromkeys()
start = time.time()
result1 = list(dict.fromkeys(test_data))
dict_time = time.time() - start

# Method 2: set (loses order)
start = time.time()
result2 = list(set(test_data))
set_time = time.time() - start

# Method 3: manual tracking
start = time.time()
seen = set()
result3 = []
for item in test_data:
    if item not in seen:
        seen.add(item)
        result3.append(item)
manual_time = time.time() - start

print(f"dict.fromkeys(): {dict_time:.4f}s (preserves order)")
print(f"set(): {set_time:.4f}s (loses order)")
print(f"manual: {manual_time:.4f}s (preserves order)")
print(f"Order preserved (dict): {result1 == sorted(result1)}")
print(f"Order preserved (set): {result2 == sorted(result2)}")

# 🔤 Works with any hashable type
mixed_data = [1, "hello", 2, "world", 1, "hello", 3.14, "world"]
unique_mixed = remove_duplicates(mixed_data)
print(f"Mixed data deduplicated: {unique_mixed}")

# 💡 When to use:
# - Processing user input lists
# - Cleaning data from APIs
# - Managing playlists or favorites
# - Removing duplicate database records
# - Filtering search results 