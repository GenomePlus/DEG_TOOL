import streamlit as st
import pandas as pd

from systems_biology import run_systems_pipeline
from visualization import plot_ppi

st.set_page_config(layout="wide")

st.title("Integrated Systems Biology Platform")

genes_input = st.text_area(
    "Enter gene symbols (comma-separated)",
    placeholder="TP53, EGFR, BRCA1"
)

metric = st.selectbox(
    "Select CytoHubba Algorithm",
    [
        "Degree","Betweenness","Closeness","Eigenvector","PageRank",
        "Clustering","Eccentricity","MCC","MNC","DMNC",
        "Radiality","Stress","EPC"
    ]
)

if st.button("Run Analysis"):

    if not genes_input.strip():
        st.warning("Please enter gene symbols.")
        st.stop()

    genes = [g.strip().upper() for g in genes_input.split(",")]

    with st.spinner("Running systems biology analysis..."):

        try:
            results = run_systems_pipeline(genes)

            G = results["ppi_graph"]

            if G.number_of_nodes() == 0:
                st.error("No PPI interactions found from STRING.")
                st.stop()

            centrality = results["centrality"]

            plot_ppi(G, centrality, metric)
            st.image("ppi.png")

            st.subheader("Top Hub Genes")

            hub_df = pd.DataFrame(
                sorted(centrality[metric].items(),
                       key=lambda x: x[1],
                       reverse=True),
                columns=["Gene","Score"]
            )

            st.dataframe(hub_df.head(15))

            st.subheader("miRNA Enrichment")
            st.dataframe(results["mirna"].head())

            st.subheader("TF Enrichment")
            st.dataframe(results["tf"].head())

            st.subheader("Pathway Enrichment")
            for lib, df in results["pathways"].items():
                st.write(lib)
                st.dataframe(df.head())

            st.success("Analysis Completed")

        except Exception as e:
            st.error(f"Error occurred: {e}")
