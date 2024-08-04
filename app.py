import streamlit as st
import os
import io
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import FAISS  # Updated import
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Configure Google API
genai.configure(api_key=GOOGLE_API_KEY)

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_file = io.BytesIO(pdf.read())  # Convert the file-like object to a BytesIO stream
        pdf_reader = PdfReader(pdf_file)  # Use PdfReader to read from the BytesIO stream
        for page in pdf_reader.pages:
            text += page.extract_text() or ""  # Ensure no NoneType issues
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=10000,
        chunk_overlap=1000,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embedding)
    vectorstore.save_local("faiss_index")

def get_conversation_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context. Make sure to provide all the details. If the answer is not in
    the provided context, just say, "The answer is not available in the provided context." Do not provide the wrong answer.\n\n
    Context: \n{context}\n
    Question: \n{question}\n
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

def user_input(user_question):
    embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    # Load the FAISS index with dangerous deserialization allowed
    new_db = FAISS.load_local("faiss_index", embeddings=embedding, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)
    chain = get_conversation_chain()
    response = chain({"input_documents": docs, "question": user_question})
    # Directly access the output from the response
    st.write("Reply: ", response.get("output_text", "No response available"))

def main():
    st.set_page_config(page_title="PDF Chat App")
    st.header("Chat with Multiple PDFs using Gemini")
    
    # User input for questions
    user_question = st.text_input("Ask a question from the PDF Files")
    if user_question:
        user_input(user_question=user_question)

    # File upload and processing
    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & process", accept_multiple_files=True)
        if st.button("Submit & process"):
            if pdf_docs:
                with st.spinner("Processing..."):
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    get_vectorstore(text_chunks)
                    st.success("Processing complete. You can now ask questions.")
            else:
                st.warning("Please upload at least one PDF file.")

if __name__ == '__main__':
    main()
