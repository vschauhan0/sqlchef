import streamlit as st
from pathlib import Path
from langchain_classic.agents import create_sql_agent
from langchain_community.callbacks import StreamlitCallbackHandler
from langchain_classic.agents import AgentType
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq
from urllib.parse import quote_plus
from langchain_classic.sql_database import SQLDatabase
import os
from dotenv import load_dotenv

load_dotenv()

st.title("SQL Chef: Chat with your Database")

LOCALDB='USE_LOCALDB'
MYSQLDB='USE_MYSQLDB'

radio_option=['SQLite3 (company.db)','Connect to MySql']

selected_option = st.sidebar.radio(
    "Choose Database to Chat : ",
    options=radio_option
)

if selected_option=='Connect to MySql':
    db_uri=MYSQLDB
    mysql_host=st.sidebar.text_input("Provide Mysql Hostname: ",value='localhost')
    mysql_user=st.sidebar.text_input("Provide Mysql Username: ",value='root')
    mysql_password=st.sidebar.text_input("Provide Mysql Password: ",type='password')
    mysql_db=st.sidebar.text_input("Provide Mysql DataBase Name: ")

else:
    db_uri=LOCALDB


groq_api=st.sidebar.text_input("Provide Groq API: ",type='password')

if not groq_api:
    st.info("Please provide your Groq API to continue")
    st.stop()

llm = ChatGroq(model='llama-3.3-70b-versatile',groq_api_key=groq_api,streaming=True)

@st.cache_resource(ttl=7200)
def configure_db(db_uri,mysql_host=None,mysql_user=None,mysql_password=None,mysql_db=None):
    if db_uri==LOCALDB:
        dbfilepath=(Path(__file__).parent/"company.db").absolute()
        creator=lambda: sqlite3.connect(f"file:{dbfilepath}?mode=ro",uri=True)
        return SQLDatabase(create_engine("sqlite:///",creator=creator))
    
    elif db_uri==MYSQLDB:
        if not(mysql_host and mysql_user and mysql_password and mysql_db):
            st.error("Please Provide all MySql Details")
            st.stop()
        
        encoded_password=quote_plus(mysql_password)
        conection_str=f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}"

        try:
            db=SQLDatabase(create_engine(conection_str))
            st.success("Connected to MySql")
            return db
        
        except Exception as e:
            st.error(f"Error: {e}")
            st.stop()

if db_uri==MYSQLDB:
    db=configure_db(db_uri,mysql_host,mysql_user,mysql_password,mysql_db)
else:
    db=configure_db(db_uri)

toolkit=SQLDatabaseToolkit(db=db,llm=llm)

agent=create_sql_agent(llm=llm,toolkit=toolkit,verbose=True,agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

if "messages" not in st.session_state or st.sidebar.button("clear message history"):
    st.session_state['messages'] = [
        {"role":"assistant","content":"How can I help you today?"}
    ]

for msg in st.session_state['messages']:
    st.chat_message(msg['role']).write(msg['content'])

user_query = st.chat_input(placeholder="Ask Anything from Database...")

if user_query:
    st.session_state['messages'].append(
        {'role':'user','content':user_query}
    )

    st.chat_message("user").write(user_query)

    with st.chat_message("assistant"):
        streamlit_callback = StreamlitCallbackHandler(st.container())

        response = agent.run(
            user_query,
            callbacks=[streamlit_callback]
        )

        st.session_state['messages'].append(
            {"role":"assistant","content":response}
        )

        st.write(response)