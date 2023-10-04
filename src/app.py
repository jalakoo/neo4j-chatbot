import streamlit as st
from n4j import Driver
from llm_manager import LLMManager
from llm_type import LLMType

# STATE SETUP
MESSAGES = "messages"
OPENAI_MODEL = "openai_model"
OPENAI_KEY = "openai_key"
if MESSAGES not in st.session_state:
    st.session_state[MESSAGES] = []

# UI
st.title("Neo4j ChatBot Demo")

# Configure Neo4j driver & LLM Type
go_local = st.toggle("Run locally", False)
if go_local:
    # Use llama
    llm_type = LLMType.LLAMA
    llm_model = st.secrets["LLAMA_MODEL"]
    llm_key = st.secrets["LLAMA_KEY"]
    n4j_host = st.secrets["NEO4J_HOST_LOCAL"]
    n4j_user = st.secrets["NEO4J_USER_LOCAL"]
    n4j_password = st.secrets["NEO4J_PASSWORD_LOCAL"]
    st.info('Running in local mode')
else:
    # Use OpenAI
    llm_type = LLMType.OPENAI
    llm_model = st.secrets["OPENAI_MODEL"]
    llm_key = st.secrets["OPENAI_KEY"]
    n4j_host = st.secrets["NEO4J_HOST_CLOUD"]
    n4j_user = st.secrets["NEO4J_USER_CLOUD"]
    n4j_password = st.secrets["NEO4J_PASSWORD_CLOUD"]

# Init'sh 
n4j = Driver(n4j_host, n4j_user, n4j_password)
llm_manager = LLMManager(llm_type, llm_model, llm_key)

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
# Using Streamlit's chat_input API
if prompt := st.chat_input("Enter question"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        for response in llm_manager.chat_completion(prior_messages=st.session_state.messages):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")


        message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})