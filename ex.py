import streamlit as st
from groq import Groq

st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460); }
</style>
""", unsafe_allow_html=True)

st.title("Charan's Funny Bot")

if "messages" not in st.session_state:
    st.session_state.messages = []


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Type a message...")

if prompt:

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)


    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a funny sarcastic assistant."},
            *st.session_state.messages
        ]
    )
    reply = response.choices[0].message.content.strip()

    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)