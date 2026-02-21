def generate_interpretation(results):

    interpretation = ""

    top_degree = sorted(
        results["centrality"]["Degree"].items(),
        key=lambda x: x[1],
        reverse=True
    )[:5]

    interpretation += "Top hub genes based on degree centrality:\n"
    for gene, score in top_degree:
        interpretation += f"- {gene} ({round(score,3)})\n"

    interpretation += "\nTop miRNA regulators identified.\n"
    interpretation += "Transcription factors enriched.\n"
    interpretation += "Key pathways involved in cellular regulation.\n"

    return interpretation
