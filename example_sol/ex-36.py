#####################################################################
# 실습문제36: 로또번호 추출기 여러 게임   02. 리스트 23번 슬라이드
# lab 36
import random

games = 5
nums = range(1,46)
lottos = []

for game in range(games):
    lotto = []

    while len(lotto) < 6:
        n = random.choice(nums)
        # if not(n in lotto):
        if n not in lotto:
            lotto.append(n)
    
    lottos.append(lotto)

print(lottos)

