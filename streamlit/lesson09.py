import streamlit as st
st.title("계산 결과 재사용")
@st. cache_data(ttl=60)
def sum_squares(limit):
    return sum(n * n for n in range(limit+1))
limit =st.number_input("끝 숫자", min_value=1, max_value=10000, value = 3)
with st.spinner("계산 중"):
    result = sum_squares(int(limit))
st.metric("제곱합", result)
if st.button("이 함수 캐시 지우기"):
    sum_squares("캐시를 지웠습니다.")






#  동작 방식 핵심
# 역할: 데코레이터가 붙은 함수의 반환값을 메모리에 캐싱(저장)해 두었다가, 같은 인자로 다시 호출될 때 함수를 재실행하지 않고 저장된 결과를 바로 돌려줍니다.

# ttl=60 의미: Time-To-Live(유효 시간)를 60초로 설정합니다. 60초 이내에는 캐시된 값을 재사용하고, 60초가 지나면 캐시가 만료되어 다음 호출 시 함수를 다시 실행하고 결과를 갱신합니다.