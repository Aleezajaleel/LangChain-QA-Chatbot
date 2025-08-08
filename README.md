# LangChain-QA-Chatbot
# 💬 Conversational Q&A Chatbot with Message History (LangChain)

This is a conversational question-answering chatbot powered by [LangChain](https://www.langchain.com/), designed to handle multi-turn dialogues while preserving context using message history.

---

## 🚀 Features

- 🧠 **Context-Aware Responses**  
  Remembers previous messages and responds accordingly.

- 🧩 **LangChain Integration**  
  Uses LangChain to connect with LLMs and handle the logic of message flow.

- 📜 **Message History Management**  
  Stores and retrieves message history for continuous conversations.

- ⚡ **Fast & Lightweight API**  
  Built with Python for fast and scalable deployment (e.g., with FastAPI or Flask).

---

## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **OpenAI / LLM Backend**
- **(Optional)** FastAPI or Flask for API routing

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Aleezajaleel/LangChain-QA-Chatbot.git
cd LangChain-QA-Chatbot
python -m venv venv
source venv/bin/activate     # On Linux/Mac
venv\Scripts\activate        # On Windows

pip install -r requirements.txt
OPENAI_API_KEY=your_openai_key
python chatbot.py

