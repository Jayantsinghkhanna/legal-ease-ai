def extract_citations(source_documents):
    """
    Extract page number and text excerpt for citations.
    """
    citations = []

    for doc in source_documents:
        citations.append({
            "page": doc.metadata.get("page", "N/A"),
            "excerpt": doc.page_content[:300]
        })

    return citations
