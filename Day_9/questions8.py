"""
**Q8: Neural Network Layer Class**
Question: Design a `DenseLayer` class representing a fully connected neural layer with methods for forward pass (weighted sum + bias) and parameter initialization. Include encapsulation for weights and bias.

Input:

```python
layer = DenseLayer(input_size=3, output_size=2)
layer.initialize_weights(seed=42)
output = layer.forward([1.0, 2.0, 3.0])
```

Expected Output: `[weighted_sum_neuron1, weighted_sum_neuron2]` (actual values depend on initialized weights)

Usage: Building blocks for implementing neural networks from scratch, understanding backpropagation, and customizing deep learning architectures.
"""

import random

class DenseLayer:
    def __init__(self, input_size, output_size):
        """Initialize layer dimensions"""
        self.__input_size = input_size  # Private attribute
        self.__output_size = output_size  # Private attribute
        self.__weights = None
        self.__bias = None
    
    def initialize_weights(self, seed=42):
        """Initialize weights and bias with small random values"""
        random.seed(seed)
        # Initialize weights as 2D list: output_size x input_size
        self.__weights = [[random.uniform(-0.5, 0.5) for _ in range(self.__input_size)] 
                          for _ in range(self.__output_size)]
        # Initialize bias as 1D list
        self.__bias = [random.uniform(-0.5, 0.5) for _ in range(self.__output_size)]
    
    def forward(self, inputs):
        """Compute forward pass: output = weights * inputs + bias"""
        if self.__weights is None:
            raise ValueError("Weights not initialized. Call initialize_weights() first.")
        
        outputs = []
        for i in range(self.__output_size):
            # Compute weighted sum for each output neuron
            weighted_sum = sum(self.__weights[i][j] * inputs[j] 
                             for j in range(self.__input_size))
            output = weighted_sum + self.__bias[i]
            outputs.append(round(output, 4))
        
        return outputs
    
    def get_parameters(self):
        """Getter method for encapsulated weights and bias"""
        return {'weights': self.__weights, 'bias': self.__bias}

# Test
layer = DenseLayer(input_size=3, output_size=2)
layer.initialize_weights(seed=42)
output = layer.forward([1.0, 2.0, 3.0])
print("Output:", output)
# Output will vary based on random initialization: e.g., [0.234, -1.567]
