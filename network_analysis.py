import networkx as nx
from itertools import combinations

class NetworkAnalysis:

    def __init__(self, ppi_df):
        self.G = nx.Graph()

        if not ppi_df.empty:
            for _, row in ppi_df.iterrows():
                self.G.add_edge(
                    row["preferredName_A"],
                    row["preferredName_B"],
                    weight=row["score"]
                )

    # ---------- BASIC CENTRALITIES ---------- #

    def degree(self):
        return dict(self.G.degree())

    def betweenness(self):
        return nx.betweenness_centrality(self.G)

    def closeness(self):
        return nx.closeness_centrality(self.G)

    def eigenvector(self):
        try:
            return nx.eigenvector_centrality(self.G, max_iter=1000)
        except:
            return {}

    def pagerank(self):
        return nx.pagerank(self.G)

    # ---------- CLUSTERING ---------- #

    def clustering_coefficient(self):
        return nx.clustering(self.G)

    # ---------- ECCENTRICITY ---------- #

    def eccentricity(self):
        try:
            return nx.eccentricity(self.G)
        except:
            return {}

    # ---------- MCC (Maximal Clique Centrality) ---------- #

    def mcc(self):
        scores = {}
        cliques = list(nx.find_cliques(self.G))

        for node in self.G.nodes():
            node_cliques = [c for c in cliques if node in c]
            score = 0
            for clique in node_cliques:
                score += factorial(len(clique)-1)
            scores[node] = score
        return scores

    # ---------- MNC ---------- #

    def mnc(self):
        scores = {}
        for node in self.G.nodes():
            neighbors = list(self.G.neighbors(node))
            subgraph = self.G.subgraph(neighbors)
            scores[node] = subgraph.number_of_nodes()
        return scores

    # ---------- DMNC ---------- #

    def dmnc(self):
        scores = {}
        for node in self.G.nodes():
            neighbors = list(self.G.neighbors(node))
            subgraph = self.G.subgraph(neighbors)
            if subgraph.number_of_nodes() > 0:
                score = subgraph.number_of_edges() / (subgraph.number_of_nodes() ** 1.7)
            else:
                score = 0
            scores[node] = score
        return scores

    # ---------- Radiality ---------- #

    def radiality(self):
        scores = {}
        path_lengths = dict(nx.all_pairs_shortest_path_length(self.G))
        diameter = nx.diameter(self.G) if nx.is_connected(self.G) else 1

        for node in self.G.nodes():
            total = sum(path_lengths[node].values())
            scores[node] = (diameter + 1) - (total / len(path_lengths[node]))
        return scores

    # ---------- Stress ---------- #

    def stress(self):
        scores = dict.fromkeys(self.G.nodes(), 0)
        for source in self.G.nodes():
            paths = nx.single_source_shortest_path(self.G, source)
            for target in paths:
                for node in paths[target]:
                    if node != source and node != target:
                        scores[node] += 1
        return scores

    # ---------- EPC ---------- #

    def epc(self):
        scores = {}
        for node in self.G.nodes():
            scores[node] = sum([self.G[node][nbr].get("weight",1) for nbr in self.G.neighbors(node)])
        return scores

    # ---------- ALL ---------- #

    def compute_all(self):

        return {
            "Degree": self.degree(),
            "Betweenness": self.betweenness(),
            "Closeness": self.closeness(),
            "Eigenvector": self.eigenvector(),
            "PageRank": self.pagerank(),
            "Clustering": self.clustering_coefficient(),
            "Eccentricity": self.eccentricity(),
            "MCC": self.mcc(),
            "MNC": self.mnc(),
            "DMNC": self.dmnc(),
            "Radiality": self.radiality(),
            "Stress": self.stress(),
            "EPC": self.epc()
        }


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
