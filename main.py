import streamlit as st
import pandas as pd
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
import json
import sqlite3
from pymongo import MongoClient
import os
from typing import List, Dict, Any

# Configure page settings
st.set_page_config(
    page_title="Database Query Assistant (Gemini)",
    layout="wide",
    initial_sidebar_state="expanded"
)

class DatabaseProcessor:
    """Handles different types of database file processing"""
    
    @staticmethod
    def process_sql_file(file) -> str:
        """Process SQL file and return content as string"""
        try:
            content = file.read().decode('utf-8')
            conn = sqlite3.connect(':memory:')
            queries = content.split(';')
            tables_info = []
            
            for query in queries:
                if query.strip():
                    try:
                        conn.execute(query)
                        cursor = conn.cursor()
                        # Get table names
                        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                        tables = cursor.fetchall()
                        
                        for table in tables:
                            table_name = table[0]
                            # Get schema
                            cursor.execute(f"PRAGMA table_info({table_name});")
                            schema = cursor.fetchall()
                            # Get sample data
                            cursor.execute(f"SELECT * FROM {table_name} LIMIT 5;")
                            sample_data = cursor.fetchall()
                            
                            tables_info.append(f"Table: {table_name}")
                            tables_info.append(f"Schema: {schema}")
                            tables_info.append(f"Sample Data: {sample_data}")
                    except sqlite3.Error as e:
                        tables_info.append(f"Error processing query: {e}")
            
            return "\n".join(tables_info)
        except Exception as e:
            st.error(f"Error processing SQL file: {e}")
            return ""

    @staticmethod
    def process_mongodb_file(file) -> str:
        """Process MongoDB JSON file and return content as string"""
        try:
            data = json.loads(file.read().decode('utf-8'))
            return json.dumps(data, indent=2)
        except json.JSONDecodeError as e:
            st.error(f"JSON Error: {e}")
            return ""

    @staticmethod
    def process_csv_file(file) -> str:
        """Process CSV file and return content as string"""
        try:
            df = pd.read_csv(file)
            return f"CSV Data:\nColumns: {list(df.columns)}\nSample Data:\n{df.head().to_string()}"
        except Exception as e:
            st.error(f"CSV Error: {e}")
            return ""

def setup_gemini(api_key: str):
    """Configure Gemini with safety settings"""
    genai.configure(api_key=api_key)
    
    # Initialize the model
    model = genai.GenerativeModel('gemini-pro')
    
    # Create a basic prompt template
    def get_response(prompt, context):
        try:
            response = model.generate_content(
                f"""Context about the database:
                {context}
                
                User question: {prompt}
                
                Please provide a clear and concise answer based on the database information above."""
            )
            return response.text
        except Exception as e:
            st.error(f"Error from Gemini API: {e}")
            return "I apologize, but I encountered an error processing your request. Please try rephrasing your question."

    return get_response

def initialize_session_state():
    """Initialize Streamlit session state variables"""
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'db_content' not in st.session_state:
        st.session_state.db_content = None
    if 'gemini_handler' not in st.session_state:
        st.session_state.gemini_handler = None

def main():
    initialize_session_state()
    
    st.title("🤖 Database Query Assistant (Gemini)")
    
    # Sidebar configuration
    with st.sidebar:
        st.header("Configuration")
        api_key = st.text_input("Enter Google API Key", type="password")
        
        if api_key:
            if not st.session_state.gemini_handler:
                st.session_state.gemini_handler = setup_gemini(api_key)
        
        st.header("Upload Database")
        uploaded_file = st.file_uploader(
            "Choose your database file",
            type=['sql', 'json', 'csv']
        )
        
        if uploaded_file and api_key:
            with st.spinner("Processing database..."):
                processor = DatabaseProcessor()
                
                try:
                    if uploaded_file.name.endswith('.sql'):
                        content = processor.process_sql_file(uploaded_file)
                    elif uploaded_file.name.endswith('.json'):
                        content = processor.process_mongodb_file(uploaded_file)
                    else:  # CSV
                        content = processor.process_csv_file(uploaded_file)
                    
                    if content:
                        st.session_state.db_content = content
                        st.success("Database processed successfully!")
                except Exception as e:
                    st.error(f"Error processing file: {str(e)}")
    
    # Main chat interface
    st.header("Ask Questions About Your Database")
    
    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Query input
    if query := st.chat_input("Ask a question about your database"):
        if not api_key:
            st.error("Please enter your Google API key in the sidebar.")
            return
        
        if st.session_state.db_content is None:
            st.error("Please upload a database file first.")
            return
        
        with st.chat_message("user"):
            st.write(query)
            st.session_state.chat_history.append({"role": "user", "content": query})
        
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = st.session_state.gemini_handler(query, st.session_state.db_content)
                    st.write(response)
                    st.session_state.chat_history.append(
                        {"role": "assistant", "content": response}
                    )
                except Exception as e:
                    st.error(f"Error generating response: {str(e)}")

if __name__ == "__main__":
    main