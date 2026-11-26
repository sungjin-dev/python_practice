import streamlit as st
import pandas as pd

st.title("상품별 매출")

rows = [
{"product": "book", "quantity": 2, "price": 12000},
{"product": "pen", "quantity": 5, "price": 1500},
{"product": "note", "quantity": 4, "price": 4500},
{"product": "pencil", "quantity": 12, "price": 1000},
{"product": "eraser", "quantity": 35, "price": 500},
{"product": "bag", "quantity": 1, "price": 22500},
{"product": "white", "quantity": 7, "price": 3500},
]

df = pd.DataFrame(rows)
df["revenue"] = df["quantity"] * df["price"] # 딕셔너리 키밸류 추가하듯 열을 추가
df["Remarks"] = "NULL" # 딕셔너리 키밸류 추가하듯 열을 추가
st.dataframe(df, hide_index=True)
st.bar_chart(df.set_index("product")["revenue"])   # 가로(product) / 세로 (수입) 형태 막대그래프
st.metric("총매출", f"{int(df['revenue'].sum()):,}원")