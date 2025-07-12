"""
Advanced Patterns - Pro-level comprehension techniques

🎯 Problem: Master sophisticated comprehension patterns for complex scenarios
"""

import itertools
from collections import defaultdict, Counter
import functools


def advanced_pattern_examples():
    """Demonstrate advanced comprehension patterns"""
    
    # Pattern 1: Conditional assignment within comprehension
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Multiple conditional transformations
    transformed = [
        x * 2 if x % 2 == 0 else x * 3 if x % 3 == 0 else x
        for x in numbers
    ]
    print(f"Conditional transformations: {transformed}")
    
    # Pattern 2: Tuple unpacking in comprehensions
    pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
    
    # Unpack and transform
    results = [f"{letter}_{num}" for num, letter in pairs]
    print(f"Tuple unpacking: {results}")
    
    # Pattern 3: Multiple iterables
    names = ['Alice', 'Bob', 'Charlie']
    ages = [25, 30, 35]
    cities = ['NYC', 'LA', 'Chicago']
    
    # Combine multiple iterables
    profiles = [
        f"{name} ({age}) from {city}"
        for name, age, city in zip(names, ages, cities)
    ]
    print(f"Multiple iterables: {profiles}")


# 📝 Example usage
advanced_pattern_examples()


# 🎯 Real-world example: Complex data processing
def process_sales_data():
    """Process complex sales data with advanced patterns"""
    sales_data = [
        {'rep': 'Alice', 'region': 'North', 'product': 'A', 'qty': 100, 'price': 10.0},
        {'rep': 'Bob', 'region': 'South', 'product': 'B', 'qty': 150, 'price': 15.0},
        {'rep': 'Alice', 'region': 'North', 'product': 'C', 'qty': 80, 'price': 20.0},
        {'rep': 'Charlie', 'region': 'East', 'product': 'A', 'qty': 120, 'price': 10.0},
        {'rep': 'Bob', 'region': 'South', 'product': 'B', 'qty': 200, 'price': 15.0},
    ]
    
    # Pattern: Grouped aggregation using comprehensions
    rep_totals = {
        rep: sum(sale['qty'] * sale['price'] for sale in sales_data if sale['rep'] == rep)
        for rep in {sale['rep'] for sale in sales_data}
    }
    print(f"Sales rep totals: {rep_totals}")
    
    # Pattern: Nested grouping
    region_product_summary = {
        region: {
            product: sum(sale['qty'] for sale in sales_data 
                        if sale['region'] == region and sale['product'] == product)
            for product in {sale['product'] for sale in sales_data if sale['region'] == region}
        }
        for region in {sale['region'] for sale in sales_data}
    }
    print(f"Region-product summary: {region_product_summary}")


process_sales_data()


# 🔢 Mathematical and scientific patterns
def mathematical_patterns():
    """Advanced mathematical computations using comprehensions"""
    
    # Pattern: Matrix operations
    matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    
    # Element-wise addition
    matrix_sum = [
        [a + b for a, b in zip(row_a, row_b)]
        for row_a, row_b in zip(matrix_a, matrix_b)
    ]
    print(f"Matrix addition: {matrix_sum}")
    
    # Pattern: Statistical calculations
    data_points = [
        {'x': 1, 'y': 2}, {'x': 2, 'y': 4}, {'x': 3, 'y': 6},
        {'x': 4, 'y': 8}, {'x': 5, 'y': 10}
    ]
    
    # Calculate correlation coefficient components
    n = len(data_points)
    sum_x = sum(point['x'] for point in data_points)
    sum_y = sum(point['y'] for point in data_points)
    sum_xy = sum(point['x'] * point['y'] for point in data_points)
    sum_x2 = sum(point['x']**2 for point in data_points)
    sum_y2 = sum(point['y']**2 for point in data_points)
    
    # Correlation coefficient
    correlation = (n * sum_xy - sum_x * sum_y) / (
        ((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))**0.5
    )
    print(f"Correlation coefficient: {correlation:.4f}")
    
    # Pattern: Complex number operations
    complex_numbers = [1+2j, 3+4j, 5+6j, 7+8j]
    
    # Magnitude and phase
    polar_form = [
        {'magnitude': abs(c), 'phase': c.imag/c.real if c.real != 0 else 0}
        for c in complex_numbers
    ]
    print(f"Polar form: {polar_form}")


mathematical_patterns()


# 🎨 Text processing and NLP patterns
def text_processing_patterns():
    """Advanced text processing with comprehensions"""
    
    documents = [
        "The quick brown fox jumps over the lazy dog",
        "Python is a powerful programming language",
        "Machine learning requires lots of data",
        "Data science combines statistics and programming"
    ]
    
    # Pattern: Word frequency across documents
    word_freq = defaultdict(int)
    for doc in documents:
        for word in doc.lower().split():
            word_freq[word] += 1
    
    # Find common words using comprehension
    common_words = {
        word: count for word, count in word_freq.items() 
        if count >= 2
    }
    print(f"Common words: {common_words}")
    
    # Pattern: TF-IDF like calculation
    import math
    
    # Document frequency
    doc_freq = {
        word: sum(1 for doc in documents if word in doc.lower().split())
        for word in word_freq.keys()
    }
    
    # TF-IDF scores for first document
    first_doc_words = documents[0].lower().split()
    tf_idf = {
        word: (first_doc_words.count(word) / len(first_doc_words)) * 
              math.log(len(documents) / doc_freq[word])
        for word in set(first_doc_words)
    }
    print(f"TF-IDF scores: {dict(list(tf_idf.items())[:5])}")
    
    # Pattern: N-grams generation
    def generate_ngrams(text, n):
        words = text.lower().split()
        return [' '.join(words[i:i+n]) for i in range(len(words)-n+1)]
    
    # Generate bigrams for all documents
    all_bigrams = [
        bigram
        for doc in documents
        for bigram in generate_ngrams(doc, 2)
    ]
    print(f"Sample bigrams: {all_bigrams[:5]}")


text_processing_patterns()


# 🚀 Advanced functional programming patterns
def functional_patterns():
    """Advanced functional programming with comprehensions"""
    
    # Pattern: Currying simulation
    def curry_add(x):
        return lambda y: x + y
    
    numbers = [1, 2, 3, 4, 5]
    add_ten = curry_add(10)
    
    # Apply curried function
    incremented = [add_ten(x) for x in numbers]
    print(f"Curried addition: {incremented}")
    
    # Pattern: Function composition
    def compose(f, g):
        return lambda x: f(g(x))
    
    # Compose functions
    square = lambda x: x**2
    double = lambda x: x * 2
    square_then_double = compose(double, square)
    
    # Apply composed function
    composed_results = [square_then_double(x) for x in numbers]
    print(f"Composed functions: {composed_results}")
    
    # Pattern: Recursive-like patterns
    def factorial_like(n):
        return functools.reduce(lambda acc, x: acc * x, range(1, n+1), 1)
    
    # Generate factorials
    factorials = [factorial_like(n) for n in range(1, 6)]
    print(f"Factorial-like: {factorials}")


functional_patterns()


# 🎯 Performance optimization patterns
def optimization_patterns():
    """Advanced patterns for performance optimization"""
    
    # Pattern: Lazy evaluation chains
    def lazy_chain():
        data = range(1000000)
        
        # Chain operations lazily
        pipeline = (
            x * 2 for x in data
            if x % 2 == 0
        )
        
        # Take only first 5 results
        return list(itertools.islice(pipeline, 5))
    
    lazy_results = lazy_chain()
    print(f"Lazy chain results: {lazy_results}")
    
    # Pattern: Conditional generator creation
    def conditional_generator(use_complex=False):
        data = range(100)
        
        if use_complex:
            return (x**3 + 2*x**2 + x + 1 for x in data if x % 7 == 0)
        else:
            return (x * 2 for x in data if x % 2 == 0)
    
    simple_gen = conditional_generator(False)
    complex_gen = conditional_generator(True)
    
    print(f"Simple generator: {list(itertools.islice(simple_gen, 5))}")
    print(f"Complex generator: {list(itertools.islice(complex_gen, 5))}")


optimization_patterns()


# 🔍 Advanced filtering and validation patterns
def validation_patterns():
    """Advanced validation and filtering patterns"""
    
    # Pattern: Multi-level validation
    def validate_user_data(users):
        # Define validation rules
        validations = {
            'age': lambda x: 18 <= x <= 120,
            'email': lambda x: '@' in x and '.' in x,
            'score': lambda x: 0 <= x <= 100
        }
        
        # Apply all validations
        return [
            {**user, 'valid': all(
                validations[field](user[field]) 
                for field in validations.keys()
                if field in user
            )}
            for user in users
        ]
    
    users = [
        {'name': 'Alice', 'age': 25, 'email': 'alice@example.com', 'score': 85},
        {'name': 'Bob', 'age': 16, 'email': 'bob@invalid', 'score': 95},
        {'name': 'Charlie', 'age': 30, 'email': 'charlie@test.com', 'score': 75}
    ]
    
    validated_users = validate_user_data(users)
    print(f"Validated users: {validated_users}")
    
    # Pattern: Complex business rules
    def apply_business_rules(products):
        return [
            {
                **product,
                'category': (
                    'premium' if product['price'] > 1000 else
                    'mid-range' if product['price'] > 500 else
                    'budget'
                ),
                'discount': (
                    20 if product['rating'] >= 4.5 and product['stock'] > 10 else
                    10 if product['rating'] >= 4.0 else
                    0
                )
            }
            for product in products
        ]
    
    products = [
        {'name': 'Laptop', 'price': 1200, 'rating': 4.7, 'stock': 15},
        {'name': 'Mouse', 'price': 50, 'rating': 4.2, 'stock': 5},
        {'name': 'Monitor', 'price': 800, 'rating': 4.8, 'stock': 20}
    ]
    
    categorized_products = apply_business_rules(products)
    print(f"Categorized products: {categorized_products}")


validation_patterns()


# 🎪 Creative and unusual patterns
def creative_patterns():
    """Creative and unusual comprehension patterns"""
    
    # Pattern: ASCII art generation
    def generate_pyramid(height):
        return [
            ' ' * (height - i - 1) + '*' * (2 * i + 1)
            for i in range(height)
        ]
    
    pyramid = generate_pyramid(5)
    print("ASCII Pyramid:")
    for line in pyramid:
        print(line)
    
    # Pattern: State machines
    def state_machine_simulation():
        states = ['idle', 'processing', 'complete', 'error']
        transitions = {
            'idle': 'processing',
            'processing': 'complete',
            'complete': 'idle',
            'error': 'idle'
        }
        
        current_state = 'idle'
        steps = 10
        
        # Simulate state transitions
        state_history = []
        for _ in range(steps):
            state_history.append(current_state)
            current_state = transitions.get(current_state, 'error')
        
        return state_history
    
    states = state_machine_simulation()
    print(f"State machine simulation: {states}")
    
    # Pattern: Dynamic code generation
    def generate_validators():
        field_types = {
            'name': str,
            'age': int,
            'email': str,
            'active': bool
        }
        
        # Generate validation functions
        validators = {
            field: (lambda t: lambda x: isinstance(x, t))(field_type)
            for field, field_type in field_types.items()
        }
        
        return validators
    
    validators = generate_validators()
    test_data = {'name': 'Alice', 'age': 25, 'email': 'alice@test.com', 'active': True}
    
    validation_results = {
        field: validators[field](test_data[field])
        for field in validators.keys()
        if field in test_data
    }
    print(f"Dynamic validation: {validation_results}")


creative_patterns()


# 💡 When to use advanced patterns:
print("\n💡 Advanced Pattern Guidelines:")
print("✅ Use when you need:")
print("  - Complex data transformations")
print("  - High performance with readability")
print("  - Functional programming paradigms")
print("  - Mathematical computations")
print("  - Advanced filtering logic")
print("  - Creative problem solving")
print()
print("⚠️  Avoid when:")
print("  - Pattern becomes unreadable")
print("  - Simple loop would be clearer")
print("  - Debugging becomes difficult")
print("  - Performance doesn't matter")
print("  - Team unfamiliar with patterns")

# 🎯 Master-level considerations:
# - Readability vs performance trade-offs
# - Memory usage optimization
# - Functional programming principles
# - Code maintainability
# - Team skill level and preferences
# - Problem domain complexity 