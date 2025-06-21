import streamlit as st
from chatbot import chatbot_response

st.title("🤖 Simple Chatbot")
# 🧠 Show examples of supported questions
with st.expander("💡 What can you ask me?"):
    st.markdown("""
    - 👋 Say hello: `Hi`, `Hello`, `Hey`
    - ❓ Ask for help: `Can you help me?`, `I need support`
    - 🕓 Ask the time: `What time is it?`
    - 🌦️ Ask for weather:`What's the weather like?`,`Is it raining?`, ` Weather today`
    - 📍 Ask location: `Where are you located?`
    - 😂 Hear a joke: `Tell me a joke`
    - 👋 Say goodbye: `Bye`, `See you later`
    """)
user_input = st.text_input("You:", "")

if user_input:
    response = chatbot_response(user_input)
    st.text_area("Bot:", value=response, height=100)
