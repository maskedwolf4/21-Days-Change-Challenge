<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Python Practice Questions for AI Engineering, Data Science \& Computational Biology (Set 4)

## Simple Python Logic Questions (Q1-Q6)

### Q1

**Question:** Write a function to calculate the melting temperature (Tm) of a DNA primer using the basic formula: Tm = 4(G+C) + 2(A+T).

**Input:** `"ATGCGCTA"`

**Expected Output:** `24`

**Usage:** Designing PCR primers, optimizing annealing temperatures in molecular cloning, planning CRISPR guide RNAs

### Q2

**Question:** Create a function that performs standard scaling (z-score standardization) on features by subtracting mean and dividing by standard deviation.

**Input:** `[^10][^12][^23][^23][^16][^23][^21][^16]`

**Expected Output:** `[-1.5, -1.125, 0.75, 0.75, -0.375, 0.75, 0.375, -0.375]`

**Usage:** Preprocessing features for support vector machines, standardizing metabolomics data, preparing inputs for gradient-based optimization

### Q3

**Question:** Write a function to calculate Pearson correlation coefficient between two numerical arrays.

**Input:** `x=[^1][^2][^3][^4][^5], y=[^2][^4][^5][^4][^5]`

**Expected Output:** `0.832`

**Usage:** Finding correlated genes in co-expression networks, feature selection in predictive modeling, identifying relationships between clinical variables

### Q4

**Question:** Create a function that performs random undersampling on the majority class to balance a binary classification dataset.

**Input:** `data=[(1,"A"), (1,"B"), (1,"C"), (1,"D"), (0,"E"), (0,"F")], seed=42`

**Expected Output:** `[(1,"A"), (1,"C"), (0,"E"), (0,"F")]` (balanced 2:2 ratio)

**Usage:** Handling class imbalance in fraud detection, balancing disease vs healthy samples, improving rare event prediction

### Q5

**Question:** Write a function to calculate the interquartile range (IQR) which is the difference between the 75th and 25th percentiles.

**Input:** `[^1][^3][^5][^7][^9][^11][^13][^15][^17][^19]`

**Expected Output:** `10.0`

**Usage:** Detecting outliers in laboratory measurements, assessing data spread in clinical trials, robust statistical analysis

### Q6

**Question:** Create a function that performs label encoding by mapping categorical text labels to integer indices starting from 0.

**Input:** `["dog", "cat", "dog", "bird", "cat", "bird"]`

**Expected Output:** `[^1][^2][^1][^0][^2][^0]` with mapping `{"bird": 0, "cat": 2, "dog": 1}`

**Usage:** Encoding categorical variables for tree-based models, converting diagnosis codes to numerical format, preparing ordinal data

## Medium Python Logic Questions (Q7-Q10)

### Q7

**Question:** Implement the silhouette coefficient calculation for evaluating clustering quality by measuring how similar an object is to its own cluster compared to other clusters.

**Input:** `data=[[^1][^2], [^2][^3], [^8][^8], [^9][^10]], cluster_labels=[^0][^0][^1]`

**Expected Output:** `0.85` (approximate average silhouette score)

**Usage:** Determining optimal number of clusters in patient segmentation, validating clustering of cell types, evaluating unsupervised learning results

### Q8

**Question:** Write a function to calculate the log-loss (binary cross-entropy) for binary classification predictions.

**Input:** `y_true=[^1][^0][^1][^1][^0], y_pred=[0.9, 0.1, 0.8, 0.7, 0.2]`

**Expected Output:** `0.168`

**Usage:** Training neural networks for image classification, evaluating probabilistic predictions in risk assessment, optimizing logistic regression models

### Q9

**Question:** Implement the Metropolis-Hastings MCMC algorithm for sampling from a target distribution (use normal distribution as proposal).

**Input:** `target_mean=5, target_std=2, n_samples=1000, initial_value=0, proposal_std=1`

**Expected Output:** `[sample_array]` with mean ≈ 5 and std ≈ 2

**Usage:** Bayesian inference in computational biology, parameter estimation in epidemiological models, sampling from posterior distributions

### Q10

**Question:** Create a function to calculate feature importance using permutation importance by measuring the decrease in model score when a feature is randomly shuffled.

**Input:** `X=[[^1][^2], [^3][^4], [^5][^6], [^7][^8]], y=[^0][^0][^1][^1], model_predictions=[^0][^0][^1][^1], n_repeats=10`

**Expected Output:** `{"feature_0": 0.5, "feature_1": 0.5}` (importance scores)

**Usage:** Identifying key biomarkers in disease prediction, understanding model decisions for regulatory compliance, feature selection in genomics

<div align="center">⁂</div>

[^1]: learning.python_ai_datascience

