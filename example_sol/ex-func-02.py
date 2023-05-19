#####################################################################
# 실습문제 번외: 함수: n자씩 끊어 쓰기

def print_mxn(s, n):
    for i in range(0, len(s), n):
        sub_s =  s[i:i+n]
        
        print( sub_s + ('_' * (n - len(sub_s))) )


def print_by_n_characters(s, n):
    for i in range(0, len(s), n):
        print(s[i:i+n].ljust(n, '_'))


def wrap_and_fill(string, n):
    print(
        '\n'.join([string[i:i + n].ljust(n, '_') 
                   for i in range(0, len(string), n)])
    )
    

print_mxn("1234567", 3)
print_by_n_characters("1234567", 3)
wrap_and_fill("1234567", 3)
#####################################################################