import requests
import pandas as pd

ENRICHR_ADD = "https://maayanlab.cloud/Enrichr/addList"
ENRICHR_ENRICH = "https://maayanlab.cloud/Enrichr/enrich"

def run_enrichr(gene_list, library):
    genes_str = "\n".join(gene_list)

    response = requests.post(ENRICHR_ADD, files={"list": genes_str})
    user_list_id = response.json()["userListId"]

    response = requests.get(
        ENRICHR_ENRICH,
        params={
            "userListId": user_list_id,
            "backgroundType": library
        }
    )

    data = response.json()[library]

    columns = [
        "Rank", "Term", "P-value",
        "Z-score", "Combined Score",
        "Genes", "Adjusted P-value"
    ]

    return pd.DataFrame(data, columns=columns)
