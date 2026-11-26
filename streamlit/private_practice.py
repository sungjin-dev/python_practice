import pandas as pd
import streamlit as st

st.title("Streamlit st.tabs 활용 예시")

# 1. 탭 생성 (tab1, tab2, tab3로 언패킹)
tab1, tab2, tab3 = st.tabs(["개요", "데이터 표", "설정"])

#2. 첫 번째 탭 : 요약 정보 및 메트릭
with tab1:
    st.header("프로젝트 개요")
    st.write("'st.tabs()'를 사용하면 한 페이지 안에서 화면을 깔금하게 나눌 수 있습니다.")

    col1, col2 = st.columns(2)
    col1.metric("활성 사용자", "1,240명", "+12%")
    col2.metric("전환율", "4.8%", "+0.6%")

# 3. 두 번째 탭: 데이터 프레임 및 필터
with tab2:
    st.header("판매 데이터")
    df = pd.DataFrame(
        {
            "지역":["대전","서울","부산","대구"],
            "매출(만원)": [320, 850, 410, 290]
        }
    )
    # st.slider(label, min_value=None, max_value=None, value=None, step=None, ...)

    min_sales=st.slider("최소 매출 필터(만원)",0,900,300,key="min_sales_slider")
    filtered_df = df[df["매출(만원)"] >=min_sales]      # key는 고유 이름표(ID) , css id와 유사    

#4. 세 번째 탭: 사용자 설정
with tab3:
    st.header("알림 설정")
    notify_email = st.checkbox("이메일 리포트 수신", value=True)
    frequency = st.selectbox("발송 주기",["메일", "매주", "매월"])

    if st.button("설정 저장"):
        st.success(f"저장 완료: 알림={notify_email}, 주기={frequency}")