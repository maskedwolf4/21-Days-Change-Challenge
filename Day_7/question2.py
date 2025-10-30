"""
### Q2

**Question:** Create a function that checks if a given number is prime. Return True if prime, False otherwise.

**Input:** `17`

**Expected Output:** `True`

**Usage:** Number theory applications in cryptography for secure bioinformatics databases; generating unique IDs; algorithmic efficiency testing
"""

def is_prime(n):
    """
    Check if a number is prime (only divisible by 1 and itself).
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    
    # Check divisibility by 2, then odd numbers up to sqrt(n)
    if n % 2 == 0:
        return False
    
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    
    return True

# Test
result = is_prime(17)
print(f"Is prime: {result}")  # Output: True



