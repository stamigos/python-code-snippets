"""
Reverse Words - Reverse each word in a sentence while keeping word order

🎯 Problem: Reverse the characters in each word but keep words in order
"""


def reverse_words_traditional(sentence):
    """Traditional approach with loops"""
    words = sentence.split()
    reversed_words = []
    for word in words:
        reversed_word = ""
        for char in word:
            reversed_word = char + reversed_word
        reversed_words.append(reversed_word)
    return " ".join(reversed_words)


def reverse_words(sentence):
    """One-liner solution using join and list comprehension"""
    return " ".join(word[::-1] for word in sentence.split())


# 📝 Example usage
sentence = "Hello World Python"
reversed_result = reverse_words(sentence)
print(f"Original: '{sentence}'")
print(f"Reversed: '{reversed_result}'")
# Output: "olleH dlroW nohtyP"

# 🎯 Real-world example: Simple text obfuscation
def obfuscate_text(text):
    """Simple text obfuscation by reversing words"""
    return reverse_words(text)

def deobfuscate_text(text):
    """Reverse the obfuscation"""
    return reverse_words(text)  # Same operation!

original = "This is a secret message"
obfuscated = obfuscate_text(original)
deobfuscated = deobfuscate_text(obfuscated)

print(f"\nOriginal: '{original}'")
print(f"Obfuscated: '{obfuscated}'")
print(f"Deobfuscated: '{deobfuscated}'")

# 🔤 Handle punctuation separately
def reverse_words_preserve_punctuation(sentence):
    """Reverse words while preserving punctuation position"""
    import re
    
    def reverse_word(word):
        # Extract letters only, reverse them, then put back
        letters = re.findall(r'[a-zA-Z]', word)
        reversed_letters = letters[::-1]
        
        result = ""
        letter_idx = 0
        for char in word:
            if char.isalpha():
                result += reversed_letters[letter_idx]
                letter_idx += 1
            else:
                result += char
        return result
    
    return " ".join(reverse_word(word) for word in sentence.split())

complex_sentence = "Hello, World! How are you?"
complex_reversed = reverse_words_preserve_punctuation(complex_sentence)
print(f"\nComplex original: '{complex_sentence}'")
print(f"Complex reversed: '{complex_reversed}'")

# 💡 When to use:
# - Text processing and manipulation
# - Simple encryption/obfuscation
# - Data transformation
# - String algorithm practice
# - Text-based puzzles and games 