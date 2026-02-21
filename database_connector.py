import requests
import pandas as pd
import gzip
import os

STRING_API = "https://string-db.org/api"

def fetch_string_interactions(genes, species=9606, score=0.7):
    if not genes:
        return pd.DataFrame()

    params = {
        "identifiers": "%0d".join(genes),
        "species": species,
        "required_score": int(score * 1000),
        "format": "tsv-no-header"
    }

    response = requests.post(
        f"{STRING_API}/network",
        data=params
    )

    if response.status_code != 200:
        raise Exception("STRING API failed")

    rows = []
    for line in response.text.strip().split("\n"):
        parts = line.split("\t")
        rows.append({
            "protein1": parts[2],
            "protein2": parts[3],
            "score": float(parts[5])
        })

    return pd.DataFrame(rows)


def load_mirtarbase(path="data/mirna_targets_human_validated_minimal.tsv.gz"):
    return pd.read_csv(path, sep="\t", compression="gzip")


def load_jaspar(path="data/jaspar_tf_targets_human_minimal.tsv.gz"):
    return pd.read_csv(path, sep="\t", compression="gzip")
