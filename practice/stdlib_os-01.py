import os

print("현재 폴더")
print(os.getcwd())
print()

print("현재 폴더에 있는 파일 및 디렉토리")
print(os.listdir())
print()

print("현재 폴더에 .py 파일만 가져오기")
for f in os.listdir():
    if f.endswith('.py'):
        print(f)
print()

print("dummy가 현재 폴더에 존재하는가?")
print( os.path.exists("dummy") )
print()

print("dummy가 폴더인가?")
print( os.path.isdir("dummy") )
print()

print("foo.txt가 폴더인가?")
print( os.path.isdir("foo.txt") )
print()

print(".\\path\\path2\\myfile.txt 경로를 os에 맞게 만들어주세요.")
print( os.path.join('.', 'path', 'path2', 'myfile.txt'))
print()

print("현재 폴더를 파고들어가면서 파일을 탐색합니다.")
for root, dirs, files in os.walk('.'):
    print("현재폴더:", root)

    for dir in dirs:
        print('  폴더-', dir)

    for file in files:
        print('  파일-', file)