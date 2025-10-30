<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Python Practice Questions for AI Engineering, Data Science \& Computational Biology (Set 8)

## Simple Python Logic Questions (Q1-Q6)

### Q1

**Question:** Write a function to calculate the standard error of the mean (SEM) for a list of numbers using the formula: SEM = std / √n.

**Input:** `[^12][^15][^14][^10][^13][^11]`

**Expected Output:** `0.764`

**Usage:** Estimating uncertainty in sample means for clinical trials; calculating error bars for gene expression plots; statistical inference in experimental biology

***

### Q2

**Question:** Create a function to find the second largest element in a list without using sorting.

**Input:** `[^10][^20][^4][^45][^99][^99][^45]`

**Expected Output:** `45`

**Usage:** Finding runner-up biomarker scores; identifying secondary peaks in chromatography; rank-based feature selection in machine learning

***

### Q3

**Question:** Write a function to encode a DNA sequence using run-length encoding (compress consecutive identical bases).

**Input:** `"AAAAGGGCCCTTTT"`

**Expected Output:** `"A4G3C3T4"`

**Usage:** Compressing repetitive genomic sequences; reducing storage for homopolymer regions; efficient representation of microsatellites

***

### Q4

**Question:** Create a function to calculate the variance of a list of numbers using the formula: variance = Σ(x - mean)² / n.

**Input:** `[^2][^4][^4][^4][^5][^5][^7][^9]`

**Expected Output:** `4.0`

**Usage:** Measuring spread in phenotypic measurements; assessing variability in sensor readings; quality control in laboratory assays

***

### Q5

**Question:** Write a function to split a string into chunks of specified length, padding the last chunk if necessary.

**Input:** `text="ATGCGTA", chunk_size=3, padding="N"`

**Expected Output:** `["ATG", "CGT", "ANN"]`

**Usage:** Partitioning sequences for parallel processing; creating k-mer windows for analysis; batch processing in sequence alignment pipelines

***

### Q6

**Question:** Create a function that removes duplicate elements from a list while preserving the original order.

**Input:** `[^3][^5][^3][^2][^5][^7][^2][^9]`

**Expected Output:** `[^3][^5][^2][^7][^9]`

**Usage:** Deduplicating patient IDs in merged datasets; removing redundant features in ML pipelines; cleaning repeated entries in biological databases

***

## Medium Python Logic Questions (Q7-Q10)

### Q7

**Question:** Implement a function to calculate the Spearman rank correlation coefficient between two numeric lists (convert to ranks first, then calculate Pearson on ranks).

**Input:** `x=[^1][^2][^3][^4][^5]`, `y=[^5][^6][^7][^8][^7]`

**Expected Output:** `0.82`

**Usage:** Non-parametric correlation for ordinal clinical data; robust correlation for non-linear relationships; analyzing ranked gene expression patterns

***

### Q8

**Question:** Write a function to perform stratified k-fold split indices for a dataset given labels (return list of k train-test index tuples).

**Input:** `labels=[^0][^0][^0][^0][^1][^1][^1][^1], k=2`

**Expected Output:** `[([^0][^1][^4][^5], [^2][^3][^6][^7]), ([^2][^3][^6][^7], [^0])]` (approximate, maintaining class balance)

**Usage:** Cross-validation for imbalanced disease datasets; fair evaluation of diagnostic classifiers; training robust predictive models

***

### Q9

**Question:** Create a function to calculate information gain for a binary classification split given parent and child class distributions.

**Input:** `parent=[^30][^20]`, `left_child=[^20][^5]`, `right_child=[^10][^15]`

**Expected Output:** `0.123`

**Usage:** Feature selection in decision trees; identifying optimal split points for diagnosis; entropy-based data partitioning

***

### Q10

**Question:** Implement a function to generate synthetic time series data using an autoregressive AR(1) model: x_t = φ * x_(t-1) + noise.

**Input:** `n_points=10, phi=0.7, initial_value=1.0, noise_std=0.1, seed=42`

**Expected Output:** `[1.0, 0.75, 0.61, 0.48, ...]` (10 values)

**Usage:** Simulating patient vital signs trajectories; generating synthetic biomarker data for testing algorithms; modeling temporal dependencies in biological processes

<div align="center">⁂</div>

[^1]: preferences.question_format

[^2]: programming.python_libraries

[^3]: projects.ai_requirements

