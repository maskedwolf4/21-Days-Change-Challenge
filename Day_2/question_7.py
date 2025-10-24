"""
### Q7

**Question:** Design a `RateLimiter` class that tracks API calls per user and enforces rate limits (e.g., max 100 calls per minute).

**Input:** `limiter = RateLimiter(max_calls=3, window=60); [limiter.allow_request("user1") for _ in range(4)]`

**Expected Output:** `[True, True, True, False]`

**Usage:** Protectin
"""

import time
from collections import defaultdict, deque

class RateLimiter:
    """Enforce rate limits per user using sliding window"""
    
    def __init__(self, max_calls, window):
        self.max_calls = max_calls
        self.window = window  # in seconds
        self.calls = defaultdict(deque)
    
    def allow_request(self, user_id):
        """Check if request is allowed for user"""
        current_time = time.time()
        user_calls = self.calls[user_id]
        
        # Remove expired timestamps
        while user_calls and current_time - user_calls[0] > self.window:
            user_calls.popleft()
        
        # Check if under limit
        if len(user_calls) < self.max_calls:
            user_calls.append(current_time)
            return True
        return False

# Usage
limiter = RateLimiter(max_calls=3, window=60)
results = [limiter.allow_request("user1") for _ in range(4)]
print(results)  # [True, True, True, False]
