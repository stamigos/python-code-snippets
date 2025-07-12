"""
Generator Expressions - Memory-efficient processing with lazy evaluation

🎯 Problem: Process large datasets without consuming excessive memory
"""

import sys
import time


def process_large_list():
    """Compare list comprehension vs generator expression memory usage"""
    # List comprehension - creates entire list in memory
    list_comp = [x**2 for x in range(1000000)]
    
    # Generator expression - creates iterator, lazy evaluation
    gen_expr = (x**2 for x in range(1000000))
    
    return list_comp, gen_expr


# 📝 Example usage - Memory comparison
numbers = range(100)

# List comprehension
squared_list = [x**2 for x in numbers]
print(f"List comprehension: {type(squared_list)}")
print(f"Memory usage: {sys.getsizeof(squared_list)} bytes")

# Generator expression
squared_gen = (x**2 for x in numbers)
print(f"Generator expression: {type(squared_gen)}")
print(f"Memory usage: {sys.getsizeof(squared_gen)} bytes")

# Convert generator to list when needed
squared_from_gen = list(squared_gen)
print(f"Results are equal: {squared_list == squared_from_gen}")


# 🎯 Real-world example: Processing large files
def process_log_file(filename):
    """Process log file line by line without loading everything into memory"""
    # Generator expression for memory efficiency
    error_lines = (
        line.strip()
        for line in open(filename, 'r', encoding='utf-8')
        if 'ERROR' in line
    )
    return error_lines

# Create sample log file
sample_log = """INFO: Application started
ERROR: Database connection failed
INFO: Retrying connection
ERROR: Authentication failed
INFO: User logged in
ERROR: File not found
INFO: Processing complete"""

with open('sample.log', 'w') as f:
    f.write(sample_log)

# Process errors lazily
error_generator = process_log_file('sample.log')
print(f"Error lines generator: {error_generator}")

# Process errors one by one
for error in error_generator:
    print(f"Found error: {error}")

# Clean up
import os
os.remove('sample.log')


# 🔢 Mathematical sequences with generators
def fibonacci_generator():
    """Generate Fibonacci sequence infinitely"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Use generator expression for finite sequence
fib_gen = (x for x in fibonacci_generator())
first_10_fib = [next(fib_gen) for _ in range(10)]
print(f"First 10 Fibonacci numbers: {first_10_fib}")

# Prime number generator
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes_gen = (x for x in range(2, 100) if is_prime(x))
primes_list = list(primes_gen)
print(f"Prime numbers up to 100: {primes_list}")


# 📊 Data processing pipelines
# Simulate large dataset
def get_user_data():
    """Simulate fetching user data"""
    users = [
        {"id": i, "name": f"User{i}", "age": 20 + (i % 50), "active": i % 3 == 0}
        for i in range(1, 100000)
    ]
    return users

# Process data with generator expressions
user_data = get_user_data()

# Memory-efficient pipeline
active_adult_names = (
    user["name"]
    for user in user_data
    if user["active"] and user["age"] >= 25
)

# Process in chunks
def process_in_chunks(generator, chunk_size=1000):
    """Process generator in chunks"""
    chunk = []
    for item in generator:
        chunk.append(item)
        if len(chunk) >= chunk_size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk

# Process active adult names in chunks
chunk_count = 0
for chunk in process_in_chunks(active_adult_names, 500):
    chunk_count += 1
    print(f"Processed chunk {chunk_count} with {len(chunk)} items")
    if chunk_count >= 3:  # Limit output
        break


# 🚀 Advanced generator patterns
# Chaining generators
def chain_generators():
    """Chain multiple generators together"""
    gen1 = (x for x in range(5))
    gen2 = (x for x in range(5, 10))
    gen3 = (x for x in range(10, 15))
    
    # Chain them
    chained = (x for gen in [gen1, gen2, gen3] for x in gen)
    return list(chained)

chained_result = chain_generators()
print(f"Chained generators: {chained_result}")

# Conditional generator
def conditional_gen(data, condition):
    """Generate items based on condition"""
    return (item for item in data if condition(item))

data = range(20)
even_gen = conditional_gen(data, lambda x: x % 2 == 0)
print(f"Even numbers: {list(even_gen)}")


# 📈 Performance comparison
# Large dataset processing
large_data = range(1000000)

# List comprehension timing
start = time.time()
list_result = [x * 2 for x in large_data if x % 2 == 0]
list_time = time.time() - start
list_memory = sys.getsizeof(list_result)

# Generator expression timing (creation)
start = time.time()
gen_result = (x * 2 for x in large_data if x % 2 == 0)
gen_creation_time = time.time() - start
gen_memory = sys.getsizeof(gen_result)

# Generator consumption timing
start = time.time()
gen_consumed = list(gen_result)
gen_consumption_time = time.time() - start

print(f"\nPerformance comparison:")
print(f"List comprehension: {list_time:.4f}s, {list_memory:,} bytes")
print(f"Generator creation: {gen_creation_time:.6f}s, {gen_memory:,} bytes")
print(f"Generator consumption: {gen_consumption_time:.4f}s")
print(f"Memory savings: {list_memory / gen_memory:.0f}x less memory")


# 🎯 When to use generators
# Good use cases:
def good_generator_usage():
    """Examples of when generators are beneficial"""
    
    # 1. Processing large files (example pattern)
    # large_file_lines = (
    #     line.strip().upper()
    #     for line in open('large_file.txt', 'r')
    #     if line.strip()
    # )
    
    # 2. Infinite sequences
    infinite_counter = (i for i in range(1000000000))
    
    # 3. Pipeline processing
    raw_data = range(1000000)
    processed = (
        str(x * 2)
        for x in raw_data
        if x % 100 == 0
    )
    
    # 4. API pagination
    def api_pages():
        page = 1
        while True:
            # Simulate API call
            yield [f"item_{page}_{i}" for i in range(10)]
            page += 1
            if page > 5:  # Limit for demo
                break
    
    all_items = (
        item
        for page in api_pages()
        for item in page
    )
    
    return list(all_items)

api_items = good_generator_usage()
print(f"API items: {api_items[:5]}...")  # Show first 5


# 💡 When to use:
# - Processing large datasets
# - Memory-constrained environments
# - Infinite or very large sequences
# - Pipeline data processing
# - File processing line by line
# - API pagination and streaming
# - When you don't need all results at once 