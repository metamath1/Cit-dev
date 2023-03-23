def f369(n):
    if not isinstance(n, int) or n <= 0:
        print("자연수만 입력하세요.")
        return None
    
    str_n = str(n)

    print( '짝'*(str_n.count('3') + str_n.count('6') + str_n.count('9')) )

f369(-1)
f369('aaa')
f369(3.4)
f369(33569)