import networkx as nx

def build_mirna_network(mirna_df, deg_genes):
    filtered = mirna_df[mirna_df["TargetGene"].isin(deg_genes)]
    G = nx.Graph()

    for _, row in filtered.iterrows():
        G.add_edge(row["miRNA"], row["TargetGene"])

    return G, filtered
