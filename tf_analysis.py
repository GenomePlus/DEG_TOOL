import networkx as nx

def build_tf_network(tf_df, deg_genes):
    filtered = tf_df[tf_df["TargetGene"].isin(deg_genes)]
    G = nx.Graph()

    for _, row in filtered.iterrows():
        G.add_edge(row["TF"], row["TargetGene"])

    return G, filtered
