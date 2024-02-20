__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from openai import OpenAI


st.title('🦜🔗 Dapta PDF chatbot')

persist_dir = 'MyVectorEmbeddings'
vectordb = Chroma(persist_directory=persist_dir , embedding_function=OpenAIEmbeddings)


chat = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.0)

qa_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    retriever=vectordb.as_retriever()
)

def generate_response(query):
    st.info(qa_chain.run(query))

with st.form('my_form'):
    text = st.text_area('Enter text:', '')
    submitted = st.form_submit_button('Submit')
    response = generate_response(text)
    st.text(response)