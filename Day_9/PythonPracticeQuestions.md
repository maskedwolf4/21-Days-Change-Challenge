<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>


## Simple Logic Questions (Q1-Q6)

**Q1: Data Preprocessing - Missing Value Counter**
Question: Write a function that takes a list of sensor readings (which may contain None values) and returns a dictionary with count of valid readings and percentage of missing data.

Input: `[23.5, None, 24.1, None, 23.8, 24.0, None, 23.9]`

Expected Output: `{'valid_readings': 5, 'missing_percentage': 37.5}`

Usage: Used in IoT data preprocessing and sensor data quality assessment before feeding into ML models.[^3]

***

**Q2: Feature Normalization Calculator**
Question: Create a function that normalizes a list of numerical features using Min-Max scaling (scale to 0-1 range).

Input: `[^10][^20][^30][^40][^50]`

Expected Output: `[0.0, 0.25, 0.5, 0.75, 1.0]`

Usage: Essential preprocessing step in neural networks and gradient descent-based algorithms to ensure all features contribute equally.[^7]

***

**Q3: Text Tokenizer for NLP**
Question: Write a function that takes a sentence and returns a dictionary with unique words as keys and their frequency counts as values (case-insensitive).

Input: `"Machine learning is great and machine learning is fun"`

Expected Output: `{'machine': 2, 'learning': 2, 'is': 2, 'great': 1, 'and': 1, 'fun': 1}`

Usage: Fundamental step in Natural Language Processing for text vectorization and feature extraction before sentiment analysis or text classification.[^8]

***

**Q4: Batch Data Generator**
Question: Create a function that splits a dataset (list) into batches of specified size. The last batch can be smaller if data doesn't divide evenly.

Input: `data=[^1][^2][^3][^4][^5][^6][^7][^8][^9], batch_size=4`

Expected Output: `[[^1][^2][^3][^4], [^5][^6][^7][^8], [^9]]`

Usage: Critical for training deep learning models with mini-batch gradient descent to manage memory efficiently with large datasets.[^8]

***

**Q5: Outlier Detection using IQR**
Question: Write a function that identifies outliers in a numerical dataset using the Interquartile Range (IQR) method. Return list of outlier values.

Input: `[^10][^12][^12][^13][^12][^11][^14][^13][^15][^10][^10][^100][^12]`

Expected Output: ``

Usage: Used in data cleaning phase before model training to remove anomalies that could skew statistical models and predictions.[^7]

***

**Q6: Train-Test Split Function**
Question: Create a function that randomly splits a dataset into training and testing sets based on a given ratio (e.g., 80-20 split). Use a seed for reproducibility.

Input: `data=[^1][^2][^3][^4][^5][^6][^7][^8][^9][^10], train_ratio=0.8, seed=42`

Expected Output: `{'train': [^1][^3][^4][^6][^7][^8][^9][^10], 'test': [^2][^5]}`

Usage: Fundamental for evaluating machine learning model performance and preventing overfitting by testing on unseen data.[^4]

***

## Medium Logic Questions with OOPs (Q7-Q10)

**Q7: Time Series Data Analyzer Class**
Question: Create a `TimeSeriesAnalyzer` class that stores timestamp-value pairs and provides methods to calculate moving average and detect trend direction (increasing/decreasing/stable).

Input:

```python
data = [(1, 100), (2, 105), (3, 110), (4, 108), (5, 115)]
analyzer = TimeSeriesAnalyzer(data)
analyzer.moving_average(window=3)
analyzer.detect_trend()
```

Expected Output:

```python
moving_average: [105.0, 107.67, 111.0]
trend: 'increasing'
```

Usage: Applied in stock price prediction, weather forecasting, and monitoring system metrics in production ML systems.[^7]

***

**Q8: Neural Network Layer Class**
Question: Design a `DenseLayer` class representing a fully connected neural layer with methods for forward pass (weighted sum + bias) and parameter initialization. Include encapsulation for weights and bias.

Input:

```python
layer = DenseLayer(input_size=3, output_size=2)
layer.initialize_weights(seed=42)
output = layer.forward([1.0, 2.0, 3.0])
```

Expected Output: `[weighted_sum_neuron1, weighted_sum_neuron2]` (actual values depend on initialized weights)

Usage: Building blocks for implementing neural networks from scratch, understanding backpropagation, and customizing deep learning architectures.[^8]

***

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

Usage: Building modular ETL pipelines for multi-modal AI systems that process different data types (images, text, audio).[^3]

***

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

Usage: Essential for evaluating classification models in medical diagnosis, fraud detection, and imbalanced dataset scenarios where accuracy alone is insufficient.[^4][^7]

<div align="center">⁂</div>

[^1]: https://www.datacamp.com/blog/top-python-interview-questions-and-answers

[^2]: https://www.interviewbit.com/python-interview-questions/

[^3]: https://www.geeksforgeeks.org/data-science/data-science-coding-interview-questions/

[^4]: https://in.indeed.com/career-advice/interviewing/python-machine-learning-interview-questions

[^5]: https://www.projectpro.io/article/100-data-science-in-python-interview-questions-and-answers-for-2021/188

[^6]: https://www.geeksforgeeks.org/python/python-exercises-practice-questions-and-solutions/

[^7]: https://codefinity.com/blog/Top-50-Python-Interview-Questions-for-Data-Analyst

[^8]: https://www.dataquest.io/blog/python-skills-you-need-to-work-with-ai/

[^9]: https://www.ccbp.in/blog/articles/python-coding-questions

[^10]: https://www.geeksforgeeks.org/python/python-interview-questions/

[^11]: https://www.simplilearn.com/tutorials/data-science-tutorial/data-science-interview-questions

[^12]: https://www.edureka.co/blog/interview-questions/python-interview-questions

[^13]: https://www.simplilearn.com/python-interview-questions-article

[^14]: https://realpython.com/python-beginner-tips/

