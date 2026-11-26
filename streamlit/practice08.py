import streamlit as st

st.title("질문 길이 마지막 10개")

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.button("대화 지우기"):
    st.session_state.message = [] 

question = st.chat_input("질문을 입력하세요")

if question and question.strip():
    st.session_state.message += [
        {"role": "user", "content":question},
        {"role": "assistant", "content": f"질문 길이: {len(question)}"},
    ]

    st.session_state.messages = st.session_state.messages[-10:]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])   