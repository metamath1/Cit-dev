#####################################################################
# 실습문제34: 로또번호 추출기   02. 리스트 19번 슬라이드
# lab 34
import random 

nums = range(1,46)
lotto = []

while len(lotto) < 6:
    n = random.choice(nums)
    # if not(n in lotto):
    if n not in lotto:
        lotto.append(n)

print(lotto)
##################################################################### 