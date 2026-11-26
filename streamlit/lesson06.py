import streamlit as st
st.title
if "count" not in st.session_state:
    st.session_state.count = 0
if st.button("증가"):
    st.session_state.count +=1
if st.button("초기화"):
    st.session_state.count = 0
st.metric("gus")
