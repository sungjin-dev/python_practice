import streamlit as st
st.title("계산 결과 재사용")
@st.cache_data(ttl=30)
def total(n):
    return sum(range(1,n+1))

n = st.number_input("n", min_value= 1, max_value= 10)
with st.spinner("계산 중"):
    result = total(int(n))
st.metric("순차합", result)
if st.button("이 함수 캐시 지우기"):
    sum.clear()
    st.success("캐시를 지웠습니다.")