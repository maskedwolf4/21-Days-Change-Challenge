"""
**Q22 - Pathway Enrichment Analyzer**
Question: Create a class `PathwayEnrichment` that performs Fisher's exact test to identify over-represented biological pathways in a gene list.
Input: List of target genes, background gene set, pathway annotations
Expected Output: DataFrame with pathway IDs, p-values, and enrichment scores
Usage: Interpreting genomic data and understanding biological mechanisms
"""
import numpy as np
from scipy.stats import fisher_exact 
import pandas as pd

class PathwayEnrichment:
    """Performs pathway enrichment analysis using Fisher's exact test"""
    
    def __init__(self, pathway_annotations):
        """
        Args:
            pathway_annotations: dict of {pathway_id: list_of_genes}
        """
        self.pathway_annotations = pathway_annotations
        self.all_genes = set()
        for genes in pathway_annotations.values():
            self.all_genes.update(genes)
    
    def create_contingency_table(self, target_genes, pathway_genes, background_genes):
        """
        Creates 2x2 contingency table for Fisher's test
        
                    In Pathway    Not in Pathway
        Target          a               b
        Background      c               d
        """
        target_set = set(target_genes)
        pathway_set = set(pathway_genes)
        background_set = set(background_genes)
        
        # a: genes in both target and pathway
        a = len(target_set & pathway_set)
        
        # b: genes in target but not pathway
        b = len(target_set - pathway_set)
        
        # c: genes in pathway but not target (from background)
        c = len((background_set & pathway_set) - target_set)
        
        # d: genes in neither
        d = len(background_set - pathway_set - target_set)
        
        return [[a, b], [c, d]]
    
    def calculate_enrichment(self, target_genes, background_genes=None):
        """
        Calculates enrichment for all pathways
        
        Args:
            target_genes: List of genes of interest
            background_genes: All genes to consider (defaults to all annotated genes)
        """
        if background_genes is None:
            background_genes = list(self.all_genes)
        
        results = []
        
        for pathway_id, pathway_genes in self.pathway_annotations.items():
            # Create contingency table
            table = self.create_contingency_table(
                target_genes, pathway_genes, background_genes
            )
            
            # Perform Fisher's exact test
            odds_ratio, p_value = fisher_exact(table, alternative='greater')
            
            # Calculate enrichment score
            a, b = table[0]
            c, d = table[1]
            
            if a > 0:
                enrichment_score = (a / (a + b)) / ((a + c) / (a + b + c + d))
            else:
                enrichment_score = 0
            
            results.append({
                'pathway_id': pathway_id,
                'genes_in_pathway': len(pathway_genes),
                'genes_in_target': a,
                'p_value': p_value,
                'odds_ratio': odds_ratio,
                'enrichment_score': enrichment_score
            })
        
        # Convert to DataFrame and sort by p-value
        df = pd.DataFrame(results)
        df = df.sort_values('p_value')
        
        # Add Bonferroni correction
        df['p_value_corrected'] = df['p_value'] * len(df)
        df['p_value_corrected'] = df['p_value_corrected'].clip(upper=1.0)
        
        return df

# Test
pathway_annotations = {
    'PATHWAY_001_Cell_Cycle': ['BRCA1', 'TP53', 'CDK1', 'CDK2', 'CCNB1'],
    'PATHWAY_002_Apoptosis': ['TP53', 'BAX', 'BCL2', 'CASP3', 'CASP9'],
    'PATHWAY_003_DNA_Repair': ['BRCA1', 'BRCA2', 'RAD51', 'TP53', 'ATM'],
    'PATHWAY_004_Metabolism': ['GLUT1', 'HK1', 'PFKM', 'LDHA', 'PDK1']
}

# Genes of interest (e.g., differentially expressed)
target_genes = ['BRCA1', 'TP53', 'BRCA2', 'RAD51', 'ATM']

analyzer = PathwayEnrichment(pathway_annotations)
enrichment_results = analyzer.calculate_enrichment(target_genes)

print("Pathway Enrichment Results:")
print(enrichment_results[['pathway_id', 'genes_in_target', 'p_value', 
                          'enrichment_score', 'p_value_corrected']].round(4))
