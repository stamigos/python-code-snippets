"""
Generate Fibonacci - Create Fibonacci sequence in one line

🎯 Problem: Generate a Fibonacci sequence up to n terms
"""


def fibonacci_traditional(n):
    """Traditional approach with loops"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib


def fibonacci(n):
    """One-liner using generator and reduce"""
    from functools import reduce
    return reduce(lambda x, _: x + [x[-1] + x[-2]], 
                  range(n-2), [0, 1])[:n] if n > 0 else []


# Alternative using list comprehension (more readable)
def fibonacci_alt(n):
    """Alternative one-liner approach"""
    fib = [0, 1]
    [fib.append(fib[-1] + fib[-2]) for _ in range(n-2)]
    return fib[:n] if n > 0 else []


# 📝 Example usage
print("First 10 Fibonacci numbers:")
print(fibonacci(10))
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# 🎯 Real-world example: Golden ratio approximation
def golden_ratio_approximation(n):
    """Approximate golden ratio using Fibonacci"""
    fib = fibonacci(n)
    if len(fib) < 2:
        return None
    return fib[-1] / fib[-2] if fib[-2] != 0 else None

print(f"\nGolden ratio approximation: {golden_ratio_approximation(20)}")
print(f"Actual golden ratio: {(1 + 5**0.5) / 2}")

# 🔢 Fibonacci generator (memory efficient)
def fibonacci_generator(n):
    """Memory-efficient Fibonacci generator"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(f"\nFibonacci generator (first 8): {list(fibonacci_generator(8))}")

# 💡 When to use:
# - Mathematical calculations
# - Algorithm demonstrations
# - Nature-inspired patterns
# - Performance testing
# - Educational examples 