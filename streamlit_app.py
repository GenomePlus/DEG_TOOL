import streamlit as st
import pandas as pd
from data_loader import load_uploaded_file
from deg_analysis import filter_deg
from database_connector import *
from network_analysis import *
from mirna_analysis import *
from tf_analysis import *
from pathway_analysis import *
from systems_biology import *
from visualization import *
from interpretation_engine import *

st.set_page_config(layout="wide")

tabs = st.tabs([
    "Upload Data",
    "Column Mapping & Filtering",
    "DEG Results",
    "Volcano Plot",
    "PPI Network",
    "miRNA Network",
    "TF Network",
    "Pathway Enrichment",
    "Systems Biology",
    "Scientific Interpretation"
])

with tabs[0]:
    uploaded = st.file_uploader("Upload DEG file")
    if uploaded:
        df = load_uploaded_file(uploaded)
        st.session_state["df"] = df
        st.dataframe(df.head())

with tabs[1]:
    if "df" in st.session_state:
        df = st.session_state["df"]

        gene_col = st.selectbox("Gene Column", df.columns)
        logfc_col = st.selectbox("logFC Column", df.columns)
        pval_col = st.selectbox("p-value Column", df.columns)

        neg = st.slider("Negative logFC", -10.0, 0.0, -1.0)
        pos = st.slider("Positive logFC", 0.0, 10.0, 1.0)
        pcut = st.slider("p-value cutoff", 0.0, 1.0, 0.05)

        if st.button("Filter DEGs"):
            full, sig, up, down = filter_deg(
                df, gene_col, logfc_col,
                pval_col, neg, pos, pcut
            )

            st.session_state["deg_full"] = full
            st.session_state["deg_sig"] = sig
            st.session_state["deg_up"] = up
            st.session_state["deg_down"] = down

            st.success("Filtering complete.")

with tabs[2]:
    if "deg_sig" in st.session_state:
        st.write("All Significant Genes")
        st.dataframe(st.session_state["deg_sig"])
        st.write("Upregulated")
        st.dataframe(st.session_state["deg_up"])
        st.write("Downregulated")
        st.dataframe(st.session_state["deg_down"])

with tabs[3]:
    if "deg_full" in st.session_state:
        fig = volcano_plot(
            st.session_state["deg_full"],
            logfc_col, pval_col, "Regulation"
        )
        st.pyplot(fig)
