# LangChain Demo Project

A comprehensive demonstration project showcasing various LangChain capabilities including Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), Prompt Templates, and ReAct agents.

## 📋 Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
- [Dependencies](#dependencies)

## 🗂️ Project Structure

```
Langchain_Demo/
├── main.py                          # Main entry point
├── pyproject.toml                   # Project configuration and dependencies
├── requirements.txt                 # Python package requirements
├── README.md                        # Project documentation
│
├── LLM/                            # Large Language Model demos
│   ├── Basic_Setup.ipynb           # Basic LLM setup and configuration
│   ├── RAG.ipynb                   # Retrieval-Augmented Generation demo
│   └── chroma_db/                  # ChromaDB vector store data
│       ├── chroma.sqlite3
│       └── 79cb7ece-bd3f-4f1c-94c5-a41d55dbfb19/
│
├── Prompt Templates/               # Prompt engineering demos
│   └── PromptTemplate_Demo.ipynb   # Prompt template examples
│
└── ReAct_Demo/                     # ReAct agent demonstrations
    ├── ReAct_Demo.ipynb            # ReAct agent implementation
    ├── Structured_Output.ipynb     # Structured output generation
    └── Tools.ipynb                 # Tool usage and integration
```

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
