# ⚖️ Legal-Ease: AI Contract Analysis System

> **Understand complex legal contracts in seconds using explainable AI.**

Legal-Ease is a **Retrieval-Augmented Generation (RAG)** application that enables users to upload legal contracts (PDFs) and interact with them through natural language queries.
The system ensures **accurate, grounded responses with source citations**, minimizing hallucinations.

---

## 🚀 Features

* 📄 Upload and process legal contract PDFs
* 🔍 Semantic search using **FAISS vector database**
* 🤖 AI-powered Q&A using **Google Gemini-Pro**
* 📌 **Source Citations** (page number + text excerpt)
* 🎛 Adjustable AI creativity (**temperature control**)
* ⚡ Fast and efficient document retrieval (Top-K chunks)

---

## 🧠 System Architecture

```
User Query
   ↓
PDF Upload → Text Chunking → Embeddings
   ↓
FAISS Vector Store
   ↓
Top-K Retrieval
   ↓
Gemini LLM
   ↓
Answer + Source Citations
```
## 📸 Demo

> Add your screenshot here

```
assets/demo.png
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Jayantsinghkhanna/legal-ease-ai.git
cd legal-ease-ai
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables

Create `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

### 5️⃣ Run Application

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
RAG_Legal/
│── src/
│   ├── document_loader.py
│   ├── vector_store.py
│   ├── qa_chain.py
│   ├── utils.py
│   └── __init__.py
│
│── data/
│── app.py
│── requirements.txt
│── .env
```

---

## ⚡ Key Engineering Highlights

* ✅ Implemented **RAG pipeline from scratch**
* ✅ Designed **source citation mechanism** to reduce hallucination
* ✅ Optimized chunk overlap for better context retention
* ✅ Modular architecture for scalability
* ✅ Interactive UI with **real-time parameter tuning**

---

## 🚧 Future Improvements

### 🔥 High Impact

* Multi-document querying
* Chat history / memory (Conversational RAG)
* Hybrid search (BM25 + Vector)
* Deployment (AWS / Docker / Hugging Face Spaces)

---

### ⚡ Advanced Features

* Clause extraction (termination, liability, etc.)
* Risk highlighting system
* Legal summarization
* PDF annotations

---

### 🧠 AI Enhancements

* Re-ranking (improve retrieval quality)
* Fine-tuned legal LLM
* Knowledge graph integration

---

## 📊 Potential Use Cases

* Legal contract review
* Compliance analysis
* Business agreements
* Internship/learning tool for law + AI

---

## 👨‍💻 Author

**Jayant Singh Khanna**

* 💻 Computer Engineering Student
* 🤖 Interested in AI, ML & Systems
* 🎯 Building real-world AI applications

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share feedback!
