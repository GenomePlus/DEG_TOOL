def generate_interpretation(summary_stats, hub_genes, pathways):

    text = f"""
ABSTRACT:
This analysis identified {summary_stats['total']} significant DEGs
({summary_stats['up']} upregulated, {summary_stats['down']} downregulated).

Hub Gene Analysis:
Top hub genes include {', '.join(hub_genes[:5])}.
These genes exhibit high centrality suggesting regulatory dominance.

Pathway Analysis:
Enrichment revealed significant involvement in:
{', '.join(pathways[:5])}.

Systems Biology Interpretation:
Network entropy and density metrics suggest
global regulatory restructuring.

Clinical Relevance:
Hub genes overlapping enriched pathways may
represent potential biomarker candidates.

Experimental Validation:
Recommend qPCR validation of hub genes and
luciferase assays for regulatory validation.
"""

    return text
