# 🤖 LangGraph-Based Modular Chatbot

A modular, extensible chatbot framework built using [LangGraph](https://python.langchain.com/docs/langgraph/), with a plug-and-play architecture to support various use cases like basic chat, agents, tool usage, memory, and more.

---

## 📌 Features

- 🔁 Graph-based conversation flow using `LangGraph`
- 💬 Streamlit-based UI for real-time interaction
- 📦 Modular structure: easily extend nodes, use cases, and state logic
- 🧠 Basic chatbot node to get started
- 🛠️ Easy integration with any LLM (OpenAI, Groq, Mistral, etc.)
- 🔍 Debugging support for transparent execution

---

## 🧱 Project Structure
```bash
LangGraphChatbot/
│
├── app.py                             # 🔹 Entry point to run the Streamlit chatbot app
│
├── requirements.txt                   # 🔹 Python dependencies
├── README.md                          # 🔹 Project documentation
│
├── src/                               # 🔸 Source code
│   └── Langraph/
│       ├── __init__.py
│       ├── graph_builder.py           # 🔹 Builds the LangGraph pipeline based on usecase
│       ├── display_result.py          # 🔹 Handles UI output and response display in Streamlit
│
│       ├── state/
│       │   ├── __init__.py
│       │   └── state.py               # 🔹 LangGraph state class definition
│
│       └── nodes/
│           ├── __init__.py
│           └── basic_chatbot_node.py  # 🔹 Basic chatbot node logic
│
└── assets/                            # (Optional) Static files, images, logos, etc.
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/dhanush-r-m/Agentic-ChatBot.git
cd langgraph-chatbot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app.py
```
### 5. Configuration 

```bash
export GROQ_API_KEY=your_key_here
```

---

## 🙋‍♂️ Author
- Dhanush R Moolemane


