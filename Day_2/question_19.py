"""
### Q19

**Question:** Implement a `SequenceAligner` class using dynamic programming to perform local alignment (Smith-Waterman) between two sequences with configurable scoring matrix.

**Input:** `aligner = SequenceAligner(match=2, mismatch=-1, gap=-1); aligner.align("ACGT", "AGT")`

**Expected Output:** Alignment score and aligned sequences with gaps

**Usage:** Finding conserved regions in comparative genomics and homology detection.
"""

import numpy as np

class SequenceAligner:
    """Perform local sequence alignment using Smith-Waterman"""
    
    def __init__(self, match=2, mismatch=-1, gap=-1):
        self.match = match
        self.mismatch = mismatch
        self.gap = gap
    
    def align(self, seq1, seq2):
        """Perform local alignment and return score and alignment"""
        m, n = len(seq1), len(seq2)
        
        # Initialize scoring matrix
        H = np.zeros((m + 1, n + 1), dtype=int)
        max_score = 0
        max_pos = (0, 0)
        
        # Fill scoring matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                match_score = H[i-1, j-1] + (
                    self.match if seq1[i-1] == seq2[j-1] else self.mismatch
                )
                delete = H[i-1, j] + self.gap
                insert = H[i, j-1] + self.gap
                H[i, j] = max(0, match_score, delete, insert)
                
                if H[i, j] > max_score:
                    max_score = H[i, j]
                    max_pos = (i, j)
        
        # Traceback to get alignment
        aligned_seq1, aligned_seq2 = self._traceback(H, seq1, seq2, max_pos)
        
        return {
            "score": max_score,
            "aligned_seq1": aligned_seq1,
            "aligned_seq2": aligned_seq2
        }
    
    def _traceback(self, H, seq1, seq2, start_pos):
        """Traceback from maximum score to get alignment"""
        aligned1, aligned2 = [], []
        i, j = start_pos
        
        while i > 0 and j > 0 and H[i, j] > 0:
            score_current = H[i, j]
            score_diag = H[i-1, j-1]
            score_up = H[i-1, j]
            score_left = H[i, j-1]
            
            if score_current == score_diag + (self.match if seq1[i-1] == seq2[j-1] else self.mismatch):
                aligned1.append(seq1[i-1])
                aligned2.append(seq2[j-1])
                i -= 1
                j -= 1
            elif score_current == score_up + self.gap:
                aligned1.append(seq1[i-1])
                aligned2.append('-')
                i -= 1
            else:
                aligned1.append('-')
                aligned2.append(seq2[j-1])
                j -= 1
        
        return ''.join(reversed(aligned1)), ''.join(reversed(aligned2))

# Usage
aligner = SequenceAligner(match=2, mismatch=-1, gap=-1)
result = aligner.align("ACGT", "AGT")
print(result)
