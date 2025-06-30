import streamlit as st

from chatbot import chatbot


def main():
    st.title("📘 AI Chatbot on 'Alice in Wonderland'")

    st.markdown("""
    Welcome! This chatbot answers questions by finding the most relevant sentence from *Alice’s Adventures in Wonderland*.

    ### 👉 How to use it:
    - Ask a question **related to the story**
    - Example questions:
        - *Who is Alice chasing?*
        - *Is there a rabbit?*
        - *What happens at the tea party?*
    - The chatbot will reply with the **closest sentence** from the book.

    ---
    """)

    question = st.text_input("💬 Your question:")
    if st.button("Submit"):
        response = chatbot(question)
        st.text_area("📖 Answer from the book:", value=response, height=120)


if __name__ == "__main__":
    main()
