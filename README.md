<h1>Web Content Analysis and Question Answering using AI</h1>
<h2>Problem Statement</h2>
The natural language processing problem I am trying to solve is extracting and analyzing text from web pages and then using that information to answer questions. This involves several sub-problems:

- **_Web Content Extraction:_** Need to extract the text content from a given URL. This is not a trivial task as web pages contain a lot of non-textual and irrelevant content like ads, menus, footers, etc.
- **_Text Chunking_**: The extracted text can be very large and may not fit into the memory of our machine or the input size of our model. So, need to split the text into manageable chunks.
- **_Question Answering_**: Given a question, need to find the most relevant answer from the chunks of text. This involves understanding the semantics of the question and the text.


<h2>Solution Approach</h2>
This solution approach involves several steps and makes use of various libraries and models.

- **_Web Content Extraction:_**  Use the **HTMLHeaderTextSplitter** class from the **langchain.text_splitter** module to extract the text content from the web page. This class splits the HTML content of the page based on the headers (h1, h2, etc.).
- **_Text Chunking:_** Use the **RecursiveCharacterTextSplitter** class from the **langchain.text_splitter** module to split the extracted text into chunks. This class recursively splits the text based on various separators like newline characters, periods, spaces, etc.
- **_Text Embedding:_** Convert the chunks of text into vector representations (embeddings) using the **OpenAIEmbeddings** class from the **langchain.embeddings.openai** module. These embeddings capture the semantic meaning of the text and can be used for similarity comparison.
- **_Vector Storage:_** Store the embeddings in a **Chroma** vector store from the **langchain.vectorstores** module. This allows us to efficiently search for the chunks of text that are most similar to a given query.
- **_Chat Model:_** Use the **ChatOpenAI** class from the **langchain.chat_models** module to generate responses to the questions. This class uses the **GPT-3.5-turbo** model from **OpenAI**.
- **_Question Answering:_** Use the **RetrievalQA** class from the **langchain.chains** module to answer the questions. This class takes a question, retrieves the most relevant chunks of text from the vector store, and generates a response using the chat model.
  
<h2>System Prompt</h2>

The system prompt provide to the language model is defined by the **PromptTemplate** class from the **langchain.prompts** module. The prompt template is a string with placeholders for the context and the question. The context is the relevant chunks of text retrieved from the vector store, and the question is the user’s question. The language model uses this prompt to generate the answer.

**In this case, the prompt template is:**

```python
prompt_template = """Use the following pieces of context to answer the question at the end. \
If you don't know the answer, just say that you don't know, don't try to make up an answer.\

{context}

Question: {question}
Answer:"""
```

This prompt instructs the language model to use the provided context to answer the question and to admit if it doesn’t know the answer.

<h2>Sample Outputs</h2>

![alt text](https://private-user-images.githubusercontent.com/156666001/298367256-23c9fa73-6b66-48f8-afaa-86c9010ec081.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDU4MjIxMTQsIm5iZiI6MTcwNTgyMTgxNCwicGF0aCI6Ii8xNTY2NjYwMDEvMjk4MzY3MjU2LTIzYzlmYTczLTZiNjYtNDhmOC1hZmFhLTg2YzkwMTBlYzA4MS5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMTIxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDEyMVQwNzIzMzRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0wZGNiZmI2ZThiNzEzMmYzMGFiY2UwZmFlOGNhMWM0NjU5MTJiYmQ1YjAyOWRiMWY1Mzg2NDU4YTQ4Yjg4MTVlJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.LX2HBIRCYIVBAxFq6fxEPA1YmZNdwYH3tze9AZHM-cE)

![alt text](https://github.com/sahansach/MyFirstApp/assets/156666001/9d0df38b-0709-4bee-994d-3dd84fb3625d)

<h2>Conclusion</h2>
This solution approach effectively solves the problem of web content analysis and question answering. It extracts and analyzes the text content from web pages and uses that information to answer questions. The use of advanced AI models and techniques ensures that the answers are accurate and relevant. However, the solution could be improved by handling more complex questions and by improving the accuracy of the web content extraction. Future work could also involve scaling the solution to handle larger web pages and more complex websites with lang translation.

