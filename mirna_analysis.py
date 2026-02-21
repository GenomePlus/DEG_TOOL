from database_connector import run_enrichr

def analyze_mirna(gene_list):
    library = "miRTarBase_2017"
    return run_enrichr(gene_list, library)
