import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent[1]))
import streamlit as st                         # 상위 폴더가 parent[0], 그거보다 더 상위가 parent[1]
from common import parse_sales
st.write("필수 열: product, quantity, price")
upload = st.file_uploader("UTF-8 CSV", type=["csv"])
if upload is not None:
    try:
        st.dataframe(parse_sales(upload.getvalue()))
    except ValueError as exc:
        st.error(str(exc))