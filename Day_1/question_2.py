"""
**Q2 - Log Parser for ML Training**
Question: Write a function that parses training log lines and extracts epoch number, loss value, and accuracy from strings formatted as "Epoch: X, Loss: Y, Accuracy: Z".
Input: `"Epoch: 5, Loss: 0.234, Accuracy: 0.891"`
Expected Output: `{"epoch": 5, "loss": 0.234, "accuracy": 0.891}`
Usage: Monitoring and analyzing machine learning model training progress
"""

import re

def parse_training_log(log:str) -> dict:

    res = dict(re.findall(r'(\w+):(\d.+)',log))
    
    return res

parse_training_log("Epoch:5, Loss:0.234, Accuracy:0.891")

# Output -> {'Epoch': '5, Loss:0.234, Accuracy:0.891'}