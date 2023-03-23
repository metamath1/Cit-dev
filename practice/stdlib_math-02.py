import math

a = int(input("첫 번째 수 a를 입력하세요: "))
b = int(input("두 번째 수 b(a보다 같거나 큰)를 입력하세요: "))

for i in range(1, a+1):
    if a % i == 0 and b % i == 0:
        print(i)

print( '최대공약수: ', math.gcd(a, b) )

