#https://blog.zarathu.com/posts/2023-02-01-streamlit/

import streamlit as st
from openai import OpenAI
with st.sidebar:
    openai_api_key = st.text_input ("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/11m-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces]"

st.title("💬 Jay's bot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st. stop()

    client = OpenAI(api_key= openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message ("user"). write(prompt)
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)