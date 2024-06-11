# Codebasics FAQ: Chatbot for an online learning platform built with LangChain and Google's Vertex AI Model (text-bison-001)

This is a prototype FAQ Chatbot that answers customers' questions for an online learning platform named Codebasics. 

The LLM is provided with the FAQ dataset, containing frequently asked questions and answers.

For a given customer's question, if:
- It is in the FAQ database, the chatbot should respond with an answer similar to the one in the database. 
- Otherwise, it should just answer "I don't know" (rather than hallucinating).

## Examples
![Screen Shot 2024-06-11 at 17 24 12 PM](https://github.com/chihyi-lin/QA-Chatbot/assets/70022680/c64fb0e2-220b-40fe-b8ff-6aa8a77667f7)

![Screen Shot 2024-06-11 at 17 24 53 PM](https://github.com/chihyi-lin/QA-Chatbot/assets/70022680/7785b126-2abc-426f-9ee5-852e5b2ca0f5)

## Installation
```
pip install -r requirements.txt
```

## Usage
Run the user interface by executing:
```
streamlit run main.py
```
The Web app will open  in your browser.

You can add database by clicking the "Create Knolwedge Base" button.

## Sample Questions
- Do you guys provide internship and also do you offer EMI payments?
- Do you have javascript course?
- Should I learn power bi or tableau?
- I've a MAC computer. Can I use powerbi on it?

## Acknowledgement
The FAQ data is from Codebasics, and the implementation is adapted from [there](https://github.com/codebasics/langchain/tree/main/3_project_codebasics_q_and_a).
