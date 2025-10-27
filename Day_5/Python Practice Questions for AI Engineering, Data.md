<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Python Practice Questions for AI Engineering, Data Science \& Computational Biology (Set 5)

## Simple Python Logic Questions (Q1-Q6)

### Q1

**Question:** Write a function to translate a DNA sequence into its corresponding mRNA sequence (replace T with U).

**Input:** `"ATGCAGTTC"`

**Expected Output:** `"AUGCAGUUC"`

**Usage:** Modeling transcription in gene expression studies; generating mRNA templates for in-vitro synthesis; simulating synthetic biology workflows

***

### Q2

**Question:** Create a function that finds the most frequent nucleotide in a given DNA sequence.

**Input:** `"AAGGCTTAA"`

**Expected Output:** `"A"`

**Usage:** Quality checks in sequencing data; analyzing nucleotide frequency bias; primer design for PCR

***

### Q3

**Question:** Write a function to compute the Manhattan distance between two coordinate points in n-dimensional space.

**Input:** `point1=[1][2][3], point2=[4][6][8]`

**Expected Output:** `12`

**Usage:** Clustering in high-dimensional data; comparing patient profiles in multi-omics analyses; analyzing spatial patterns in epidemiology

***

### Q4

**Question:** Create a function to count the number of missing (NaN) values in a dataset list.

**Input:** `[1.2, np.nan, 5.6, np.nan, 3.4, 2.1]`

**Expected Output:** `2`

**Usage:** Data cleaning in biomedical research; handling sensor dropouts; preparing health survey data for machine learning

***

### Q5

**Question:** Write a function to compute the geometric mean of a list of positive numbers.

**Input:** `[1][3][9][27]`

**Expected Output:** `6.0`

**Usage:** Calculating average growth rates; aggregating gene expression fold changes; analyzing cell proliferation data

***

### Q6

**Question:** Create a function to flatten a nested list of arbitrary depth.

**Input:** `[[1, [2, [3][4]], 5]]`

**Expected Output:** `[1][2][3][4][5]`

**Usage:** Normalizing hierarchical biological data; flattening outputs from recursive simulations; preprocessing tree-like data structures

***

## Medium Python Logic Questions (Q7-Q10)

### Q7

**Question:** Write a function to merge two dictionaries where values are lists and concatenate lists if the same key appears in both.

**Input:** `dict1={"A":[1][2], "B":[3]}, dict2={"A":[4], "C":[5][6]}`

**Expected Output:** `{"A": [1][2][4], "B":[3], "C":[5][6]}`

**Usage:** Integrating multi-source patient records; merging gene annotations; aggregating experimental replicates

***

### Q8

**Question:** Implement a function that removes outlier points from a data list using median absolute deviation (MAD) threshold of 3.

**Input:** `[2][3][4][100][5][3]`

**Expected Output:** `[2][3][4][5][3]`

**Usage:** Robust preprocessing in clinical lab measurements; filtering artifacts in brain imaging; outlier removal in financial time series

***

### Q9

**Question:** Write a function to parse a FASTA formatted string and return a dictionary with sequence names as keys and sequences as values.

**Input:** `">seq1\nATGCA\n>seq2\nGGGTT"`

**Expected Output:** `{"seq1": "ATGCA", "seq2": "GGGTT"}`

**Usage:** Handling genomic and proteomic datasets; data ingestion for bioinformatics pipelines; workflow automation in sequence analysis

***

### Q10

**Question:** Create a function that ranks items in a list in descending order and returns a dictionary mapping the item to its rank (starting from 1).

**Input:** `[56][42][85][16]`

**Expected Output:** `{85: 1, 56: 2, 42: 3, 16: 4}`

**Usage:** Scoring models in competitions; ranking biomarkers by predictive value; prioritizing candidate genes in genome-wide studies

