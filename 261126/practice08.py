raw = ["3","x","7","","12"]
numbers = []
for value in raw :
    try:
        numbers.append(int(value))
    except ValueError :
        print("건너뜀:", repr(value))

squares = [n * n for n in numbers if n%2==1]
labels = {n:"짝수" if n % 2==0 else "홀수" for n in numbers} 
print(numbers, squares)
print(labels)

names = ["박찬호","박세리","박지성","이순신","이성계","이이","김유신","김구","김윤후"]


park = []
lee = []
kim = []

for value in names :
    try :
        park = [n for n in names if n[:1] == "박"]
        lee = [n for n in names if n[:1] == "이"]
        kim = [n for n in names if n[:1] == "김"]
    except ValueError :
            print("건너뜀:", repr(value))

print(park)
print(lee)
print(kim)


numbers = ["701110-1521083","810902-2692873","051219-3106944","050327-4923888","810802-1218369"]