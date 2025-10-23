"""
**Q4 - Gene Expression Threshold Filter**
Question: Write a function that filters gene names where expression values exceed a given threshold.
Input: `{"BRCA1": 450, "TP53": 120, "EGFR": 890}`, threshold=`200`
Expected Output: `["BRCA1", "EGFR"]`
Usage: Identifying significantly expressed genes in RNA-seq analysis
"""

def gene_expression_threshold(gene_data:dict,threshold:int):

    genes =[]

    for key, value in gene_data.items():
        if value > threshold:
            genes.append(key)

    return genes


data = gene_expression_threshold(gene_data={"BRCA1": 450, "TP53": 120, "EGFR": 890}, threshold=200)
print(data)