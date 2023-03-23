import time

print("for 문 실행을 1초씩 지연시킵니다.")
for i in range(5):
    print(i)
    time.sleep(1)
print()

print("실행시간을 측정합니다.")
start= time.time()
for i in range(5):
    print(i)
    time.sleep(1)
end = time.time()
print("코드실행시간: ", end-start)

