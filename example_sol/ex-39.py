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

 