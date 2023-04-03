L = [1,2,3,4,5]

# 
# try:
#     print(L[len(L)])
#     a = 10 / 0
# except:
#     print("예외 발생")


# try:
#     # a = 10 / 0
#     print(L[len(L)])
# except ZeroDivisionError:    
#     print("0으로 나누는 예외 발생")
# except IndexError:
#     print("인덱스 예외 발생")


# try:
#     a = 10 / 0
#     print(L[len(L)])
# except ZeroDivisionError as e:    
#     print("0으로 나누는 예외 발생", e)
# except IndexError as e:
#     print("인덱스 예외 발생", e)


# 사용자 정의 예외

class SameNumberError(Exception):
    def __str__(self):
        return "나의 예외: 두 수가 같은 경우 발생"

def my_func(a, b):
    if a == b:
        raise SameNumberError
    else:
        return a+b
try:
    print(my_func(2,2))
except SameNumberError as e:
    print(e)


