<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Python Practice Questions for AI Engineering, Data Science \& Computational Biology (Set 6)

## Simple Python Logic Questions (Q1-Q6)

### Q1

**Question:** Write a function to count the number of codons (triplets) in a given DNA sequence, ignoring any trailing bases that do not form a complete codon.

**Input:** `"ATGCGTAACTAG"`

**Expected Output:** `4`

**Usage:** Parsing coding regions for translation; identifying possible open reading frames; analyzing frameshift mutations

***

### Q2

**Question:** Create a function that returns the indices of all local maxima in a numeric list.

**Input:** `[^1][^3][^7][^1][^2][^6][^0][^1]`

**Expected Output:** `[^2][^5]`

**Usage:** Detecting peaks in sensor signals; finding gene expression spikes; identifying events in physiological time series

***

### Q3

**Question:** Write a function to perform element-wise multiplication of two lists of equal length.

**Input:** `[^2][^4][^6]`, `[^1][^3][^5]`

**Expected Output:** `[^2][^12][^30]`

**Usage:** Combining arrays of coefficients and features; simulating signal processing pipelines; calculating weighted scores in ensemble models

***

### Q4

**Question:** Create a function to return the cumulative sum list of a given numeric list.

**Input:** `[^4][^2][^5][^3]`

**Expected Output:** `[^4][^6][^11][^14]`

**Usage:** Generating running totals in time-series; measuring cumulative population or resource growth; financial data analysis

***

### Q5

**Question:** Write a function to check if a DNA sequence is palindromic (its reverse complement is identical to the original).

**Input:** `"GTATAC"`

**Expected Output:** `True`

**Usage:** Detecting restriction enzyme recognition sites; studying regulatory motifs; identifying palindromic repeats in genomes

***

### Q6

**Question:** Create a function that returns a dictionary with counts of each unique element in a list.

**Input:** `['apple', 'orange', 'apple', 'banana']`

**Expected Output:** `{'apple': 2, 'orange': 1, 'banana': 1}`

**Usage:** Summarizing categorical survey results; counting different mutation types in a sequence; analyzing species distribution

***

## Medium Python Logic Questions (Q7-Q10)

### Q7

**Question:** Write a function to compute the Dice coefficient (similarity) between two sets.

**Input:** `set1={"gene1","gene2","gene3"}, set2={"gene2","gene4","gene5"}`

**Expected Output:** `0.333`

**Usage:** Comparing sample overlaps in cohort selection; quantifying annotation similarity; feature selection in omics data

***

### Q8

**Question:** Implement a function that returns the longest common prefix among a list of DNA sequences.

**Input:** `["ATGCC", "ATGCACT", "ATGCTT"]`

**Expected Output:** `"ATGC"`

**Usage:** Multiple sequence alignment pre-processing; identifying conserved regulatory motifs; designing common PCR primers

***

### Q9

**Question:** Create a function to bucketize a numeric list by placing each value into bins defined by edges.

**Input:** `values=[1.2, 2.4, 3.6, 4.8], bins=[^0][^2][^4][^6]`

**Expected Output:** `[^0][^1][^2][^2]`
*(values go into bin 0: [0,2), bin 1: [2,4), bin 2: )*

**Usage:** Discretizing clinical data for risk categories; pre-processing features for decision trees; histogram-based visualizations

***

### Q10

**Question:** Write a function to compute the Hurst exponent for a given time series list using the rescaled range (R/S) method (use 2-segment calculation for simplicity).

**Input:** `[0.5, 1.0, 0.6, 0.8, 1.2, 1.4]`

**Expected Output:** A float around `0.6` (actual value depends on calculation details)

**Usage:** Identifying long-term memory or trend strength in biosignals; financial analytics; analyzing persistence in biological rhythms

<div align="center">⁂</div>

[^1]: projects.python_web

[^2]: programming.python_libraries

