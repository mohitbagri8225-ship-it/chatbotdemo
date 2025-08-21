import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv,dotenv_values

load_dotenv()
llm=ChatGroq(
    temperature=0,
 groq_api_key=os.getenv("groq_api_key"),
    model_name="llama-3.3-70b-versatile"
)
prompt=ChatPromptTemplate.from_messages(
    [("system","You are an assistant who needs to breakdown the task given as {human_input} into short subtasks without any details seperated by -> with proper guidance.Also process the logs")]
    # ("human","{human_input}")]
)
chain=prompt| llm

st.set_page_config(page_title="Chatbot Demo")
st.title("Task summarizer agent")

a=st.text_area("Enter the task:")
if st.button("Submit"):
  with st.spinner("Processing the request"):
    inputs={
        'human_input':a

    }
    result=chain.invoke(inputs)
    st.success("Query processed successfully!!")
    st.write(result.content)