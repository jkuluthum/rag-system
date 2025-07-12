import streamlit as st
from pipeline import ask_me

# --- Page Config ---
st.set_page_config(page_title="Romeo and Juliet Chatbot", layout="wide")
st.title("Chat About Romeo and Juliet")

# --- Instructions ---
with st.sidebar:
    st.subheader("Instructions")
    st.write("Ask any question about Romeo and Juliet.")
    
    if st.button("Clear Conversation"):
        st.session_state.conversation = []
        st.rerun()

# --- Initialize Conversation State ---
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# --- Display Chat History ---
for turn in st.session_state.conversation:
    with st.chat_message("user"):
        st.markdown(turn["question"])
    with st.chat_message("assistant"):
        #word_count = len(turn["answer"].split())
        st.markdown(f"{turn['answer']}")

# --- Chat Input ---
user_input = st.chat_input("Ask anything...")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Generating Response..."):
            response = ask_me(user_input)
        #word_count = len(response.split())
        st.markdown(f"{response}")

    # Store chat turn
    st.session_state.conversation.append({
        "question": user_input,
        "answer": response
    })
