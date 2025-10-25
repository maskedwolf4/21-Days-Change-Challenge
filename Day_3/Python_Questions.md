# Python Practice Questions for AI Engineering, Data Science & Computational Biology (Set 3)

## Simple Python Logic Questions (Q1-Q6)

### Q1
**Question:** Write a function to reverse complement a DNA sequence (reverse the string and swap A↔T, G↔C).

**Input:** `"ATGCGA"`

**Expected Output:** `"TCGCAT"`

**Usage:** Analyzing reverse strand in genome assembly, primer design for PCR, processing paired-end sequencing reads


### Q2
**Question:** Create a function that performs log transformation (natural log) on expression data, adding a pseudocount to handle zeros.

**Input:** `values=[0][1][10][100][1000], pseudocount=1`

**Expected Output:** `[0.0, 0.693, 2.398, 4.615, 6.908]`

**Usage:** Stabilizing variance in RNA-seq analysis, normalizing skewed distributions in proteomics, preprocessing data for linear models


### Q3
**Question:** Write a function to calculate the Euclidean distance between two points in n-dimensional space.

**Input:** `point1=[1][2][3], point2=[4][6][8]`

**Expected Output:** `7.071`

**Usage:** Measuring similarity in feature space, k-nearest neighbors classification, clustering algorithms in patient stratification


### Q4
**Question:** Create a function that generates bootstrapped samples (random sampling with replacement) from a dataset.

**Input:** `data=[10][20][30][40], n_samples=4, seed=42`

**Expected Output:** `[30][10][30][20]` (example with replacement)

**Usage:** Estimating confidence intervals in clinical studies, random forest algorithms, assessing model stability


### Q5
**Question:** Write a function to calculate the coefficient of variation (CV) which is standard deviation divided by mean, expressed as percentage.

**Input:** `[2.1, 2.3, 2.2, 2.4, 2.0]`

**Expected Output:** `6.93`

**Usage:** Quality control in qPCR experiments, comparing variability across different scales, assessing technical reproducibility


### Q6
**Question:** Create a function that converts a sequence to k-mer frequency dictionary (subsequences of length k).

**Input:** `sequence="ATGCATG", k=3`

**Expected Output:** `{"ATG": 2, "TGC": 1, "GCA": 1, "CAT": 1}`

**Usage:** Feature extraction for genome classification, identifying DNA motifs, training language models on biological sequences


## Medium Python Logic Questions (Q7-Q10)

### Q7
**Question:** Implement the Levenshtein distance (edit distance) calculation between two strings using dynamic programming to find minimum insertions, deletions, and substitutions.

**Input:** `string1="KITTEN", string2="SITTING"`

**Expected Output:** `3`

**Usage:** Spell checking in biomedical literature mining, measuring mutation distance between sequences, fuzzy matching in database searches


### Q8
**Question:** Write a function to calculate the Area Under the ROC Curve (AUC-ROC) using the trapezoidal rule given true labels and prediction scores.

**Input:** `y_true=[0][0][1][1][1], y_scores=[0.1, 0.4, 0.35, 0.8, 0.9]`

**Expected Output:** `0.833`

**Usage:** Evaluating binary classifiers in disease diagnosis, comparing drug efficacy models, assessing biomarker performance


### Q9
**Question:** Implement the Viterbi algorithm for finding the most likely sequence of hidden states in a Hidden Markov Model given observations.

**Input:** `observations=[0][1][2], states=[0][1], start_prob=[0.6,0.4], trans_prob=[[0.7,0.3],[0.4,0.6]], emit_prob=[[0.5,0.4,0.1],[0.1,0.3,0.6]]`

**Expected Output:** `[0][0][1]` (most likely state sequence)

**Usage:** Gene prediction in genomic sequences, protein secondary structure prediction, speech recognition in voice-controlled medical devices


### Q10
**Question:** Create a function to perform batch normalization on a feature matrix (normalize each feature across samples to zero mean and unit variance).

**Input:** `data=[[1][2], [2][4], [3][6], [4][8]], epsilon=1e-5`

**Expected Output:** `[[-1.342, -1.342], [-0.447, -0.447], [0.447, 0.447], [1.342, 1.342]]`

**Usage:** Preprocessing layers in deep neural networks, stabilizing training in drug discovery models, normalizing multi-omics data integration