import streamlit as st
st.title("참가인원 이메일 검증")

with st.form("apply"):
    name = st.text_input("이름")
    email = st.text_input("이메일")
    hours = st.number_input("주당 학습 시간", min_value=0, max_value=40, value=5)
    people = st.number_input("인원", min_value=1, max_value=10)
    submitted = st.form_submit_button("계산")
if submitted:
    if '@' not in email.strip() :
        st.error("이메일 형식으로 입력해주세요.")
    else:
        st.write(email, int(people))

