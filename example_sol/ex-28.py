#####################################################################        
# 실습문제28: 별모양 출력   01.다양한형태의 제에문 12번 슬라이드
# lab 28
for i in range(1, 6):
    print("*" * i)

# 2중 for 버전
for i in range(1,6):
    s = ''
    for j in range(1,i+1):
        s += '*'
    print(s)
##################################################################### 