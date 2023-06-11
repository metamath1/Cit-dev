#####################################################################
# 실습문제40: 로또 여러게임 만들기 함수
# lab 40
import random

games = 5
nums = range(1,46)
lottos = []

def make_games(L):
    lottos = []
    for lotto in L:
        while len(lotto) < 6:
            n = random.randrange(1, 46)
            if n not in lotto:
                lotto.append(n)
        lottos.append(lotto)

    return lottos

L = [[10, 3], [40, 31, 1], []] 
games = make_games(L)
print(games)
