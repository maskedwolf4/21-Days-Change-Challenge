"""
### Q6

**Question:** Build a `VectorSpace` class that performs dot product, magnitude calculation, and cosine similarity between two vectors.

**Input:** `v1 = VectorSpace([1][2][3]); v2 = VectorSpace([4][5][6]); v1.cosine_similarity(v2)`

**Expected Output:** `0.9746318461970762`

**Usage:** Embedding similarity calculations in RAG systems and recommendation engines.
"""


import math

class VectorSpace:
    """Performs vector operations for similarity calculations"""
    
    def __init__(self, vector):
        self.vector = vector
    
    def dot_product(self, other):
        """Calculate dot product with another vector"""
        return sum(a * b for a, b in zip(self.vector, other.vector))
    
    def magnitude(self):
        """Calculate vector magnitude"""
        return math.sqrt(sum(x ** 2 for x in self.vector))
    
    def cosine_similarity(self, other):
        """Calculate cosine similarity with another vector"""
        dot_prod = self.dot_product(other)
        mag_product = self.magnitude() * other.magnitude()
        return dot_prod / mag_product if mag_product != 0 else 0

# Usage
v1 = VectorSpace([1, 2, 3])
v2 = VectorSpace([4, 5, 6])
print(v1.cosine_similarity(v2))  # 0.9746318461970762

