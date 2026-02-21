import matplotlib.pyplot as plt
import numpy as np

def volcano_plot(df, logfc_col, pval_col, regulation_col):
    plt.figure(figsize=(8,6))

    df["neglog10"] = -np.log10(df[pval_col] + 1e-10)

    colors = {
        "Upregulated": "red",
        "Downregulated": "blue",
        "Not Significant": "grey"
    }

    for label, group in df.groupby(regulation_col):
        plt.scatter(
            group[logfc_col],
            group["neglog10"],
            c=colors[label],
            label=label,
            alpha=0.6
        )

    plt.xlabel("logFC")
    plt.ylabel("-log10(p-value)")
    plt.legend()
    plt.tight_layout()

    return plt
