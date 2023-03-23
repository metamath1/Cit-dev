import random


print("0~1사이에 숫자를 하나 선택합니다.")
print(random.random())
print()

print("1~10사이에 정수 하나를 선택합니다.")
print( random.randrange(1, 11) )
print()

print("foo, bar, egg 중 하나를 선택합니다.")
print( random.choice(('foo', 'bar', 'egg')) )
