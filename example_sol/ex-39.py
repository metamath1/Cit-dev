#####################################################################
# 실습문제39: 최소값 찾기
# lab 39
L = [10, 3, 20, 100]

def find_min(L):
    min_value = L[0]

    for i in L[1:]:
        if i < min_value:
            min_value = i
    
    return min_value

min_value = find_min(L)
print(min_value)

# #####################################################################
# # 실습문제39: n*n인 *로 그려진 정사각형
# # lab 39

# def draw_rect(n):
#     for i in range(n):
#         print('*'*n)

# def draw_rect2(n):
#     for i in range(n):
#         if i == 0 or i == (n-1):
#             print('*'*n)
#         else:
#             print('*'+ ' '*(n-2) + '*')

# draw_rect2(1)
# ##################################################################### 