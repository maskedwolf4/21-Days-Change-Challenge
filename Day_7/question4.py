"""
### Q4

**Question:** Create a function to generate a list of Fibonacci numbers up to a given limit (inclusive).

**Input:** `limit=20`

**Expected Output:** `[0][1][1][2][3][5][8][13]`

**Usage:** Modeling exponential growth in populations; phyllotaxis patterns in plant biology; recursive algorithms in computational biology
"""

def fibonacci_up_to(limit):
    """
    Generate Fibonacci sequence up to given limit (inclusive).
    F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2) for n>1
    """
    if limit < 0:
        return []
    
    fib = [0, 1]
    while True:
        next_fib = fib[-1] + fib[-2]
        if next_fib > limit:
            break
        fib.append(next_fib)
    
    return fib

# Test
result = fibonacci_up_to(20)
print(f"Fibonacci up to 20: {result}")  # Output: [0, 1, 1, 2, 3, 5, 8, 13]
