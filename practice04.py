def basket_total(*prices):
    return sum(prices)

def basket(**kwargs):
    return kwargs

items = []

run = True
while (run) :
    print("1. 상품 정보 입력 2. 상품목록 조회 3. 종료")
    userSelectedNum = int(input("번호를 선택하세요."))
    if userSelectedNum == 1 :

        inputProduct = input("상품명을 입력하세요")
        inputPrice = int(input("가격을 입력하시오"))

        items.append(basket(product = inputProduct, price = inputPrice)) 
    elif userSelectedNum == 2 :
        print(sorted(items, key =lambda item: item['price'], reverse=True))    
    else :
        print("종료합니다.")
        run = False
        
print(len(items))
