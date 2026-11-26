import sys
import json
import config
from datetime import datetime

print("PYTHON FINAL PROJECT")
print("수업시간:", 60)
print("실행기:", sys.executable)

users= ["박찬호","박세리","박지성","이승엽","이강인","손흥민","홍길동"]

items = [{'product': 'pen', 'price': 1500}, 
         {'product': 'note', 'price': 8000}, 
         {'product': 'bag', 'price': 25000},
         {'product': 'book', 'price': 12000}, 
         {'product': 'eraser', 'price': 500}, 
         {'product': 'pencil', 'price': 2500}]

owned_items = {"book", "pen","pencil"}
wish_items = {"pen", "bag"}

confirmedBasket = []
quantity_check = []
customerInfo = []
purchase_list = []
transaction_history = []

memo = {}
login_id = ""

def calculator(price, quantity, shipping = 3000) :
    subtotal = price * quantity
    return subtotal + shipping

def basket_total(list):

    return sum(item['quantity'] * item['price'] for item in list)

def profile(**kwargs):
    return kwargs

run = True

while (run) :

    print("회원 정보를 불러옵니다.")
    customerInfo.append(profile(name="박찬호", level="basic"))
    customerInfo.append(profile(name="박세리", level="common"))
    customerInfo.append(profile(name="박지성", level="vip"))
    customerInfo.append(profile(name="이승엽", level="basic"))
    customerInfo.append(profile(name="이강인", level="common"))
    customerInfo.append(profile(name="손흥민", level="vip"))
    customerInfo.append(profile(name="홍길동", level="vvip"))    
    print("------------------------------------------")    
    print("=== 파이썬 스마트 스토어 & 학습 매니저 ===")
    print("1. 상품 목록 보기 2. 주문 담기 및 견적 계산, 3. 수량 일괄 정산 리포트, 4. 보유 vs 관심 상품 비교, 5. 주문 내역 및 저장 불러오기, 6. 회원 프로필 7. 추가 메모 등록, 0.종료")
    userSelectedNum = int(input("번호를 선택하세요."))
    if userSelectedNum == config.PRODUCT_LIST :
        list = []
        list = sorted(items, key =lambda item: item['price'], reverse=True)
        
        print("=======상품 목록=======")
        print(list) 
        print("----------------------------------------------------------------------")    
        print("최고가 상품")
        print(list[0])
        print("--------------------------------") 
        print("최저가 상품")
        print(list[-1])
        print("--------------------------------") 
        print("추천 TOP3") 
        print(list[:3])
        
    elif userSelectedNum == config.ADD_TO_CART :
        is_member = False

        inputUserName = input("사용자 이름을 입력하세요: ").strip()
        if inputUserName in users :
            print("회원인증되었습니다.")
            is_member = True
            login_id = inputUserName

        else :
            print("회원이 아닙니다.")

        run_a = True

        while (run_a) :
            purchase_total = []

            print("=====상품 주문 시작=====")  
            selectedNum = int(input("원하는 작업을 선택하세요 1. 상품 선택 및 수량 입력, 2. 최종결제 및 종료"))
            print("------------------------------------")
            purchase_Info = {}

            if selectedNum == 1 :  

                inputProduct = input("상품명을 입력하세요: ").strip()
                product = inputProduct.lower()

                price = 0

                for i in items :
                    if i['product'] == product:
                        price = i['price']
                
                inputQuantity = int(input("수량을 입력하시오: "))

                for i in range(len(items)):
                    quantity_check.append(0)

                for idx, item in enumerate(items) :
                            if  item['product'] == product:
                                quantity_check[idx] = inputQuantity   
                            
                for quantity in quantity_check :
                    if quantity <= 0:
                        continue

                print("------------------------------------")
    
                try :
                    inputQuantuty = int()
                except ValueError :
                    print("정수가 아닙니다.")
                    print("------------------------------------")

                total_price = calculator(price, inputQuantity)
                
                if total_price < 0:
                    message = "금액 오류"
                elif total_price >= 30000 and is_member: 
                    message = "무료배송"
                    total_price -= 3000
                else : 
                    message = "배송비 3000원"
                print(message)   

                purchase_list.append({"quantity": inputQuantity, "price": price})

            elif selectedNum == 2 : 
                print("총금액")
                print(basket_total(purchase_list))  

                confirmTest = input("구매를 원하십니까? (Y/N)").strip()
                confirm = confirmTest.lower()
                
                if confirm in ["Y", "y"] :
                    print("구매가 완료되었습니다.")
                    transaction_history.extend(purchase_list)
                    purchase_list = []
                    run_a = False
                else :
                    print("구매가 취소 되었습니다.")
                    purchase_total = []
                    purchase_list = []
                    break

    elif userSelectedNum == config.BULK_QUANTITY_SETTLEMENT :
       report = {str(i+1):v for i, v in enumerate(transaction_history)}
       print(report) 

    elif userSelectedNum == config.OWNED_VS_WATCHLIST : 
        print("보유 vs 관심 상품 비교")
        print("========================")
        
        print("보유 품목에만 있는 물품")
        print(sorted(owned_items-wish_items))
        print("--------------------------------")
        print("관심 품목에만 있는 물품")
        print(sorted(wish_items-owned_items))
        print("--------------------------------")
        print("공통으로 있는 물품")
        print(sorted(owned_items&wish_items)) 
        print("--------------------------------")
        print("모두 합친 물품")
        print(sorted(owned_items|wish_items)) 

    elif userSelectedNum == config.SAVE_AND_LOAD : 
        print("===주문 내역 정산===")

        userLevel = ""

        for item in customerInfo :
            if item['name'] == login_id :
                userLevel = item['level']

        data = {
            "name" : inputUserName,
            "total_price" : basket_total(transaction_history),
            "userLevel" : userLevel,
            "date" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        } 

        text = json.dumps(data, ensure_ascii=False)
        print(json.loads(text))

    elif userSelectedNum == config.USER_PROFILE :
        print("====매장 좌표====")
        location = ("서울","종로")
        x ,y = location
        print(x, y)

    elif userSelectedNum == config.MEMO:

        while (True) :
            memoNum = int(input("1. 메모 남기기, 2. 메모확인, 0. 종료"))

            if memoNum == 1 :

                memoDate = input("메모할 내용을 입력하세요: ")

                memo = {
                    "date" : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "content" : memoDate
                }

            elif memoNum == 2 : 
                text2 = json.dumps(memo, ensure_ascii=False)
                print(json.loads(text2))
            elif memoNum == 0 :
                print("메모 쓰기를 종료합니다.")
                break   

    elif userSelectedNum == config.EXIT:    
        print("종료합니다.")
        login_id = ""
        run = False

    else :
        print("잘못입력하셨습니다.")
        continue




