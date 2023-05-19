#####################################################################
# 실습문제35: 로또번호 추출기   02. 리스트 19번 슬라이드
# lab 35
import random 

nums = range(1,46)
lotto = []

while len(lotto) < 6:
    n = random.choice(nums)
    is_in = False
    for i in lotto:
        if i == n:
            is_in = True

    if not is_in:
        lotto.append(n)

print(lotto)

####################################################################

nums = range(1,46)
lotto = []

while len(lotto) < 6:
    n = random.choice(nums)
    # if not(n in lotto):
    if n not in lotto:
        lotto.append(n)

print(lotto)
##################################################################### 