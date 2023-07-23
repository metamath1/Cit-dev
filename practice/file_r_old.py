print("파일을 모두 읽습니다.")
f = open('file_w.txt', 'r', encoding='utf-8')
print( f.read() ) # 숫자는 한 글자(character)
f.close()

print("\n파일을 한줄씩 읽습니다.")
f = open('file_w.txt', 'r', encoding='utf-8')
print( f.readline(), end='' )
print( f.readline(), end='' )
f.close()

print("\n파일을 for문을 통해 모두 읽습니다.")
f = open('file_w.txt', 'r', encoding='utf-8')
for line in f:
    print(line, end='')
f.close()

print("\n파일을 모두 읽어 리스트로 반환 받습니다.")
f = open('file_w.txt', 'r', encoding='utf-8')
lines = f.readlines()
for line in lines:
    print(line, end='')
f.close()