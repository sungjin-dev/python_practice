def sum_value(*args) :
    return sum(args)
def profile(**kwargs) :
    return kwargs

print(sum_value(3,4,5,6,7,11))
print(profile(name="민수", level="basic"))
items = [("pen", 1500) , ("book", 12000), ("eraser", 500)]
print(sorted(items, key=lambda item: item[1], reverse=True))  # 새로운 객체
print(items.sorted(items, key=lambda item: item[1], reverse=True)) # 원본 수정          