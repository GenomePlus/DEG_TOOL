import streamlit as st
from systems_biology import run_systems_pipeline
from visualization import plot_ppi
from interpretation_engine import generate_interpretation

st.title("Integrated Systems Biology Analysis Platform")

genes_input = st.text_area("Enter gene symbols (comma-separated)")

if st.button("Run Analysis"):

    genes = [g.strip() for g in genes_input.split(",")]

    results = run_systems_pipeline(genes)

    plot_ppi(results["ppi_graph"], results["centrality"])
    st.image("ppi.png")

    st.subheader("miRNA Enrichment")
    st.dataframe(results["mirna"].head())

    st.subheader("TF Enrichment")
    st.dataframe(results["tf"].head())

    st.subheader("Pathway Enrichment")
    for lib, df in results["pathways"].items():
        st.write(lib)
        st.dataframe(df.head())

    st.subheader("Biological Interpretation")
    st.text(generate_interpretation(results))
