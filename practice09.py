import random

def generate_dummy_cn_list(count = 10):

    cn_list = []
    weights = [2,3,4,5,6,7,8,9,2,3,4,5]

    for _ in range(count): # 언더스코어(_): "이 변수의 값은 쓰지 않는다"는 개발자 간의 관례
        year = random.randint(1970,2005)
        month = random.randint(1,12)
        day = random.randint(1,28)

        yy = str(year)[2:]
        mm = f"{month:02d}"  # 정수를 최소 2자리로 맞추되 빈 앞자리는 0으로 채움
        dd = f"{day:02d}"  

        if year < 2000:
            gender = random.choice([1, 2])
        else:
            gender = random.choice([3, 4])

        region_and_order = f"{random.randint(0, 99999):05d}"
        
        # 앞 12자리 조합
        first_12 = f"{yy}{mm}{dd}{gender}{region_and_order}"
        
        # 4. 마지막 검증 번호(Checksum) 계산
        total = sum(int(digit) * weight for digit, weight in zip(first_12, weights))
        check_digit = (11 - (total % 11)) % 10
        
        cn_list.append(f"{yy}{mm}{dd}-{gender}{region_and_order}{check_digit}")
        
    return cn_list

# 실행: 더미 주민번호 5개 생성
for cn in generate_dummy_cn_list(5):
    print(cn)