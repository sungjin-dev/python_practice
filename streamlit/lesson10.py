from pathlib import Path
import streamlit as st
from common import parse_sales, summarize

st.set_page_config(page_title="매출 대시보드", layout="wide")
st.title("업로드 매출 대시보드")
uploaded = st.file_uploader("UTF-8 CSV", type=["csv"])  # resolve() : 상대 경로를 절대 경로로 변환
sample = Path(__file__).resolve().parents[1] /".vscode" /"data"/"sales.csv"
raw = uploaded.getvalue() if uploaded else sample.read_bytes()
try :
    rows =parse_sales(raw)
except ValueError as exc:
    st.error(str(exc))
    st.stop()
choices = ["전체"] + sorted({row["product"]for row in rows})  # 리스트 + 연산인듯?
selected = st.selectbox("상품", choices)
filtered = rows if selected == "전체" else [
    row for row in rows if row["product"] == selected
]

summary = summarize(filtered)
st.metric("총매출", f"{summary['revenue']:,}원")
st.metric("수량", summary["quantity"])
st.dataframe(filtered)
if filtered:
    st.bar_chart(summary["by_product"])
else:
    st.info("표시할 데이터가 없습니다.")