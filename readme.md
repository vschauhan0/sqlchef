# 🍽️ SQL Chef — AI Powered Database Assistant

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/LangChain-AI-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Groq-LLM-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Database-SQL-lightgrey?style=for-the-badge">
</p>

---

# 🎥 Demo Videos

## 🗄️ sqlite3 Demo

https://github.com/user-attachments/assets/f8b3d14b-f095-4606-9f7e-840178d638ef

---

## 🗄️ MySQL Demo

https://github.com/user-attachments/assets/3cfcb707-900a-4587-93fb-5e9885979ff0

---

# 🚀 Overview

**SQL Chef** is an AI-powered SQL assistant that enables users to interact with databases using natural language queries.

Built using **LangChain Agents**, **Groq LLM**, and **Streamlit**, the application automatically converts human questions into SQL queries and retrieves results instantly.

The system supports both:

- SQLite Databases
- MySQL Databases

This project demonstrates the practical implementation of:

- Agentic AI
- Generative AI
- LLM-powered agents
- Natural Language to SQL conversion
- Database integrations
- Interactive AI applications

---

# ✨ Features

## 🤖 AI-Powered Querying

Ask questions like:

```text
Show top 5 highest paid employees
```

or

```text
How many sales were made last month?
```

without writing SQL manually.

---

## 🗄️ Multi Database Support

Supports:

- SQLite3
- MySQL

Users can dynamically switch databases from the sidebar.

---

## ⚡ Real-Time Streaming Responses

The app streams AI-generated responses live using:

- LangChain Callbacks
- Streamlit Callback Handler

---

## 🧠 Intelligent SQL Agent

Uses LangChain SQL Agent with:

- Zero Shot ReAct Reasoning
- Tool-based execution
- Automatic SQL generation

---

## 🔒 Secure Database Connection

- Password protected database access
- Environment variable support
- Safe database handling

---

## 🎨 Interactive UI

Modern chatbot-style interface built with Streamlit.

Features include:

- Chat history
- Sidebar configuration
- Database switching
- Live responses

---

# 🏗️ System Architecture

```text
+-------------------+
|   User Question   |
+-------------------+
          |
          v
+-------------------+
|   Streamlit UI    |
+-------------------+
          |
          v
+-------------------+
|   LangChain Agent |
+-------------------+
          |
          v
+-------------------+
|   Groq LLM Model  |
+-------------------+
          |
          v
+-------------------+
| SQL Query Builder |
+-------------------+
          |
          v
+-------------------+
| Database Engine   |
| SQLite / MySQL    |
+-------------------+
          |
          v
+-------------------+
| Final AI Response |
+-------------------+
```

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend Development |
| Streamlit | Frontend Web Interface |
| LangChain | AI Agent Framework |
| Groq API | Large Language Model |
| SQLAlchemy | Database ORM |
| SQLite3 | Local Database |
| MySQL | External Database |
| dotenv | Environment Variables |

---

# 📂 Project Structure

```bash
SQL-Chef/
│
├── app.py
├── company.db
├── requirements.txt
├── .env
├── README.md

```

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/sqlchef.git
cd sql-chef
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Required Libraries

```txt
streamlit
langchain
langchain-community
langchain-groq
sqlalchemy
mysql-connector-python
python-dotenv
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from:

👉 https://console.groq.com/

---

# ▶️ Running the Application

```bash
streamlit run app.py
```

Application will start on:

```text
http://localhost:8501
```

---

# 💻 Application Workflow

## Step 1

User enters database query in natural language.

---

## Step 2

LangChain Agent analyzes the prompt.

---

## Step 3

Groq LLM generates optimized SQL query.

---

## Step 4

SQLAlchemy executes query on database.

---

## Step 5

Results are formatted and displayed in chat interface.

---

# 🧪 Example Queries

```text
Show all employees working in HR department
```

```text
What is the average salary of employees?
```

```text
List top 10 sales records
```

```text
Which department has maximum employees?
```

```text
Show employee names with salary greater than 50000
```

---


# 🧠 Core Concepts Used

- LLM Applications
- AI Agents
- Natural Language Processing
- SQL Query Generation
- Streamlit Web Apps
- Database Management
- Prompt Engineering

---

# 🔥 Advanced Features

✅ Streaming AI Responses  
✅ Multi Database Connectivity  
✅ AI SQL Generation  
✅ LangChain Toolkits  
✅ Agentic Workflow  
✅ Chat History Management  
✅ Cached Database Connections  
✅ Dynamic Database Switching  

---

# 🚧 Future Enhancements

- PostgreSQL Support
- MongoDB Integration
- Data Visualization Dashboard
- Authentication System
- Query Export Feature
- Voice-based Database Queries
- AI Query Suggestions
- Dark Mode UI

---

# 📈 Resume Highlights

This project demonstrates strong understanding of:

- Generative AI
- LangChain Framework
- AI Agents
- LLM Integration
- Database Management
- Full Stack Development
- Streamlit Deployment
- Prompt Engineering

---

# 👨‍💻 Author

## Vansh Chauhan

AI & Full Stack Developer passionate about:

- Generative AI
- Machine Learning
- AI Agents
- Full Stack Applications

---

# 🌟 Show Your Support

If you liked this project:

⭐ Star the repository  
🍴 Fork the project  
📢 Share with others  

---

# 📜 License

This project is licensed under the MIT License.

---

# 🙌 Acknowledgements

Special thanks to:

- LangChain
- Groq
- Streamlit
- Open Source Community

for providing amazing tools and frameworks.
