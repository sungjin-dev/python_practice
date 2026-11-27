from pathlib import Path
import streamlit as st
import pandas as pd
from common import parse_sales, summarize
from datetime import datetime

st.set_page_config(page_title="미니 POS & 매출 대시보드", layout="wide")
st.title("🏪올인원 미니 POS & 매출 분석기")
st.write("**학습 목표**: 입력(`form`), 상태 유지(`session_state`), 캐싱(`cache_data`), 데이터 시각화를 하나로 통합합니다.")

if "pos_orders" not in st.session_state:
    st.session_state.pos_orders = []

if "messages" not in st.session_state:
    default_message = {"role": "assistant", "content": "안녕하세요! '총매출', '인기상품', '주문건수' 등을 물어보세요."}
    st.session_state.messages = [default_message]

@st.cache_data(ttl=60)
def get_cached_summary(rows):
    return summarize(rows)

st.sidebar.header("⚙️ 데이터 관리")
st.sidebar.file_uploader("추가 매출 CSV 업로드 (UTF-8)", type=["csv"])

if st.button("요약 캐시 초기화"):
    st.session_state.pos_orders = []
    st.sidebar.warning("현장 주문 내역이 초기화되었습니다.")

uploaded = st.file_uploader("UTF-8 CSV", type=["csv"])  

path_check = Path(__file__).resolve().parents[1] /".vscode"/"data"/"sales.csv"  

base_rows = []

try:
    if uploaded :
        base_rows = parse_sales(uploaded.getvalue()) 
        st.sidebar.success(f"CSV에서 {len(base_rows)}행을 불러왔습니다.")  
    elif path_check:
        base_rows = parse_sales(path_check.read_bytes())
    else : 
        base_rows= [
            {"product": "book", "quantity": 2, "price": 12000, "month": "2026-11"}, 
            {"product": "pen", "quantity": 5, "price": 1500, "month": "2026-11"}]
except ValueError as exc:
    st.error(str(exc))    

all_rows = base_rows + st.session_state.pos_orders

tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 매출 대시보드", "💳 POS 주문 입력", "💬 매출 도우미 챗봇", "🧾​가계부 및 월간 지출", "✔️​TO-DO-LIST"])

with tab1:
    choices = ["전체"] + sorted({row["product"]for row in all_rows})  # 리스트 + 연산인듯?
    selected = st.selectbox("조회할 상품 선택", choices)

    if selected == "전체" :
        filtered = all_rows 
    else :
        filtered = [r for r in all_rows if r["product"] == selected]
        
    summary = summarize(filtered)

    col1, col2, col3 = st.columns(3)

    col1.metric("총매출", f"{summary['revenue']:,}원")
    col2.metric("총 판매 수량", f"{summary['quantity']:,}개")
    col3.metric("거래 건수", f"{len(filtered)}건")

    left, right = st.columns([1.2,1])

    st.header("상세 거래 내역")
    st.dataframe(filtered)

    if filtered:
        df = pd.DataFrame(filtered)
        df["subtotal"] = df["quantity"] * df["price"]
        st.dataframe(df, use_container_width = True, hide_index = True)
    else:
        st.info("표시할 데이터가 없습니다.")
        st.header("상품별 매출 비중")
    if summary["by_product"] :
        st.bar_chart(summary["by_product"])

with tab2 :
    st.header("신규 현장 주문 등록")

    if "pos_orders" not in st.session_state:
        st.session_state.pos_orders = []
    
    st.info(f"상품명 및 가격, {summary["by_product"]}")
    with st.form("pos_form", clear_on_submit = True):
        p_name = st.text_input("상품명 (1~40자)")
        c1, c2 = st.columns(2) 
        p_qty = c1.number_input("수량", min_value=1, max_value=1000, value=1)
        p_price = c2.number_input("단가 (원)", min_value=100, max_value=1_000_000, value=5000, step=500)

        summitted = st.form_submit_button("주문 추가")

    if summitted:
        st.session_state.pop("result", None) 

        clean_name = p_name.strip()
        
        if not clean_name or len(clean_name) > 40:
            st.error("상품명은 공백 제외 1~40글자로 입력하세요.")
        elif  clean_name not in summary["by_product"] :
            st.error("목록에 없는 상품입니다.")
        else:
            st.session_state.pos_orders.append({
                "product" : clean_name,
                "quantity" : int(p_qty),
                "price" : int(p_price),
                "month" : datetime.now().strftime("%Y-%m")
            })
            st.success(f"'{clean_name}' {p_qty}개 (총 {p_qty * p_price:,}원) 주문이 등록되었습니다! 대시보드 탭에서 확인하세요.")
            
with tab3 :
    st.header("데이터 기반 간단 Q&A")
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    prompt = st.chat_input("매출에 대해 질문해보세요 (예: 총매출 알려줘, 가장 잘 팔린 상품은?)")

    total_summary = get_cached_summary(all_rows)

    if prompt and prompt.strip():
        if prompt in ["총매출", "매출" ] : 
            reply= f"현재 누적 총매출은 **{total_summary['revenue']:,}원**입니다."
        elif prompt in ["인기", "가장",  "상품"] :  
            if total_summary["by_product"] :
                best = max(total_summary["by_product"].items(), key=lambda x: x[1])
                reply = f"매출 1위 상품은 **{best[0]}**이며, 총 **{best[1]:,}원**의 매출을 기록했습니다."
                
            else: 
                reply = "아직 등록된 상품 데이터가 없습니다."
        elif  prompt in ["수량", "건수"]  : 
            reply = f"총 거래 건수는 **{len(all_rows)}건**, 총 판매 수량은 **{total_summary['quantity']:,}개**입니다."
        else : 
            reply = "질문을 이해하지 못했습니다. **'총매출'**, **'인기 상품'**, **'판매 수량'** 키워드를 포함해 질문해 주세요!"
    else :
        reply = "아직 질문이 없습니다."
    
    st.session_state.messages.append({"role": "assistant", "content" : reply}) 
    st.session_state.messages = st.session_state.messages[-1:] 

    for message in st.session_state.messages :
        with st.chat_message(message["role"]):
            st.write(message["content"])

with tab4 :
    st.header("가계부 및 월간 지출 분석 페이지")

    st.title("월별 가계부")

    budget_info = st.session_state.pos_orders

    if not budget_info:
        st.error("아직 소비가 없습니다.")
    else :
        df = pd.DataFrame(budget_info)
        df["consume"] = df["quantity"] * df["price"]
        st.dataframe(df, hide_index = True)
        st.bar_chart(df.set_index("month")["consume"])
        st.metric("월별 소비", f"{int(df['consume'].sum()):,}원") 
        st.metric("최대 소비 달", f"{df['consume'].max():,}원")

with tab5 :       
    st.header("할일 목록")
    if "todos" not in st.session_state:
        st.session_state.todos = []
    new = st.text_input("할 일")
    if st.button("추가") and new.strip():
        st.session_state.todos.append(new.strip())
    if st.button("모두 지우기"):
        st.session_state.todos = []
    for number, todo in enumerate(st.session_state.todos, 1):
        st.write(f"{number}. {todo}")
    st.caption(f"총 {len(st.session_state.todos)}개")

    