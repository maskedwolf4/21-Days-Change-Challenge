<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Python Practice Questions for AI Engineering, Data Science \& Computational Biology (Set 7)

## Simple Python Logic Questions (Q1-Q6)

### Q1

**Question:** Write a function to find the mode (most frequent value) in a numeric list. If there are multiple modes, return the first one encountered.

**Input:** `[3][7][3][5][3][9][1]`

**Expected Output:** `3`

**Usage:** Identifying predominant cell types in tissue samples; finding most common mutation variants; summarizing survey responses in clinical studies

***

### Q2

**Question:** Create a function that checks if a given number is prime. Return True if prime, False otherwise.

**Input:** `17`

**Expected Output:** `True`

**Usage:** Number theory applications in cryptography for secure bioinformatics databases; generating unique IDs; algorithmic efficiency testing

***

### Q3

**Question:** Write a function to rotate a list left by k positions (move first k elements to the end).

**Input:** `lst=[1][2][3][4][5][6]`, `k=2`

**Expected Output:** `[3][4][5][6][1][2]`

**Usage:** Circular buffer management for streaming sensor data; cyclic shift operations in signal processing; DNA circular genome analysis

***

### Q4

**Question:** Create a function to generate a list of Fibonacci numbers up to a given limit (inclusive).

**Input:** `limit=20`

**Expected Output:** `[0][1][1][2][3][5][8][13]`

**Usage:** Modeling exponential growth in populations; phyllotaxis patterns in plant biology; recursive algorithms in computational biology

***

### Q5

**Question:** Write a function to convert a list of degrees to radians using the formula: radians = degrees × (π/180).

**Input:** `[0][90][180][270]`

**Expected Output:** `[0.0, 1.57, 3.14, 4.71]` (rounded to 2 decimals)

**Usage:** Converting angles for trigonometric functions in bioinformatics; spatial analysis of molecular structures; signal processing in medical imaging

***

### Q6

**Question:** Create a function that returns the intersection of two dictionaries based on keys (returns a new dict with common keys and their values).

**Input:** `d1={'A':1, 'B':2, 'C':3}`, `d2={'B':4, 'C':5, 'D':6}`

**Expected Output:** `{'B': 2, 'C': 3}`

**Usage:** Merging overlapping gene annotations; finding common clinical variables between datasets; synchronizing shared model parameters

***

## Medium Python Logic Questions (Q7-Q10)

### Q7

**Question:** Implement a function to find the median of a list of numbers (handle both odd and even length lists correctly).

**Input:** `[7][3][1][4][6]`

**Expected Output:** `4`

**Usage:** Robust central tendency measure in biomedical statistics; outlier-resistant analysis of lab measurements; non-parametric data analysis

***

### Q8

**Question:** Write a function to compute the weighted average of a list of numbers with corresponding weights.

**Input:** `values=[10][20][30][40]`, `weights=[0.1, 0.2, 0.3, 0.4]`

**Expected Output:** `25.0`

**Usage:** Calculating weighted gene expression scores; importance-based feature aggregation; risk-adjusted clinical scoring systems

***

### Q9

**Question:** Create a function that performs string matching using the Knuth-Morris-Pratt (KMP) algorithm to find all occurrences of a pattern in text.

**Input:** `text="ABABDABACDABABCABAB"`, `pattern="ABABCABAB"`

**Expected Output:** `[14]`

**Usage:** Pattern matching in genomic sequences; finding regulatory motifs; text mining in biomedical literature

***

### Q10

**Question:** Write a function to implement the Tower of Hanoi problem solver, returning the list of moves as (from_peg, to_peg) tuples.

**Input:** `n_disks=3`

**Expected Output:** `[(1,3), (1,2), (3,2), (1,3), (2,1), (2,3)]`

**Usage:** Recursive algorithm understanding for bioinformatics tree traversals; state space exploration in molecular dynamics; puzzle-solving AI development

