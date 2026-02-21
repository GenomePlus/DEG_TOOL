from database_connector import run_enrichr

def analyze_pathways(gene_list):

    libraries = [
        "KEGG_2021_Human",
        "Reactome_2022",
        "GO_Biological_Process_2021"
    ]

    results = {}

    for lib in libraries:
        results[lib] = run_enrichr(gene_list, lib)

    return results
