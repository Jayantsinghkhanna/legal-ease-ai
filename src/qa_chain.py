from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def build_qa_chain(vectorstore, temperature: float):
    """
    Build a modern RAG QA chain using LCEL (LangChain Expression Language).
    """

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        temperature=temperature
    )

    prompt = ChatPromptTemplate.from_template(
        """
        You are a legal contract analysis assistant.

        Answer the user's question using ONLY the provided context.
        If the answer is not present in the context, say:
        "The contract does not specify this information."

        Context:
        {context}

        Question:
        {question}
        """
    )

    chain = (
        {
            "context": retriever,
            "question": lambda x: x["question"],
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain, retriever
