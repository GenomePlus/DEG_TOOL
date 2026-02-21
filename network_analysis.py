import networkx as nx

class NetworkAnalysis:

    def __init__(self, ppi_df):
        self.G = nx.Graph()
        for _, row in ppi_df.iterrows():
            self.G.add_edge(
                row["preferredName_A"],
                row["preferredName_B"],
                weight=row["score"]
            )

    def compute_centrality(self):
        return {
            "Degree": nx.degree_centrality(self.G),
            "Betweenness": nx.betweenness_centrality(self.G),
            "Closeness": nx.closeness_centrality(self.G),
            "Eigenvector": nx.eigenvector_centrality(self.G, max_iter=1000)
        }
