import matplotlib.pyplot as plt
import networkx as nx

def plot_ppi(G, centrality_dict, metric="Degree"):
    pos = nx.spring_layout(G)
    values = [centrality_dict[metric].get(n, 0) for n in G.nodes()]

    plt.figure(figsize=(10,8))
    nx.draw(G, pos,
            node_color=values,
            cmap="YlOrRd",
            with_labels=True,
            node_size=600)

    plt.title(f"PPI Network ({metric})")
    plt.tight_layout()
    plt.savefig("ppi.png", dpi=300)
    plt.close()
