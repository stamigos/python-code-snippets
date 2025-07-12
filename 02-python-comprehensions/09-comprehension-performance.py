"""
Comprehension Performance - Speed comparisons and optimization tips

🎯 Problem: Understanding when comprehensions are faster and more efficient
"""

import time
import sys
from collections import defaultdict


def benchmark_list_creation():
    """Compare different ways to create lists"""
    n = 100000
    
    # Method 1: Traditional loop
    start = time.time()
    result1 = []
    for i in range(n):
        result1.append(i * 2)
    loop_time = time.time() - start
    
    # Method 2: List comprehension
    start = time.time()
    result2 = [i * 2 for i in range(n)]
    comp_time = time.time() - start
    
    # Method 3: Using map()
    start = time.time()
    result3 = list(map(lambda x: x * 2, range(n)))
    map_time = time.time() - start
    
    return loop_time, comp_time, map_time


# 📝 Example usage - Performance comparison
loop_time, comp_time, map_time = benchmark_list_creation()

print("List Creation Performance:")
print(f"Traditional loop: {loop_time:.4f}s")
print(f"List comprehension: {comp_time:.4f}s")
print(f"Map function: {map_time:.4f}s")
print(f"Comprehension speedup: {loop_time/comp_time:.2f}x faster than loop")
print(f"Map speedup: {loop_time/map_time:.2f}x faster than loop")


# 🎯 Real-world example: Data processing performance
def process_large_dataset():
    """Process a large dataset with different approaches"""
    # Create sample data
    data = [
        {"id": i, "name": f"User{i}", "score": i % 100, "active": i % 2 == 0}
        for i in range(50000)
    ]
    
    # Method 1: Traditional filtering and mapping
    start = time.time()
    result1 = []
    for item in data:
        if item["active"] and item["score"] > 50:
            result1.append(item["name"].upper())
    traditional_time = time.time() - start
    
    # Method 2: List comprehension
    start = time.time()
    result2 = [
        item["name"].upper()
        for item in data
        if item["active"] and item["score"] > 50
    ]
    comp_time = time.time() - start
    
    # Method 3: Filter + map
    start = time.time()
    filtered = filter(lambda x: x["active"] and x["score"] > 50, data)
    result3 = list(map(lambda x: x["name"].upper(), filtered))
    filter_map_time = time.time() - start
    
    return traditional_time, comp_time, filter_map_time, len(result1)

traditional_time, comp_time, filter_map_time, result_count = process_large_dataset()

print(f"\nData Processing Performance ({result_count} items):")
print(f"Traditional approach: {traditional_time:.4f}s")
print(f"List comprehension: {comp_time:.4f}s")
print(f"Filter + map: {filter_map_time:.4f}s")
print(f"Best performer: {'Comprehension' if comp_time < min(traditional_time, filter_map_time) else 'Filter+Map' if filter_map_time < traditional_time else 'Traditional'}")


# 🔢 Memory usage comparison
def memory_usage_comparison():
    """Compare memory usage of different approaches"""
    n = 10000
    
    # List comprehension
    list_comp = [x**2 for x in range(n)]
    list_memory = sys.getsizeof(list_comp)
    
    # Generator expression
    gen_expr = (x**2 for x in range(n))
    gen_memory = sys.getsizeof(gen_expr)
    
    # Traditional list building
    traditional_list = []
    for x in range(n):
        traditional_list.append(x**2)
    trad_memory = sys.getsizeof(traditional_list)
    
    return list_memory, gen_memory, trad_memory

list_mem, gen_mem, trad_mem = memory_usage_comparison()

print(f"\nMemory Usage Comparison (10,000 items):")
print(f"List comprehension: {list_mem:,} bytes")
print(f"Generator expression: {gen_mem:,} bytes")
print(f"Traditional list: {trad_mem:,} bytes")
print(f"Generator memory savings: {list_mem/gen_mem:.0f}x less memory")


# 📊 Dictionary comprehension performance
def dict_performance_comparison():
    """Compare dictionary creation methods"""
    keys = [f"key_{i}" for i in range(10000)]
    values = [i * 2 for i in range(10000)]
    
    # Method 1: Traditional loop
    start = time.time()
    result1 = {}
    for k, v in zip(keys, values):
        result1[k] = v
    loop_time = time.time() - start
    
    # Method 2: Dictionary comprehension
    start = time.time()
    result2 = {k: v for k, v in zip(keys, values)}
    comp_time = time.time() - start
    
    # Method 3: dict() constructor
    start = time.time()
    result3 = dict(zip(keys, values))
    dict_time = time.time() - start
    
    return loop_time, comp_time, dict_time

dict_loop_time, dict_comp_time, dict_constructor_time = dict_performance_comparison()

print(f"\nDictionary Creation Performance:")
print(f"Traditional loop: {dict_loop_time:.4f}s")
print(f"Dict comprehension: {dict_comp_time:.4f}s")
print(f"Dict constructor: {dict_constructor_time:.4f}s")
print(f"Fastest method: {'Dict()' if dict_constructor_time < min(dict_loop_time, dict_comp_time) else 'Comprehension' if dict_comp_time < dict_loop_time else 'Loop'}")


# 🎨 Nested comprehension performance
def nested_comprehension_performance():
    """Compare nested loop vs nested comprehension performance"""
    matrix_size = 200
    
    # Traditional nested loops
    start = time.time()
    result1 = []
    for i in range(matrix_size):
        row = []
        for j in range(matrix_size):
            row.append(i * j)
        result1.append(row)
    nested_loop_time = time.time() - start
    
    # Nested comprehension
    start = time.time()
    result2 = [
        [i * j for j in range(matrix_size)]
        for i in range(matrix_size)
    ]
    nested_comp_time = time.time() - start
    
    return nested_loop_time, nested_comp_time

nested_loop_time, nested_comp_time = nested_comprehension_performance()

print(f"\nNested Structure Performance (200x200 matrix):")
print(f"Nested loops: {nested_loop_time:.4f}s")
print(f"Nested comprehension: {nested_comp_time:.4f}s")
print(f"Speedup: {nested_loop_time/nested_comp_time:.2f}x faster")


# 🚀 Advanced performance patterns
def conditional_performance():
    """Compare performance with conditions"""
    data = list(range(100000))
    
    # Simple condition
    start = time.time()
    result1 = [x for x in data if x % 2 == 0]
    simple_time = time.time() - start
    
    # Complex condition
    start = time.time()
    result2 = [x for x in data if x % 2 == 0 and x % 3 == 0 and x > 100]
    complex_time = time.time() - start
    
    # Function call in condition
    def is_valid(x):
        return x % 2 == 0 and x % 3 == 0 and x > 100
    
    start = time.time()
    result3 = [x for x in data if is_valid(x)]
    function_time = time.time() - start
    
    return simple_time, complex_time, function_time, len(result1), len(result2)

simple_time, complex_time, function_time, simple_count, complex_count = conditional_performance()

print(f"\nConditional Performance:")
print(f"Simple condition: {simple_time:.4f}s ({simple_count} items)")
print(f"Complex condition: {complex_time:.4f}s ({complex_count} items)")
print(f"Function condition: {function_time:.4f}s ({complex_count} items)")
print(f"Overhead of function call: {function_time/complex_time:.2f}x slower")


# 📈 Performance optimization tips
def optimization_tips():
    """Demonstrate performance optimization techniques"""
    data = list(range(50000))
    
    # Tip 1: Move calculations outside when possible
    # Bad: recalculating in each iteration
    start = time.time()
    result1 = [x * len(data) for x in data]
    bad_time = time.time() - start
    
    # Good: calculate once
    start = time.time()
    data_len = len(data)
    result2 = [x * data_len for x in data]
    good_time = time.time() - start
    
    # Tip 2: Use appropriate data structures
    # For membership testing
    data_set = set(data)
    lookup_list = list(range(0, 50000, 100))
    
    # Bad: list membership
    start = time.time()
    result3 = [x for x in lookup_list if x in data]
    list_lookup_time = time.time() - start
    
    # Good: set membership
    start = time.time()
    result4 = [x for x in lookup_list if x in data_set]
    set_lookup_time = time.time() - start
    
    return bad_time, good_time, list_lookup_time, set_lookup_time

bad_time, good_time, list_lookup_time, set_lookup_time = optimization_tips()

print(f"\nOptimization Tips:")
print(f"Recalculating inside loop: {bad_time:.4f}s")
print(f"Calculate once outside: {good_time:.4f}s")
print(f"Improvement: {bad_time/good_time:.2f}x faster")
print(f"List membership lookup: {list_lookup_time:.4f}s")
print(f"Set membership lookup: {set_lookup_time:.4f}s")
print(f"Set lookup improvement: {list_lookup_time/set_lookup_time:.0f}x faster")


# 🎯 When to choose each approach
print(f"\n🎯 Performance Guidelines:")
print("✅ Use list comprehensions when:")
print("  - Simple transformations and filtering")
print("  - Need the entire result immediately")
print("  - Working with small to medium datasets")
print("  - Readability is important")
print()
print("✅ Use generator expressions when:")
print("  - Working with large datasets")
print("  - Processing items one at a time")
print("  - Memory usage is a concern")
print("  - Implementing lazy evaluation")
print()
print("✅ Use traditional loops when:")
print("  - Complex logic that hurts comprehension readability")
print("  - Need to break out of loop early")
print("  - Multiple operations per iteration")
print("  - Debugging complex transformations")


# 💡 When to use:
# - Performance-critical code optimization
# - Memory usage analysis
# - Choosing between different approaches
# - Large dataset processing
# - Understanding Python internals
# - Code profiling and benchmarking 