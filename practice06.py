import json

A_class = {"영어", "수학", "사회","국어","경제"}
B_class = {"영어", "수학", "화학","생명","물리"}

print(sorted(A_class&B_class)) # 교집합
print(sorted(A_class-B_class)) # A반에만
print(sorted(B_class-A_class)) # B반에만

dict = {"name" : "민수", "subject" : "영어"}

text = json.dumps(dict, ensure_ascii=False)
print(json.loads(text))


