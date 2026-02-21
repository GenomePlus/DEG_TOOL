import networkx as nx
import numpy as np

def build_network(edge_df):
    G = nx.Graph()
    for _, row in edge_df.iterrows():
        G.add_edge(row["protein1"], row["protein2"], weight=row.get("score", 1))
    return G


def compute_centrality(G):
    degree = nx.degree_centrality(G)
    betweenness = nx.betweenness_centrality(G)
    closeness = nx.closeness_centrality(G)

    return degree, betweenness, closeness
