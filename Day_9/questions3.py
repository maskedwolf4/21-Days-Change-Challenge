"""
**Q3: Text Tokenizer for NLP**
Question: Write a function that takes a sentence and returns a dictionary with unique words as keys and their frequency counts as values (case-insensitive).

Input: `"Machine learning is great and machine learning is fun"`

Expected Output: `{'machine': 2, 'learning': 2, 'is': 2, 'great': 1, 'and': 1, 'fun': 1}`

Usage: Fundamental step in Natural Language Processing for text vectorization and feature extraction before sentiment analysis or text classification.[^8]
"""

from collections import Counter

def word_freq(sentence: str) -> dict:
    """A function that takes a sentence and returns a dictionary with unique words as keys and their frequency counts as values (case-insensitive)."""

    sentence = sentence.lower()

    word_list = sentence.split()

    word_frequncy = Counter(word_list)

    return word_frequncy

print(word_freq("Machine learning is great and machine learning is fun"))



