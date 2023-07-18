#####################################################################
# 실습문제 번외: 369게임
# lab 40
# def f369(n):
#     if not isinstance(n, int) or n <= 0:
#         print("자연수만 입력하세요.")
#         return None
    
#     str_n = str(n)

#     print( '짝'*(str_n.count('3') + str_n.count('6') + str_n.count('9')) )

# f369(-1)
# f369('aaa')
# f369(3.4)
# f369(33569)

import ex_38

nums_str = input("숫자를 공백으로 구분해서 입력: ")

nums_str_list = nums_str.strip().split()

nums = []
for num in nums_str_list:
    nums.append(float(num))

print("평균: ", ex_38.mean(nums))
print("표준편차: ", ex_38.std(nums))

