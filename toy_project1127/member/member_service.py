def register_member(name, phone):    
    if not name.strip():        
        raise ValueError("이름을 입력하세요.")    
    if not phone.strip():        
        raise ValueError("연락처를 입력하세요.") 


    insert_member(name, phone)