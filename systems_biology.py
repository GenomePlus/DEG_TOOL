import numpy as np
import networkx as nx

def network_entropy(G):
    degrees = np.array([d for _, d in G.degree()])
    if degrees.sum() == 0:
        return 0

    p = degrees / degrees.sum()
    return -np.sum(p * np.log2(p + 1e-10))


def network_density(G):
    return nx.density(G)


def network_centralization(G):
    degrees = np.array([d for _, d in G.degree()])
    max_deg = degrees.max()
    n = len(degrees)

    if n <= 2:
        return 0

    return np.sum(max_deg - degrees) / ((n - 1) * (n - 2))


def network_heterogeneity(G):
    degrees = np.array([d for _, d in G.degree()])
    if degrees.mean() == 0:
        return 0
    return np.std(degrees) / degrees.mean()
