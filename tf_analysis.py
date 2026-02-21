from database_connector import run_enrichr

def analyze_tf(gene_list):
    library = "ChEA_2016"
    return run_enrichr(gene_list, library)
