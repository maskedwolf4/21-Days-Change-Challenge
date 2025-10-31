"""
**Q9: Data Pipeline Manager with Inheritance**
Question: Create a base class `DataProcessor` with method `process()` and two derived classes: `ImageProcessor` (resizes images to specified dimensions) and `TextProcessor` (removes special characters and converts to lowercase). Implement using inheritance and method overriding.

Input:

```python
img_processor = ImageProcessor(target_size=(224, 224))
text_processor = TextProcessor()
img_processor.process("image_data: 1920x1080")
text_processor.process("Hello World! @2024")
```

Expected Output:

```python
ImageProcessor: "Resized to (224, 224)"
TextProcessor: "hello world 2024"
```

Usage: Building modular ETL pipelines for multi-modal AI systems that process different data types (images, text, audio).
"""

class DataProcessor:
    """Base class for data processing"""
    def __init__(self):
        self.processor_type = "Generic"
    
    def process(self, data):
        """Base method to be overridden by subclasses"""
        raise NotImplementedError("Subclasses must implement process() method")
    
    def log(self, message):
        """Common logging functionality"""
        print(f"[{self.processor_type}] {message}")


class ImageProcessor(DataProcessor):
    """Processes image data"""
    def __init__(self, target_size):
        super().__init__()
        self.processor_type = "ImageProcessor"
        self.target_size = target_size
    
    def process(self, data):
        """Override: Simulates image resizing"""
        self.log(f"Processing: {data}")
        result = f"Resized to {self.target_size}"
        return result


class TextProcessor(DataProcessor):
    """Processes text data"""
    def __init__(self):
        super().__init__()
        self.processor_type = "TextProcessor"
    
    def process(self, data):
        """Override: Removes special characters and converts to lowercase"""
        import re
        # Remove special characters except spaces
        cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', data)
        result = cleaned.lower()
        self.log(f"Cleaned text")
        return result


# Test
img_processor = ImageProcessor(target_size=(224, 224))
text_processor = TextProcessor()

print(img_processor.process("image_data: 1920x1080"))
print(text_processor.process("Hello World! @2024"))

# Output:
# [ImageProcessor] Processing: image_data: 1920x1080
# Resized to (224, 224)
# [TextProcessor] Cleaned text
# hello world 2024

