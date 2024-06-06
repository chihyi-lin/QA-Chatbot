# Codebasics Q&A: Chatbot for an online learning platform built with LangChain and Google Palm
This is a prototype Q&A Chatbot that answers customers' questions for an online learning platform Codebasics. 
The data is from Codebasics, and the implementation is adapted from [there](https://github.com/codebasics/langchain/tree/main/3_project_codebasics_q_and_a).
For a given customer's question, if:
- it is in the Q&A database, the chatbot should respond with an answer similar to the one in the database. 
- Otherwise, it should just answer "I don't know" (rather than hallucinating).
