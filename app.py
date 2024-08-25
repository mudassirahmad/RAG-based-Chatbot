import streamlit as st
from src.helper import get_pdf_text, get_conversational_chain, get_text_chunks, get_vector_store

def user_input(user_prompt):
    response= st.session_state.conversation.invoke({'question': user_prompt})
    st.session_state.chatHistory = response['chat_history']
    for i, message in enumerate(st.session_state.chatHistory):
        if i%2==0:
            st.write("User", message.content)
        else:
            st.write("Reply:", message.content)

def main():
    st.set_page_config("Information Retrieval")
    st.header("RAG based LLM app") 
    
    user_prmpt = st.text_input("Ask a question from your uploaded PDF files")
    
    if "conversation" not in st.session_state:
        st.session_state.conversation = "None"
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = None
    if user_prmpt:
        user_input(user_prmpt)

    with st.sidebar:
        st.title("Menu")
        pdf_docs = st.file_uploader("Upload your PDF Files", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text= get_pdf_text(pdf_docs)
                text_chunks=  get_text_chunks(raw_text)
                vector_store = get_vector_store(text_chunks)
                st.session_state.conversation = get_conversational_chain(vector_store)

                st.success("Done")


if __name__=="__main__":
    main()