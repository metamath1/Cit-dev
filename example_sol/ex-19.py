#####################################################################
# 실습문제19: 3의배수  02.반복문 12번 슬라이드
# lab 19
# 100까지 3의 배수
for i in range(1, 101):
    if i % 3 == 0:
        print(i)

i = 0
for j in range(33):
    i = i + 3
    print(i)


for i in range(3, 101, 3):
    print(i)
#####################################################################