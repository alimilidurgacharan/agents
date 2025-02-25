import streamlit as st
from utils import apply_styles
from agents import agent, as_stream
from dotenv import load_dotenv

load_dotenv()

st.title('Chat Bot')

if st.button('new chat'):
    st.session_state.messages = []
    st.rerun()

apply_styles()

if "messages"  not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message("content"))

if prompt := st.chat_input("ask me something"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        chunks = agent.run(prompt, stream=True)
        response = st.write_stream(as_stream(chunks))
        st.session_state.messages.append({"role": "assistant", "content": response})
