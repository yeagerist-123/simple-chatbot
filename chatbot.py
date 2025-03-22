import streamlit as st
import os
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq

st.title('Basic Chatbot')
st.write('Chat with this simple AI assistant!')

api_key = st.sidebar.text_input("Enter your Groq API key:", type="password")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"]) 

if api_key:
    model = ChatGroq(
        model_name="llama3-70b-8192",
        groq_api_key=api_key,
        temperature=0.7,
    )
    
    memory = ConversationBufferMemory()
    conversation = ConversationChain(
        llm=model,
        memory=memory,
        verbose=False,
    )

    user_input = st.chat_input("Type your message here...")
    
    if user_input:
        with st.chat_message("user"):
            st.markdown(user_input)
        
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        with st.spinner("Thinking..."):
            response = conversation.predict(input=user_input)
        
        with st.chat_message("assistant"):
            st.markdown(response)
        
        st.session_state.messages.append({"role": "assistant", "content": response})
else:
    st.info("Please enter your Groq API Key in the sidebar to start chatting!")
    st.write("Don't have a key? Sign up at Groq to get one.")

st.sidebar.markdown('---')
st.sidebar.subheader("About this Chatbot")
st.sidebar.write(
    """This is a simple chatbot built with:
    - Streamlit
    - LangChain
    - ChatGroq
    
    To use it, simply enter your Groq API key and start chatting!
    """
)

        
    
        
        




