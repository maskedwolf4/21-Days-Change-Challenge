"""
**Q10: Model Performance Evaluator with Static Methods**
Question: Design a `ModelEvaluator` class with static methods to calculate precision, recall, and F1-score from true positives, false positives, and false negatives. Add a class method to generate a confusion matrix summary.

Input:

```python
precision = ModelEvaluator.calculate_precision(tp=80, fp=20)
recall = ModelEvaluator.calculate_recall(tp=80, fn=15)
f1 = ModelEvaluator.calculate_f1(precision, recall)
```

Expected Output:

```python
precision: 0.8
recall: 0.842
f1: 0.82
```

Usage: Essential for evaluating classification models in medical diagnosis, fraud detection, and imbalanced dataset scenarios where accuracy alone is insufficient.
"""

class ModelEvaluator:

    @staticmethod
    def calculate_precision(tp: int, fp: int):

        precision = tp/(tp+fp)

        return precision
    
    @staticmethod
    def calculate_recall(tp: int, fn: int):

        recall = tp/(tp+fn)

        return recall
    
    @staticmethod
    def calculate_f1(precision: int, recall: int):

        f1_score = 2*((precision*recall)/(precision+recall))

        return f1_score
    
    
precision = ModelEvaluator.calculate_precision(tp=80, fp=20)
recall = ModelEvaluator.calculate_recall(tp=80, fn=15)
f1 = ModelEvaluator.calculate_f1(precision, recall)

print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")
    

### Alternative Solution
class ModelEvaluator:
    """Class for calculating ML model evaluation metrics"""
    
    @staticmethod
    def calculate_precision(tp, fp):
        """
        Precision = TP / (TP + FP)
        Measures accuracy of positive predictions
        """
        if tp + fp == 0:
            return 0.0
        return round(tp / (tp + fp), 3)
    
    @staticmethod
    def calculate_recall(tp, fn):
        """
        Recall = TP / (TP + FN)
        Measures ability to find all positive instances
        """
        if tp + fn == 0:
            return 0.0
        return round(tp / (tp + fn), 3)
    
    @staticmethod
    def calculate_f1(precision, recall):
        """
        F1 Score = 2 * (Precision * Recall) / (Precision + Recall)
        Harmonic mean of precision and recall
        """
        if precision + recall == 0:
            return 0.0
        return round(2 * (precision * recall) / (precision + recall), 3)
    
    @classmethod
    def evaluate_model(cls, tp, fp, fn, tn):
        """
        Class method to compute all metrics at once
        Returns comprehensive evaluation dictionary
        """
        precision = cls.calculate_precision(tp, fp)
        recall = cls.calculate_recall(tp, fn)
        f1 = cls.calculate_f1(precision, recall)
        accuracy = (tp + tn) / (tp + fp + fn + tn)
        
        return {
            'precision': precision,
            'recall': recall,
            'f1_score': f1,
            'accuracy': round(accuracy, 3),
            'confusion_matrix': {
                'TP': tp, 'FP': fp,
                'FN': fn, 'TN': tn
            }
        }


# Test
precision = ModelEvaluator.calculate_precision(tp=80, fp=20)
recall = ModelEvaluator.calculate_recall(tp=80, fn=15)
f1 = ModelEvaluator.calculate_f1(precision, recall)

print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")

# Comprehensive evaluation
full_eval = ModelEvaluator.evaluate_model(tp=80, fp=20, fn=15, tn=85)
print("\nFull Evaluation:")
print(full_eval)

# Output:
# Precision: 0.8
# Recall: 0.842
# F1 Score: 0.82
