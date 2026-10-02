import streamlit as st

st.set_page_config(page_title="NeuroNexus", page_icon="🧠", layout="centered")
st.title("🧠 NeuroNexus")
st.caption("Your AI Conversation Partner")

# Simple demo mode (no heavy model loading)
st.info("Running in simple demo mode. Type a message below.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your message here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Simple reply (replace this later with real model)
    reply = f"You said: **{prompt}**\n\n(This is a demo reply. Connect a real model later.)"
    
    with st.chat_message("assistant"):
        st.markdown(reply)
    
    st.session_state.messages.append({"role": "assistant", "content": reply})

if st.sidebar.button("Clear conversation"):
    st.session_state.messages = []
    st.rerun()