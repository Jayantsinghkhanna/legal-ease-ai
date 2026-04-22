import sys
import os
import streamlit as st
from dotenv import load_dotenv

# --------------------------------------------------
# Fix import path for Streamlit
# --------------------------------------------------
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)

# --------------------------------------------------
# Local imports
# --------------------------------------------------
from src.document_loader import load_and_split_pdf
from src.vector_store import create_faiss_index
from src.qa_chain import build_qa_chain
from src.utils import extract_citations

# --------------------------------------------------
# Load environment variables
# --------------------------------------------------
load_dotenv()

# --------------------------------------------------
# Streamlit page config
# --------------------------------------------------
st.set_page_config(
    page_title="Legal-Ease",
    layout="wide"
)

st.title("⚖️ Legal-Ease: AI Contract Analysis System")
st.caption("Retrieval-Augmented Generation (RAG) with source citations")

# --------------------------------------------------
# Sidebar controls
# --------------------------------------------------
st.sidebar.header("⚙️ Settings")

temperature = st.sidebar.slider(
    "AI Creativity (Temperature)",
    min_value=0.0,
    max_value=1.0,
    value=0.2,
    step=0.1
)

# --------------------------------------------------
# File upload
# --------------------------------------------------
uploaded_file = st.file_uploader(
    "Upload a Legal Contract (PDF)",
    type=["pdf"]
)

if uploaded_file:
    # Ensure data directories exist
    os.makedirs("data/uploads", exist_ok=True)
    os.makedirs("data/faiss_index", exist_ok=True)

    pdf_path = os.path.join("data/uploads", uploaded_file.name)

    # Save uploaded PDF
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("🔍 Processing contract and building knowledge base..."):
        documents = load_and_split_pdf(pdf_path)
        vectorstore = create_faiss_index(documents)

    # Build RAG chain + retriever
    qa_chain, retriever = build_qa_chain(vectorstore, temperature)

    st.success("✅ Contract processed successfully!")

    # --------------------------------------------------
    # User query
    # --------------------------------------------------
    query = st.text_input(
        "Ask a question about the contract",
        placeholder="e.g. What is the termination notice period?"
    )

    if query:
        with st.spinner("🤖 Analyzing contract..."):
            # Retrieve relevant chunks
            docs = retriever.get_relevant_documents(query)

            # Build context text
            context_text = "\n\n".join(
                [doc.page_content for doc in docs]
            )

            # Generate answer
            answer = qa_chain({
                "question": query,
                "context": context_text
            })

        # --------------------------------------------------
        # Display answer
        # --------------------------------------------------
        st.subheader("✅ Answer")
        st.write(answer)

        # --------------------------------------------------
        # Display citations
        # --------------------------------------------------
        st.subheader("📌 Source Citations")

        citations = extract_citations(docs)

        for idx, c in enumerate(citations, start=1):
            st.markdown(f"**Source {idx} — Page {c['page']}**")
            st.caption(c["excerpt"])

else:
    st.info("⬆️ Upload a PDF contract to get started.")
