"""
Check Palindrome - Verify if text reads the same forwards and backwards

🎯 Problem: Determine if a string is a palindrome
"""

import re


def is_palindrome_traditional(text):
    """Traditional approach with loops"""
    # Clean the text: remove non-alphanumeric and convert to lowercase
    cleaned = ""
    for char in text:
        if char.isalnum():
            cleaned += char.lower()
    
    # Check if it's the same forwards and backwards
    for i in range(len(cleaned) // 2):
        if cleaned[i] != cleaned[len(cleaned) - 1 - i]:
            return False
    return True


def is_palindrome(text):
    """One-liner solution"""
    clean = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    return clean == clean[::-1]


# Even shorter for simple cases (no cleaning)
def is_palindrome_simple(text):
    """Simple palindrome check without cleaning"""
    return text == text[::-1]


# 📝 Example usage
test_cases = [
    "racecar",
    "A man, a plan, a canal: Panama",
    "race a car",
    "hello",
    "Madam",
    "Was it a car or a cat I saw?"
]

print("Palindrome test results:")
for text in test_cases:
    result = is_palindrome(text)
    print(f"'{text}' -> {result}")

# 🎯 Real-world example: DNA sequence analysis
def is_dna_palindrome(sequence):
    """Check if DNA sequence is palindromic"""
    # DNA palindromes read the same on both strands
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    
    # Get reverse complement
    reverse_comp = ''.join(complement.get(base, base) 
                           for base in sequence[::-1])
    
    return sequence == reverse_comp

dna_sequences = ["GAATTC", "AAGCTT", "ATCGAT", "ABCDEF"]
print("\nDNA palindrome analysis:")
for seq in dna_sequences:
    if all(c in 'ATGC' for c in seq):
        result = is_dna_palindrome(seq)
        print(f"'{seq}' -> {result}")


# 🔢 Numeric palindrome
def is_numeric_palindrome(num):
    """Check if number is palindromic"""
    return str(num) == str(num)[::-1]


numbers = [121, 1331, 12321, 123, 1234321]
print("\nNumeric palindromes:")
for num in numbers:
    print(f"{num} -> {is_numeric_palindrome(num)}")

# 💡 When to use:
# - Text processing and validation
# - DNA/RNA sequence analysis
# - Number theory problems
# - Data validation
# - Algorithm practice 