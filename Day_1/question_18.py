"""
**Q18 - Sequence Alignment Scorer**
Question: Create a class `PairwiseAligner` that implements Smith-Waterman local alignment scoring for DNA/protein sequences with configurable scoring matrices.
Input: Two sequences, match score, mismatch penalty, gap penalty
Expected Output: Alignment score and aligned sequences
Usage: Comparing biological sequences for homology detection
"""

import numpy as np

class PairwiseAligner:
    """Implements Smith-Waterman local alignment algorithm"""
    
    def __init__(self, match_score=3, mismatch_penalty=-3, gap_penalty=-2):
        self.match_score = match_score
        self.mismatch_penalty = mismatch_penalty
        self.gap_penalty = gap_penalty
    
    def create_scoring_matrix(self, seq1, seq2):
        """Creates scoring matrix using dynamic programming"""
        rows = len(seq1) + 1
        cols = len(seq2) + 1
        
        # Initialize matrix with zeros
        H = np.zeros((rows, cols), dtype=int)
        
        # Fill matrix
        max_score = 0
        max_pos = (0, 0)
        
        for i in range(1, rows):
            for j in range(1, cols):
                # Calculate scores for match/mismatch, deletion, insertion
                match = H[i-1, j-1] + (self.match_score if seq1[i-1] == seq2[j-1] 
                                       else self.mismatch_penalty)
                delete = H[i-1, j] + self.gap_penalty
                insert = H[i, j-1] + self.gap_penalty
                
                # Take maximum (including 0 for local alignment)
                H[i, j] = max(0, match, delete, insert)
                
                # Track maximum score position
                if H[i, j] > max_score:
                    max_score = H[i, j]
                    max_pos = (i, j)
        
        return H, max_score, max_pos
    
    def traceback(self, H, seq1, seq2, max_pos):
        """Performs traceback to get aligned sequences"""
        aligned_seq1 = []
        aligned_seq2 = []
        
        i, j = max_pos
        
        while i > 0 and j > 0 and H[i, j] > 0:
            current_score = H[i, j]
            diagonal = H[i-1, j-1]
            up = H[i-1, j]
            left = H[i, j-1]
            
            if current_score == diagonal + (self.match_score if seq1[i-1] == seq2[j-1] 
                                           else self.mismatch_penalty):
                aligned_seq1.append(seq1[i-1])
                aligned_seq2.append(seq2[j-1])
                i -= 1
                j -= 1
            elif current_score == up + self.gap_penalty:
                aligned_seq1.append(seq1[i-1])
                aligned_seq2.append('-')
                i -= 1
            else:
                aligned_seq1.append('-')
                aligned_seq2.append(seq2[j-1])
                j -= 1
        
        return ''.join(reversed(aligned_seq1)), ''.join(reversed(aligned_seq2))
    
    def align(self, seq1, seq2):
        """Performs complete alignment and returns score and aligned sequences"""
        H, max_score, max_pos = self.create_scoring_matrix(seq1, seq2)
        aligned_1, aligned_2 = self.traceback(H, seq1, seq2, max_pos)
        
        return {
            'score': max_score,
            'aligned_seq1': aligned_1,
            'aligned_seq2': aligned_2,
            'identity': sum(a == b for a, b in zip(aligned_1, aligned_2)) / len(aligned_1) * 100
        }

# Test
aligner = PairwiseAligner(match_score=3, mismatch_penalty=-3, gap_penalty=-2)
seq1 = "TGTTACGG"
seq2 = "GGTTGACTA"

result = aligner.align(seq1, seq2)
print(f"Alignment Score: {result['score']}")
print(f"Sequence 1: {result['aligned_seq1']}")
print(f"Sequence 2: {result['aligned_seq2']}")
print(f"Identity: {result['identity']:.1f}%")
