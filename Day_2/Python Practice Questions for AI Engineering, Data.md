<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Python Practice Questions for AI Engineering, Data Science \& Computational Biology

## Q1-Q4: Simple Python Logic

### Q1

**Question:** Write a function to calculate the GC content percentage of a DNA sequence (ratio of G and C nucleotides to total length).

**Input:** `"ATGCGCTA"`

**Expected Output:** `50.0`

**Usage:** Basic quality metric in genomics for assessing DNA sequences before analysis.

***

### Q2

**Question:** Create a function that converts temperature readings from Celsius to Kelvin and Fahrenheit, returning a dictionary with all three scales.

**Input:** `25.0`

**Expected Output:** `{"celsius": 25.0, "kelvin": 298.15, "fahrenheit": 77.0}`

**Usage:** Environmental data normalization in climate modeling and experimental data preprocessing.

***

### Q3

**Question:** Write a function to calculate the Hamming distance between two equal-length strings (number of positions at which corresponding characters differ).

**Input:** `"AGCT", "AACT"`

**Expected Output:** `1`

**Usage:** Measuring sequence similarity in bioinformatics and error detection in data transmission.

***

### Q4

**Question:** Create a function that parses a FASTA header line and extracts the sequence ID and description as separate values.

**Input:** `">sp|P12345|PROTEIN_HUMAN Heat shock protein"`

**Expected Output:** `{"id": "sp|P12345|PROTEIN_HUMAN", "description": "Heat shock protein"}`

**Usage:** Preprocessing biological sequence data files for downstream analysis pipelines.

***

## Q5-Q8: Medium Python Logic (with OOPs)

### Q5

**Question:** Create a `SequenceValidator` class that validates DNA, RNA, and protein sequences. Include methods to check sequence type and validate characters.

**Input:** `validator = SequenceValidator("ATGCN"); validator.validate()`

**Expected Output:** `{"valid": True, "type": "DNA", "ambiguous_bases": 1}`

**Usage:** Input validation in sequencing pipelines before storing data in databases.

***

### Q6

**Question:** Build a `VectorSpace` class that performs dot product, magnitude calculation, and cosine similarity between two vectors.

**Input:** `v1 = VectorSpace([1][2][3]); v2 = VectorSpace([4][5][6]); v1.cosine_similarity(v2)`

**Expected Output:** `0.9746318461970762`

**Usage:** Embedding similarity calculations in RAG systems and recommendation engines.

***

### Q7

**Question:** Design a `RateLimiter` class that tracks API calls per user and enforces rate limits (e.g., max 100 calls per minute).

**Input:** `limiter = RateLimiter(max_calls=3, window=60); [limiter.allow_request("user1") for _ in range(4)]`

**Expected Output:** `[True, True, True, False]`

**Usage:** Protecting backend APIs from abuse and ensuring fair resource allocation.

***

### Q8

**Question:** Create a `CircularBuffer` class with fixed size that overwrites oldest data when full, with methods to add, retrieve, and check if full.

**Input:** `buffer = CircularBuffer(3); buffer.add(1); buffer.add(2); buffer.add(3); buffer.add(4); buffer.get_all()`

**Expected Output:** `[2][3][4]`

**Usage:** Real-time streaming data processing in IoT sensors and time-series analysis.

***

## Q9-Q12: NumPy and Pandas for Data Science

### Q9

**Question:** Given a pandas DataFrame of gene expression data with samples as rows and genes as columns, normalize each gene (column) using z-score normalization.

**Input:** DataFrame with shape (100, 50) containing raw expression values

**Expected Output:** DataFrame with same shape where each column has mean=0 and std=1

**Usage:** Preprocessing gene expression matrices before clustering or differential expression analysis.

***

### Q10

**Question:** Write a function using NumPy to calculate the pairwise Euclidean distance matrix between all rows of a 2D array efficiently without loops.

**Input:** `np.array([[1][2], [3][4], [5][6]])`

**Expected Output:** 3x3 symmetric matrix with distances between each pair of points

**Usage:** K-means clustering initialization and nearest neighbor searches in ML pipelines.

***

### Q11

**Question:** Create a function that reads a CSV of clinical trial data, handles missing values using median imputation for numeric columns and mode for categorical, then returns cleaned DataFrame.

**Input:** CSV file path with mixed data types and missing values

**Expected Output:** Cleaned DataFrame with no missing values

**Usage:** Data preprocessing in healthcare analytics and clinical research studies.

***

### Q12

**Question:** Build a function that takes a pandas DataFrame of time-series stock prices and calculates rolling mean, standard deviation, and Bollinger Bands (mean ± 2*std) for a given window.

**Input:** DataFrame with 'date' and 'price' columns, window=20

**Expected Output:** DataFrame with additional columns for rolling_mean, rolling_std, upper_band, lower_band

**Usage:** Technical analysis in quantitative finance and trading algorithm development.

***

## Q13-Q17: AI \& Gen AI Engineering (Async + Pydantic)

### Q13

**Question:** Create a Pydantic model `EmbeddingRequest` with fields for text (list of strings), model_name, and dimension, with validators ensuring text list is not empty and dimension is positive.

**Input:** `{"text": ["hello world"], "model_name": "voyage-2", "dimension": 1024}`

**Expected Output:** Validated EmbeddingRequest object or ValidationError

**Usage:** Request validation in vector embedding microservices for RAG applications.

***

### Q14

**Question:** Write an async function that concurrently fetches embeddings for multiple text chunks from an API, with retry logic and timeout handling.

**Input:** List of 100 text chunks, API endpoint URL

**Expected Output:** List of 100 embedding vectors in same order

**Usage:** Batch processing documents for vector database ingestion in production RAG systems.

***

### Q15

**Question:** Design a Pydantic model `ChatMessage` with role validation (only "user", "assistant", "system" allowed), content string, and optional metadata dict with timestamp.

**Input:** `{"role": "user", "content": "Explain proteins", "metadata": {"user_id": "123"}}`

**Expected Output:** Validated ChatMessage object

**Usage:** Message validation in LLM chat applications and conversation history storage.

***

### Q16

**Question:** Create an async function that processes a queue of text generation requests with rate limiting (max 5 concurrent requests) and aggregates results.

**Input:** Queue of 50 prompts, LLM API client

**Expected Output:** List of 50 generated responses with metadata (time taken, tokens used)

**Usage:** Batch inference in production LLM applications with cost and latency optimization.

***

### Q17

**Question:** Build a Pydantic model `AgentResponse` with fields for tool_calls (list of dicts), final_answer (string), reasoning_steps (list), and confidence_score (0-1 float with validator).

**Input:** `{"tool_calls": [{"name": "search", "args": {...}}], "final_answer": "The answer is...", "reasoning_steps": ["step1", "step2"], "confidence_score": 0.85}`

**Expected Output:** Validated AgentResponse object

**Usage:** Structured output parsing from LLM agents in agentic AI workflows.

***

## Q18-Q22: Computational Biology

### Q18

**Question:** Create a `Protein` class that stores amino acid sequence and calculates molecular weight, isoelectric point, and hydrophobicity using Kyte-Doolittle scale.

**Input:** `protein = Protein("MKTAYIAKQR"); protein.calculate_properties()`

**Expected Output:** `{"molecular_weight": 1149.36, "pI": 9.75, "hydrophobicity": -0.32}`

**Usage:** Protein characterization in drug discovery and structural biology research.

***

### Q19

**Question:** Implement a `SequenceAligner` class using dynamic programming to perform local alignment (Smith-Waterman) between two sequences with configurable scoring matrix.

**Input:** `aligner = SequenceAligner(match=2, mismatch=-1, gap=-1); aligner.align("ACGT", "AGT")`

**Expected Output:** Alignment score and aligned sequences with gaps

**Usage:** Finding conserved regions in comparative genomics and homology detection.

***

### Q20

**Question:** Build a `PhylogeneticTree` class that constructs a UPGMA tree from a distance matrix and outputs the tree in Newick format.

**Input:** Distance matrix as nested list/array

**Expected Output:** Newick format string representing the hierarchical tree

**Usage:** Evolutionary analysis and species relationship visualization in phylogenetics.

***

### Q21

**Question:** Create a `ProteinStructure` class that parses PDB file format, extracts alpha carbon coordinates, and calculates inter-residue distances and contact maps.

**Input:** PDB file content as string

**Expected Output:** Contact map as 2D numpy array where 1 indicates residues within 8Å

**Usage:** Protein structure analysis and machine learning feature extraction for structure prediction.

***

### Q22

**Question:** Design a `GeneExpressionAnalyzer` class that performs differential expression analysis using t-tests between two conditions, corrects for multiple testing (Benjamini-Hochberg), and returns significant genes.

**Input:** Expression matrix (genes × samples), condition labels, significance threshold

**Expected Output:** DataFrame with genes, fold-change, p-values, adjusted p-values, significance flag

**Usage:** Identifying biomarkers in cancer research and understanding disease mechanisms.

***

## Q23-Q25: FastAPI Backend

### Q23

**Question:** Create a FastAPI endpoint that accepts protein sequences via POST, validates them using Pydantic, performs async batch embedding generation, stores embeddings in a dictionary cache, and returns embedding vectors.

**Input:** `POST /embed {"sequences": ["MKTAY", "ACDEF"]}`

**Expected Output:** `{"embeddings": [[...], [...]], "cached": [false, false], "processing_time": 0.45}`

**Usage:** Protein embedding microservice for ML-based protein function prediction pipelines.

***

### Q24

**Question:** Build a FastAPI application with dependency injection for database connection pooling, implementing CRUD endpoints for managing experiment metadata with async database operations.

**Input:** `GET /experiments/{experiment_id}`

**Expected Output:** JSON response with experiment details or 404 if not found

**Usage:** Laboratory information management systems (LIMS) and research data management platforms.

***

### Q25

**Question:** Implement a FastAPI endpoint with WebSocket support that streams real-time analysis results as they're computed, with proper error handling and connection management.

**Input:** WebSocket connection with initial parameters

**Expected Output:** Streaming JSON messages with incremental results and progress updates

**Usage:** Real-time bioinformatics pipeline monitoring and interactive data analysis dashboards.

