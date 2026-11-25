total = 0 
for number in range(1, 11) :
    if number % 2 != 0 :
        continue
    total += number
print(total)
print("----------------")

total = 0 
for number in range(1, 11) :
    if number % 2 == 0 :
        continue
    total += number
print(total)
print("----------------")

for number in range(1,11):
    if number % 2 != 0 :
        continue
    print(number, end=" , ")

print()
print("----------------")

for number in range(1,11):
    if number % 2 == 0 :
        continue
    print(number, end=" , ")

