<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Python Practice Questions for AI Engineering, Data Science \& Computational Biology

## Q1-Q4: Simple Python Logic

**Q1 - Protein Sequence Validator**
Question: Write a function that validates if a given string is a valid protein sequence (contains only standard amino acid codes: ACDEFGHIKLMNPQRSTVWY).
Input: `"MKTAYIAKQRQ"`, `"MKTAYIAKQRQZ"`
Expected Output: `True`, `False`
Usage: Input validation for bioinformatics pipelines processing protein data

**Q2 - Log Parser for ML Training**
Question: Write a function that parses training log lines and extracts epoch number, loss value, and accuracy from strings formatted as "Epoch: X, Loss: Y, Accuracy: Z".
Input: `"Epoch: 5, Loss: 0.234, Accuracy: 0.891"`
Expected Output: `{"epoch": 5, "loss": 0.234, "accuracy": 0.891}`
Usage: Monitoring and analyzing machine learning model training progress

**Q3 - API Response Time Categorizer**
Question: Write a function that categorizes API response times into 'fast' (<100ms), 'medium' (100-500ms), 'slow' (500-1000ms), or 'critical' (>1000ms).
Input: `[45][230][780][1200][95]`
Expected Output: `['fast', 'medium', 'slow', 'critical', 'fast']`
Usage: Performance monitoring in FastAPI applications

**Q4 - Gene Expression Threshold Filter**
Question: Write a function that filters gene names where expression values exceed a given threshold.
Input: `{"BRCA1": 450, "TP53": 120, "EGFR": 890}`, threshold=`200`
Expected Output: `["BRCA1", "EGFR"]`
Usage: Identifying significantly expressed genes in RNA-seq analysis

## Q5-Q8: Medium Python Logic with OOPs

**Q5 - Embedding Vector Distance Calculator**
Question: Create a class `VectorMetrics` with methods to calculate Euclidean, Manhattan, and Cosine distances between two embedding vectors.
Input: `vector1=[1.0, 2.0, 3.0]`, `vector2=[4.0, 5.0, 6.0]`
Expected Output: `{"euclidean": 5.196, "manhattan": 9.0, "cosine": 0.025}`
Usage: Similarity calculations in RAG systems and semantic search

**Q6 - Batch Request Processor**
Question: Create a class `BatchProcessor` that groups API requests into batches of size N and tracks processing status (pending/completed/failed).
Input: `requests=[req1, req2, req3, req4, req5]`, `batch_size=2`
Expected Output: `[[req1, req2], [req3, req4], [req5]]` with status tracking
Usage: Optimizing throughput in LLM API calls and rate-limited services

**Q7 - Scientific Unit Converter**
Question: Create a class `BioUnitConverter` that converts between common biological measurement units (ng/ml to mg/L, μM to nM, etc.) with dimensional analysis validation.
Input: `value=500`, `from_unit="ng/ml"`, `to_unit="mg/L"`
Expected Output: `0.5`
Usage: Standardizing measurements across different experimental datasets

**Q8 - Token Counter with Tiktoken**
Question: Create a class `TokenBudgetManager` that tracks token usage across multiple LLM calls and warns when approaching budget limits.
Input: Multiple text inputs with a budget of `10000` tokens
Expected Output: Running count and warning at 80% usage
Usage: Managing costs in production LLM applications

## Q9-Q12: NumPy and Pandas for Data Science

**Q9 - Gene Expression Matrix Normalization**
Question: Given a NumPy array representing gene expression data (genes × samples), normalize each gene using z-score normalization across samples.
Input: `np.array([[100][200][150], [50][75][60], [300][350][320]])`
Expected Output: Normalized array with mean=0 and std=1 for each row
Usage: Preprocessing gene expression data for differential expression analysis

**Q10 - Clinical Trial Data Aggregation**
Question: Using Pandas, aggregate patient data by treatment group and calculate mean, std, and count for multiple biomarkers.
Input: DataFrame with columns `[patient_id, treatment_group, biomarker_A, biomarker_B, age]`
Expected Output: Grouped statistics DataFrame
Usage: Statistical analysis in clinical research and drug efficacy studies

**Q11 - Time Series Feature Engineering**
Question: Create rolling window features (mean, std, min, max) for sensor data with configurable window sizes using Pandas.
Input: DataFrame with timestamp and sensor values, `window_size=5`
Expected Output: DataFrame with original + 4 new rolling feature columns
Usage: Feature engineering for predictive maintenance and IoT analytics

**Q12 - Missing Data Imputation Strategy**
Question: Implement multiple imputation strategies (mean, median, forward-fill, interpolate) for a dataset and compare resulting distributions using NumPy/Pandas.
Input: DataFrame with missing values in multiple columns
Expected Output: Dictionary of imputed DataFrames with strategy names as keys
Usage: Data preprocessing in machine learning pipelines with incomplete datasets

## Q13-Q17: AI and Gen AI Engineering with Async and Pydantic

**Q13 - Async LLM Batch Inference**
Question: Create an async function that processes multiple prompts concurrently using asyncio, with Pydantic models for request/response validation.
Input: List of prompts, max concurrent requests
Expected Output: List of validated LLM responses
Usage: Parallel processing of LLM requests in production AI applications

**Q14 - Async Document Embedding Pipeline**
Question: Build an async pipeline that chunks documents, generates embeddings concurrently, and validates output using Pydantic schemas.
Input: List of document texts, chunk size, embedding model name
Expected Output: List of validated embedding objects with metadata
Usage: Building RAG systems with efficient document processing

**Q15 - Pydantic Model for ML Experiment Tracking**
Question: Create nested Pydantic models for ML experiment configuration (model params, dataset info, training config) with validation rules.
Input: Dictionary with experiment parameters
Expected Output: Validated ExperimentConfig object
Usage: Configuration management in MLOps and experiment tracking systems

**Q16 - Async Multi-Model Inference Router**
Question: Build an async router that sends requests to different LLM providers based on task type, with Pydantic request/response models and retry logic.
Input: Task type, prompt, provider preferences
Expected Output: Validated response from appropriate provider
Usage: Multi-model AI systems with fallback strategies

**Q17 - Streaming Response Handler**
Question: Create an async generator with Pydantic validation that handles streaming LLM responses and yields validated chunks.
Input: Streaming API response
Expected Output: Async generator of validated response chunks
Usage: Real-time streaming applications like chatbots with type safety

## Q18-Q22: Computational Biology Logic with OOPs

**Q18 - Sequence Alignment Scorer**
Question: Create a class `PairwiseAligner` that implements Smith-Waterman local alignment scoring for DNA/protein sequences with configurable scoring matrices.
Input: Two sequences, match score, mismatch penalty, gap penalty
Expected Output: Alignment score and aligned sequences
Usage: Comparing biological sequences for homology detection

**Q19 - Phylogenetic Tree Distance Matrix**
Question: Build a class `PhylogeneticCalculator` that computes pairwise evolutionary distances between species based on sequence differences.
Input: Dictionary of species names and their sequences
Expected Output: Distance matrix as DataFrame
Usage: Constructing phylogenetic trees in evolutionary biology studies

**Q20 - Protein Structure Contact Map**
Question: Create a class `ContactMapGenerator` that identifies residue-residue contacts in a protein structure based on distance thresholds.
Input: List of 3D coordinates for each residue, distance threshold
Expected Output: Binary contact matrix
Usage: Protein structure analysis and fold prediction

**Q21 - Codon Usage Bias Calculator**
Question: Implement a class `CodonAnalyzer` that calculates codon usage frequency and Relative Synonymous Codon Usage (RSCU) for a given DNA sequence.
Input: DNA sequence string
Expected Output: Dictionary of codon frequencies and RSCU values
Usage: Gene expression optimization and synthetic biology applications

**Q22 - Pathway Enrichment Analyzer**
Question: Create a class `PathwayEnrichment` that performs Fisher's exact test to identify over-represented biological pathways in a gene list.
Input: List of target genes, background gene set, pathway annotations
Expected Output: DataFrame with pathway IDs, p-values, and enrichment scores
Usage: Interpreting genomic data and understanding biological mechanisms

## Q23-Q25: FastAPI Backend

**Q23 - ML Model Serving Endpoint**
Question: Create a FastAPI endpoint with Pydantic models that accepts feature vectors, runs inference using a loaded model, and returns predictions with confidence scores.
Input: POST request with feature array
Expected Output: JSON with prediction and confidence
Usage: Deploying machine learning models as REST APIs in production

**Q24 - Async Batch Prediction Service**
Question: Build a FastAPI endpoint that accepts batch prediction requests, processes them asynchronously using background tasks, and provides status/result retrieval endpoints.
Input: POST with batch data, GET for status check
Expected Output: Job ID and batch predictions when complete
Usage: High-throughput prediction services for large-scale data processing

**Q25 - Rate-Limited Embeddings API**
Question: Implement a FastAPI service with rate limiting middleware that generates text embeddings, caches results, and handles concurrent requests with proper error handling.
Input: POST request with text list
Expected Output: Array of embedding vectors with request metadata
Usage: Building embedding services for RAG systems with cost and performance optimization

