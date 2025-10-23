"""
**Q8 - Token Counter with Tiktoken**
Question: Create a class `TokenBudgetManager` that tracks token usage across multiple LLM calls and warns when approaching budget limits.
Input: Multiple text inputs with a budget of `10000` tokens
Expected Output: Running count and warning at 80% usage
Usage: Managing costs in production LLM applications
"""

import tiktoken # type: ignore

class TokenBudgetManager:
    """Manages token usage across LLM calls with budget tracking"""
    
    def __init__(self, budget, model="gpt-3.5-turbo"):
        self.budget = budget
        self.used_tokens = 0
        self.encoding = tiktoken.encoding_for_model(model)
        self.warning_threshold = 0.8
    
    def count_tokens(self, text):
        """Counts tokens in text"""
        return len(self.encoding.encode(text))
    
    def add_usage(self, text):
        """Adds token usage and checks budget"""
        tokens = self.count_tokens(text)
        self.used_tokens += tokens
        
        usage_percent = self.used_tokens / self.budget
        
        if usage_percent >= self.warning_threshold and usage_percent < 1.0:
            print(f"Warning: {usage_percent*100:.1f}% of token budget used")
        elif usage_percent >= 1.0:
            print("Budget exceeded!")
        
        return tokens
    
    def get_remaining(self):
        """Returns remaining tokens"""
        return self.budget - self.used_tokens

# Test
manager = TokenBudgetManager(budget=100)
manager.add_usage("Hello world, let's test tiktoken.")
manager.add_usage("This is another message to track tokens.")
print(f"Remaining: {manager.get_remaining()}")
