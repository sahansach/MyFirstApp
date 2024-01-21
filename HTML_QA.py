# Import necessary libraries
import os
import requests
import configparser
import streamlit as st  # Streamlit library for creating web apps
from openai import OpenAI  # OpenAI library for AI models
from langchain.text_splitter import RecursiveCharacterTextSplitter, HTMLHeaderTextSplitter  # Text splitting tools
from langchain.embeddings.openai import OpenAIEmbeddings  # Embedding tools
from langchain.vectorstores import Chroma  # Vector storage tools
from langchain.chat_models import ChatOpenAI  # Chat model tools
from langchain.prompts import PromptTemplate  # Prompt template tools
from langchain.chains import RetrievalQA  # Question-Answering tools

#openai_api_key stored in config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

openai_api_key = config['SECRETS']['openai_api_key']
# Initialize OpenAI client with API key
client = OpenAI(api_key=openai_api_key)

# Create a form using the 'with' syntax
with st.form(key='my_form'):
    url = st.text_input(label='Enter the website url')
    input_text = st.text_input(label='Enter your query')
    submit_button = st.form_submit_button(label='Submit')

    # Processing will start only if both URL & Query inputs available
    if submit_button:
        if url and input_text:
            # Define headers to split on
            headers_to_split_on = [
                ("h1", "Header 1"),
                ("h2", "Header 2"),
            ]

            # Initialize HTML header text splitter
            html_splitter = HTMLHeaderTextSplitter(headers_to_split_on=headers_to_split_on)

            # Split text from URL
            html_header_splits = html_splitter.split_text_from_url(url)

            # Initialize recursive character text splitter
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,
                                                           chunk_overlap=10,
                                                           length_function=len,
                                                           separators=['\n\n', '\n', '.', ' ', ''],
                                                           add_start_index=True,
                                                           )

            # Split documents into chunks
            text_chunks = text_splitter.split_documents(html_header_splits)

            # Initialize OpenAI embeddings
            embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

            # Create Chroma vector store from documents
            url_search = Chroma.from_documents(text_chunks, embeddings)

            # Define chat model
            MODEL = "gpt-3.5-turbo"

            # Initialize chat model
            chat_llm = ChatOpenAI(model=MODEL,
                                  temperature=0,
                                  max_tokens=200,
                                  openai_api_key=openai_api_key,
                                  verbose=True)

            # Define prompt template
            prompt_template = """Use the following pieces of context to answer the question at the end. \
            If you don't know the answer, just say that you don't know, don't try to make up an answer.\

            {context}

            Question: {question}
            Answer:"""

            # Initialize prompt template
            PROMPT = PromptTemplate(
                template=prompt_template, input_variables=["context", "question"]
            )

            # Define chain type arguments
            chain_type_kwargs = {"prompt": PROMPT}

            # Initialize RetrievalQA
            qa2 = RetrievalQA.from_chain_type(llm=chat_llm,
                                              chain_type="stuff",
                                              retriever=url_search.as_retriever(),
                                              chain_type_kwargs=chain_type_kwargs)

            # Run the QA model with the input text
            response = qa2.run(input_text)

            # Display the response
            st.write(response)
        else:
            st.error("Please enter both a URL and a query.")
