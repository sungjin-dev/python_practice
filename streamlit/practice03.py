import streamlit as st

st.title("계산기")

priceA = st.number_input("단가", min_value = 100, max_value = 9990000, value=1000)
quantityA = st.number_input("수량", min_value = 1, max_value = 99, value=1)

totalA = int(priceA) * int(quantityA)

st.metric("A총액", f"{totalA:,}원")

priceB = st.number_input("단가", min_value = 100, value=1000)
quantityB = st.number_input("수량", min_value = 1, value=1)

totalB = int(priceB) * int(quantityB)
st.metric("A총액", f"{totalA:,}원")


st.write("그밖에 계산 결과")

st.metric("총액 차이", f"{abs(totalA-totalB):,}원")





