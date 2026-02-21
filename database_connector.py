import requests
import pandas as pd
from io import StringIO

SPECIES_ID = 9606


# ------------------ STRING PPI ------------------ #

def fetch_string_ppi(genes, score_threshold=700):
    genes_str = "%0d".join(genes)
    url = "https://string-db.org/api/tsv/network"

    params = {
        "identifiers": genes_str,
        "species": SPECIES_ID,
        "required_score": score_threshold,
        "caller_identity": "systems_biology_tool"
    }

    response = requests.post(url, data=params)

    if response.status_code != 200:
        return pd.DataFrame()

    return pd.read_csv(StringIO(response.text), sep="\t")


# ------------------ ENRICHR ------------------ #

def run_enrichr(gene_list, library):
    add_url = "https://maayanlab.cloud/Enrichr/addList"
    enrich_url = "https://maayanlab.cloud/Enrichr/enrich"

    genes_str = "\n".join(gene_list)

    payload = {"list": (None, genes_str)}
    response = requests.post(add_url, files=payload)

    if not response.ok:
        return pd.DataFrame()

    user_list_id = response.json()["userListId"]

    result = requests.get(enrich_url,
                          params={"userListId": user_list_id,
                                  "backgroundType": library})

    if not result.ok:
        return pd.DataFrame()

    data = result.json()[library]
    return pd.DataFrame(data)
