import streamlit as st
import time
import openai

# STATE SETUP
MESSAGES = "messages"
OPENAI_MODEL = "openai_model"
OPENAI_KEY = "openai_key"
if MESSAGES not in st.session_state:
    st.session_state[MESSAGES] = []
if OPENAI_MODEL not in st.session_state:
    st.session_state[OPENAI_MODEL] = "gpt-3.5-turbo"
if OPENAI_KEY not in st.session_state:
    st.session_state[OPENAI_KEY] = st.secrets["OPENAI_KEY"]


# UI
st.title("Neo4j ChatBot Demo")

go_local = st.toggle("Run locally", False)
if go_local:
    # Use llama
    print('Running in local mode')
    n4j_host = st.secrets["NEO4J_HOST_LOCAL"]
    n4j_user = st.secrets["NEO4J_USER_LOCAL"]
    n4j_password = st.secrets["NEO4J_PASSWORD_LOCAL"]

else:
    # Use OpenAI
    n4j_host = st.secrets["NEO4J_HOST_CLOUD"]
    n4j_user = st.secrets["NEO4J_USER_CLOUD"]
    n4j_password = st.secrets["NEO4J_PASSWORD_CLOUD"]


# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Enter question"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        openai.api_key = st.session_state[OPENAI_KEY]
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
            model=st.session_state[OPENAI_MODEL],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})