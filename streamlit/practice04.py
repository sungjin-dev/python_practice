import streamlit as st
import pandas as pd

st.title("과목 점수 분석")

rows = [
    {"subject": "국어", "score": 80},
    {"subject": "영어", "score": 90},
    {"subject": "수학", "score": 100},
    {"subject": "윤리", "score": 90},
    {"subject": "한국지리", "score": 70},
    {"subject": "법과사회", "score": 80},
    {"subject": "경제", "score": 100},
    {"subject": "한국사", "score": 80},
    {"subject": "근현대사", "score": 70}
]

df = pd.DataFrame(rows)
st.dataframe(df, hide_index=True)
st.bar_chart(df.set_index("subject")["score"])
st.metric("평균",f"{df['score'].mean():.1f}")