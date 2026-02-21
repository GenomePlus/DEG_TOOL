import pandas as pd

def filter_deg(df, gene_col, logfc_col, pval_col,
               neg_threshold, pos_threshold, pval_cutoff):

    df = df.copy()

    df["Regulation"] = "Not Significant"

    df.loc[
        (df[logfc_col] >= pos_threshold) &
        (df[pval_col] <= pval_cutoff),
        "Regulation"
    ] = "Upregulated"

    df.loc[
        (df[logfc_col] <= neg_threshold) &
        (df[pval_col] <= pval_cutoff),
        "Regulation"
    ] = "Downregulated"

    up = df[df["Regulation"] == "Upregulated"]
    down = df[df["Regulation"] == "Downregulated"]
    significant = df[df["Regulation"] != "Not Significant"]

    return df, significant, up, down
