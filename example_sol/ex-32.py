#####################################################################        
# 실습문제32: updown숫자 맞추기   01.다양한형태의 제에문 19번 슬라이드
# lab 32
import random

nums = list(range(1, 101))
num = random.choice(nums)

print("컴퓨터가 숫자를 골랐습니다.")
n = -1
j = 0

while n != num:
    n = int( input("(1~100) 숫자를 맞춰 보세요 >>>") )
    j += 1

    if n > num:
        print('donw 입니다.')
    elif n < num:
        print('up 입니다.')
    else:
        print('정답입니다!')
        print('총시도 횟쉬: ', j)
        break
##################################################################### 