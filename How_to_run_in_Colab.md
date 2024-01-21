To run in colab and streamlit refer below,

https://www.youtube.com/watch?v=ZZsyxIWdCko

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/ZZsyxIWdCko/0.jpg)](http://www.youtube.com/watch?v=ZZsyxIWdCko)

First install the following packages

```python
!pip install streamlit -q
!pip install openai
!pip install openai langchain sentence_transformers chromadb streamlit
!pip install --upgrade langchain
!pip install tiktoken
!pip install -U langchain-community
```

then run 

```python
!wget -q -O - ipv4.icanhazip.com
```



```python
! streamlit run HTML_QA.py & npx localtunnel --port 8501
```
