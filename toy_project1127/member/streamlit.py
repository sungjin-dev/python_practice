import streamlit as st
st.title("고객 관리 시스템")
name = st.text_input("고객 이름")
phone = st.text_input("연락처")
if st.button("고객 등록"):    
    try:        
        register_customer(name, phone)        
    st.success("등록 완료!")    
    except ValueError as e:        
    st.error(str(e))

if submitted:
    conn = sqlite3.connect("customer.db")

    conn.execute(
        """
        INSERT INTO customers (name, age, phone)
        VALUES (?, ?, ?)
        """,
        (name, age, phone)
    )

    conn.commit()
    conn.close()

    st.success("고객 등록 완료!")