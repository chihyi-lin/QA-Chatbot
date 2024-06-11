import streamlit as st
from helper import chain, create_vector_db

st.title("Codebasics Q&A")
btn = st.button("Create Knowledgebase")
if btn:
    create_vector_db()

input_text = st.text_input("Question: ")

if input_text:
    chain = chain()
    response = chain.invoke({"input": input_text})
    st.header("Answer")
    st.write(response["answer"])