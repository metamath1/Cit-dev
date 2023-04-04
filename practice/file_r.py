print("파일을 모두 읽습니다.")
with open('file_w.txt', 'r', encoding='utf-8') as f:
    f.seek(3) # ascii는 1 byte,  대부분 문자는 3byte
    print( f.read() ) # 숫자는 한 글자(character)

# print("\n파일을 한줄씩 읽습니다.")
# with open('file_w.txt', 'r', encoding='utf-8') as f:
#     print( f.readline(), end='' )
#     print( f.readline(), end='' )

# print("\n파일을 for문을 통해 모두 읽습니다.")
# with open('file_w.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         print(line, end='')
#     print()

# print("\n파일을 모두 읽어 리스트로 반환 받습니다.")
# with open('file_w.txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line, end='')
#     print()