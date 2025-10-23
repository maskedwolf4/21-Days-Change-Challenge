"""
**Q5 - Embedding Vector Distance Calculator**
Question: Create a class `VectorMetrics` with methods to calculate Euclidean, Manhattan, and Cosine distances between two embedding vectors.
Input: `vector1=[1.0, 2.0, 3.0]`, `vector2=[4.0, 5.0, 6.0]`
Expected Output: `{"euclidean": 5.196, "manhattan": 9.0, "cosine": 0.025}`
Usage: Similarity calculations in RAG systems and semantic search
"""

import numpy as np

class VectorMetrics:

    def __init__(self, vector1, vector2):
        self.vector1 = vector1
        self.vector2 = vector2

    def euclideain_distance(self,v1,v2):
        v1 = np.array(self.vector1)
        v2 = np.array(self.vector2)
        np.array(v1)
        np.array(v2)

        ed = np.linalg.norm(v1-v2)
        ed = ed.item()
        return ed


    
    def manhattan_distance(self,v1,v2):
        v1 = np.array(self.vector1)
        v2 = np.array(self.vector2)

        
        md  = np.sum(np.abs(v1-v2))
        md = md.item()
        return md
    
    def cosine_distance(self,v1,v2):
        v1 = np.array(self.vector1) 
        v2 = np.array(self.vector1)

        dot_product = np.dot(v1, v2)
        magnitude_v1 = np.linalg.norm(v1)
        magnitude_v2 = np.linalg.norm(v2)

        cosine_distance = 1 - (dot_product / (magnitude_v1 * magnitude_v2))

        cd = cosine_distance.item()
        return cd
    
    def show(self):
        ed = self.euclideain_distance(self.vector1,self.vector2)
        md = self.euclideain_distance(self.vector1,self.vector2)
        cd = self.cosine_distance(self.vector1,self.vector2)

        return {"Euclideain" : ed, "Manhattan" : md, "Cosine" : cd}
    
vm = VectorMetrics(vector1=[1.0, 2.0, 3.0], vector2=[4.0, 5.0, 6.0])
print(vm.show())

