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


You have to add a new file named **HTML_QA.py** and copy paste the code in it and then you can run below

```python
! streamlit run HTML_QA.py & npx localtunnel --port 8501
```

Once done you will get an IP address and url as shown in below image, follow the instructions in Youtube video to run the app

![alt text](https://github.com/sahansach/MyFirstApp/assets/156666001/bfdc1019-65ae-4230-85c4-1a9653b45668)
