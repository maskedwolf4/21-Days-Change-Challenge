"""
### Q8

**Question:** Create a `CircularBuffer` class with fixed size that overwrites oldest data when full, with methods to add, retrieve, and check if full.

**Input:** `buffer = CircularBuffer(3); buffer.add(1); buffer.add(2); buffer.add(3); buffer.add(4); buffer.get_all()`

**Expected Output:** `[2][3][4]`

**Usage:** Real-time streaming data processing in IoT sensors and time-series analysis.
"""


class CircularBuffer:
    """Fixed-size buffer that overwrites oldest data when full"""
    
    def __init__(self, size):
        self.size = size
        self.buffer = []
        self.pointer = 0
    
    def add(self, item):
        """Add item to buffer, overwriting oldest if full"""
        if len(self.buffer) < self.size:
            self.buffer.append(item)
        else:
            self.buffer[self.pointer] = item
        self.pointer = (self.pointer + 1) % self.size
    
    def get_all(self):
        """Return all items in insertion order"""
        if len(self.buffer) < self.size:
            return self.buffer.copy()
        return self.buffer[self.pointer:] + self.buffer[:self.pointer]
    
    def is_full(self):
        """Check if buffer is at capacity"""
        return len(self.buffer) == self.size

# Usage
buffer = CircularBuffer(3)
buffer.add(1)
buffer.add(2)
buffer.add(3)
buffer.add(4)
print(buffer.get_all())  # [2, 3, 4]
