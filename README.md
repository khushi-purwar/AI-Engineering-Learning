# AI Engineering Learning 🚀

A hands-on repository for learning and experimenting with **AI Engineering, LLMs, LangChain, Prompt Engineering, Chains, RAG, and ReAct-based AI agents**.

This repository focuses on learning by building practical examples and gradually combining individual concepts into more advanced AI applications.

---

## 📚 Topics Covered

- Large Language Models (LLMs)
- Prompt Templates & Messages
- LangChain Chains
- Custom Runnables
- Conditional & Parallel Chains
- Retrieval-Augmented Generation (RAG)
- ChromaDB
- ReAct Agents
- Tool Calling
- Structured Outputs
- Streaming
- SQL ReAct Agents
- Local Model Execution with Docker

---

## 🗂️ Project Structure

```text
AI-Engineering-Learning/
│
├── Chains/
│   ├── Chain_demo.ipynb
│   ├── Chain_with_customRunnable.ipynb
│   ├── Conditional_chain.ipynb
│   └── Parallel_chain.ipynb
│
├── LLM/
│   ├── chroma_db/
│   ├── Basic_Setup.ipynb
│   ├── Docker_Model_Runner.ipynb
│   ├── NovaS.pdf
│   └── RAG.ipynb
│
├── Prompt Templates/
│   ├── Messages.ipynb
│   └── PromptTemplate_Demo.ipynb
│
├── ReAct/
│   ├── ReAct_Demo.ipynb
│   ├── SQL_ReAct_Agent.ipynb
│   ├── Structured_Output.ipynb
│   ├── Tools.ipynb
│   ├── With_Stream.ipynb
│   └── init_db.py
│
├── ReAct RAG/
│   ├── ReAct_RAG_Demo.ipynb
│   └── Semantic_RAG.ipynb
│
├── main.py
├── pyproject.toml
├── requirements.txt
├── uv.lock
└── README.md




## ✨ Features

- **LLM Integration**: Basic setup and configuration for working with Large Language Models
- **RAG Implementation**: Retrieval-Augmented Generation with vector database (ChromaDB)
- **Prompt Engineering**: Template-based prompt management and optimization
- **ReAct Agents**: Reasoning and Acting agents for complex task execution
- **Structured Outputs**: Generate structured, predictable outputs from LLMs
- **Tool Integration**: Integrate external tools and APIs with LLM agents

## 📦 Prerequisites

- Python 3.11 or higher
- Jupyter Notebook or JupyterLab
- Google Generative AI API key (for demos using Google's models)

## 🚀 Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd Langchain_Demo
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
   Or using the project file:
   ```bash
   pip install -e .
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root with your API keys:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```

### 🧠 Learning Modules
## 1. LLM

The **LLM** section covers the fundamentals of working with Large Language Models
and building applications around them.

### Topics Covered

- **Basic LLM Setup** — Setting up and interacting with an LLM.
- **Model Configuration** — Configuring models and their parameters.
- **Local Model Execution** — Running models locally.
- **Retrieval-Augmented Generation (RAG)** — Providing external context to an LLM during generation.
- **Vector Databases with ChromaDB** — Storing and retrieving embeddings for semantic search.


## 💻 Usage

### Running Jupyter Notebooks

1. Start Jupyter:
   ```bash
   jupyter notebook
   ```

2. Navigate to the desired demo folder and open the notebook

3. Follow the instructions within each notebook

### Running the Main Script

```bash
python main.py
```

## 📚 Modules

### LLM/
Contains demonstrations of core LLM functionality:
- **Basic_Setup.ipynb**: Introduction to LangChain, model initialization, and basic prompting
- **RAG.ipynb**: Implementing Retrieval-Augmented Generation using ChromaDB for document retrieval

### Prompt Templates/
- **PromptTemplate_Demo.ipynb**: Creating reusable prompt templates, variable substitution, and prompt optimization

### ReAct_Demo/
Advanced agent demonstrations:
- **ReAct_Demo.ipynb**: Building ReAct (Reasoning + Acting) agents that can use tools
- **Structured_Output.ipynb**: Generating structured data outputs (JSON, Pydantic models)
- **Tools.ipynb**: Creating and integrating custom tools with LangChain agents

## 🔧 Dependencies

Key dependencies include:

- **langchain** (>=1.3.11): Core LangChain framework
- **langchain-community** (>=0.4.2): Community integrations
- **langchain-google-genai** (>=4.2.6): Google Generative AI integration
- **chromadb** (>=1.5.9): Vector database for embeddings
- **google-genai** (>=2.10.0): Google's Generative AI SDK
- **pypdf** (>=6.14.2): PDF processing for document loading

See `pyproject.toml` or `requirements.txt` for the complete list.

## 📝 Notes

- The `chroma_db` folder contains persisted vector embeddings. Don't delete unless you want to regenerate embeddings.
- Each notebook is self-contained and can be run independently
- Make sure to set up your API keys before running the demos

## 🤝 Contributing

Feel free to explore, modify, and extend these demos for your own learning and projects.

## 📄 License

[Add your license information here]

---

**Happy Learning with LangChain! 🚀**
