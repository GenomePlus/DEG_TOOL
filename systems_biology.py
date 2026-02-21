from database_connector import fetch_string_ppi
from network_analysis import NetworkAnalysis
from mirna_analysis import analyze_mirna
from tf_analysis import analyze_tf
from pathway_analysis import analyze_pathways

def run_systems_pipeline(gene_list):

    # PPI
    ppi_df = fetch_string_ppi(gene_list)
    network = NetworkAnalysis(ppi_df)
    centrality = network.compute_centrality()

    # Regulatory
    mirna_results = analyze_mirna(gene_list)
    tf_results = analyze_tf(gene_list)

    # Pathways
    pathway_results = analyze_pathways(gene_list)

    return {
        "ppi_graph": network.G,
        "centrality": centrality,
        "mirna": mirna_results,
        "tf": tf_results,
        "pathways": pathway_results
    }
