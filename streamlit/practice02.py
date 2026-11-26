import streamlit as st

st.set_page_config(page_title="태블릿 판매", layout="wide")
st.title("상품 판매")
st.markdown("**오늘 목표**: 하루 24시간 내 70개 판매")
st.markdown("단 오늘만 `30%`할인!!!")
st.markdown("---")
st.sidebar.header("초특급 할인")
st.sidebar.write("금일만 30% 할인")
st.sidebar.write("전화번호 : 042-777-7777")
st.sidebar.write("빨리 연락주세요!")
left, right = st.columns(2)
with left:
    st.header("스테디 셀러")
    st.write("가장 잘 팔리는 제품 15% 추가 할인")
with right:
    st.header("신제품")
    st.write("최신 사양 탑재 10% 추가 할인")