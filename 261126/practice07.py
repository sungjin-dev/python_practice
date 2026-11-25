scores = ["1","-1","75","90","101","30","55","0","85","65","70"]

pure_scores, errors = [], []

try :
    scores = int("abc")
except ValueError :
    print("정수가 아닙니다.")

for n in scores:
    try :
        score = int(n)
        if scores <0 or scores >100 :
            raise ValueError("range")
        pure_scores.append(score)
    except ValueError :
        errors.append(n)

passedScores = [score for score in pure_scores if scores >= 60]

try :
    score = int("")
except ValueError : 
    score = ""