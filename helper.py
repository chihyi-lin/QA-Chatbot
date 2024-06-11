from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAI
from langchain_community.document_loaders import CSVLoader
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

import os
from dotenv import load_dotenv

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=os.environ["GOOGLE_API_KEY"])
instructor_embeddings = HuggingFaceInstructEmbeddings(model_name='hkunlp/instructor-large')

vectordb_file_path = "faiss_index"


def create_vector_db():
    loader = CSVLoader(file_path="codebasics_faqs.csv", source_column="prompt", encoding='cp1252')
    data = loader.load()
    # create a vector database from data
    vectordb = FAISS.from_documents(documents=data, embedding=instructor_embeddings)
    vectordb.save_local(vectordb_file_path)


def chain():
    # Load the vector database from the local folder
    vectordb = FAISS.load_local(vectordb_file_path, 
                                instructor_embeddings,
                                allow_dangerous_deserialization = True)
    retriever = vectordb.as_retriever(score_threshold=0.6)
    template = """Given the following context and a question, generate an answer based on this context only.
In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

CONTEXT: {context}

QUESTION: {input}"""

    prompt = ChatPromptTemplate.from_template(template)
    document_chain = create_stuff_documents_chain(llm, prompt)
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    return retrieval_chain


if __name__ == "__main__":
    create_vector_db()
    retrieval_chain = chain()
    response = retrieval_chain.invoke({"input": "Do you offer javascript course?"})
    print(response['answer'])
