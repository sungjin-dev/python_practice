import io
import streamlit as st
import pandas as pd

#python -m streamlit run streamlit/app.py --server.address 127.0.0.1

st.set_page_config(page_title="첫 앱", layout="centered")
st.header("오늘의 학습목표 : streamlit")
st.title("상품별 매출")
rows = [
{"product": "book", "quantity": 2, "price": 12000},
{"product": "pen", "quantity": 5, "price": 1500},
{"product": "note", "quantity": 7, "price": 2500},
{"product": "bag", "quantity": 3, "price": 25000},
{"product": "eraser", "quantity": 15, "price": 500},
{"product": "pencil", "quantity": 8, "price": 1000},
]

df = pd.DataFrame(rows)
df["revenue"] = df["quantity"] * df["price"]
st.dataframe(df, hide_index=True)
st.bar_chart(df.set_index("product")["revenue"])
st.metric("총매출", f"{int(df['revenue'].sum()):,}원")


st.title("주문 미리보기")
with st.form("order_form"):  # 즉시 스크립트 실행X, 일단 모아둠(트랜잭션 느낌인가)
    name = st.text_input("이름")
    raw = st.text_input("수량", value="1")
    submitted = st.form_submit_button("계산")
if submitted: # st.form_submit_button("계산")을 누르는 순간 폼 안의 값들이 한꺼번에 반영, 스크립트가 재실행되고, submitted가 True(조건문 돌아감)
    st.session_state.pop("result", None) #이전 데이터 제거(총액)
    try:
        quantity = int(raw)
        if not name.strip() or not 1<= quantity <=100:
            raise ValueError("이름과 1~100의 수량을 입력하세요.")
        st.session_state.result = quantity*8000
    except ValueError:
        st.error("이름과 1~100의 정수 수량을 확인하세요.")
if "result" in st.session_state:
    st.metric("총액", f"{st.session_state.result:,}원")
 #st.session_state는 사용자 세션 동안 값이 유지되는 딕셔너리 형태 저장소

st.caption("이메일 형식 검증을 단순화한 미리보기입니다.")
with st.form("apply"):
    email = st.text_input("이메일")
    people = st.number_input("인원", min_value = 1, max_value=10)
    done = st.form_submit_button("미리보기")
if done:
    if "@" not in email:
        st.error("이메일을 확인하세요.")
    else :
        st.write(email, int(people))