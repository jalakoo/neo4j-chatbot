import streamlit as st
from n4j import Driver
from llm_manager import LLMManager
from llms.llm_type import LLMType

# STATE SETUP
MESSAGES = "messages"
OPENAI_MODEL = "openai_model"
OPENAI_KEY = "openai_key"
if MESSAGES not in st.session_state:
    st.session_state[MESSAGES] = []

# UI
st.title("Neo4j ChatBot Demo")

# CONFIG
c1, c2 = st.columns(2)
# Configure Neo4j driver
with c1:
    db_mode = st.radio(
        "Neo4j Database",
        ["Movies"],
        captions = ["Sandbox instance of Movies DB"]).lower()
    if db_mode == "movies":
        n4j_host = st.secrets["NEO4J_HOST_CLOUD"]
        n4j_user = st.secrets["NEO4J_USER_CLOUD"]
        n4j_password = st.secrets["NEO4J_PASSWORD_CLOUD"]
    else:
        n4j_host = st.secrets["NEO4J_HOST_LOCAL"]
        n4j_user = st.secrets["NEO4J_USER_LOCAL"]
        n4j_password = st.secrets["NEO4J_PASSWORD_LOCAL"]

# Configure LLM scheme
with c2:
    type = st.radio(
        "LLM Mode",
        ["OpenAI", "Cypher Rag", "Vector Search"],
        captions = ["OpenAI Directly.", "OpenAI <> Cypher", "Langchain + Neo4j Vector"]).lower()

    if type == "cypher rag":
        llm_type = LLMType.CYPHER_RAG
        llm_model = st.secrets["OPENAI_MODEL"]
        llm_key = st.secrets["OPENAI_KEY"]
    elif type == "vector search":
        llm_type = LLMType.VECTOR
        llm_model = ""
        llm_key = ""
    else:
        # Default to OpenAI
        llm_type = LLMType.OPENAI
        llm_model = st.secrets["OPENAI_MODEL"]
        llm_key = st.secrets["OPENAI_KEY"]

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
        # full_response = ""

        # for response in llm_manager.chat_completion(
        #     prior_messages=st.session_state.messages,
        #     neo4j_uri=n4j_host,
        #     neo4j_user=n4j_user,
        #     neo4j_password=n4j_password):
        
        #     print(f'response: {response}')

        #     full_response += response.choices[0].delta.get("content", "")
        #     message_placeholder.markdown(full_response + "▌")
        full_response = llm_manager.chat_completion(
            prior_messages=st.session_state.messages,
            neo4j_uri=n4j_host,
            neo4j_user=n4j_user,
            neo4j_password=n4j_password)

        message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})