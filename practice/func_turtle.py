import turtle

"""
turtle.forward(distance): 현재 방향으로 distance만큼 이동
turtle.backward(distance): 현재 반대방향으로 distance만큼 이동
turtle.right(angle): 진행방향 오른쪽으로 angle만큼 회전
turtle.left(angle): 진행방향 왼쪽으로 angle만큼 회전
turtle.circle(radius, angle): 현재 지점을 기준으로 +r면 반시계방향으로 반지름 r인 원 그림
turtle.goto(x, y): x, y 좌표로 이동
turtle.dot(d): 현재 위치를 중심으로 지름 d만큼의 원을 그리고 채움
turtle.home(): 0,0 으로 이동
turtle.clear(): 그림 다 지움

turtle.color(color): 펜색 지정
turtle.penup(): 펜을 올림(이동해도 그림이 안그려짐)
turtle.pendown(): 펜을 내림(이동하면 그림이 그려짐)
"""

turtle.setup(width = 500, height = 500)

# 원점에 빨간색 점 찍기
turtle.color('red')
turtle.dot(15)
turtle.color('black')
turtle.shape('turtle')
turtle.penup()

# 뒤집어진 직각삼각형
# for y in range(0, 200, 20):
#     for x in range(0, y+20, 20):
#         turtle.penup()
#         turtle.goto(x, y)
#         turtle.pendown()
#         turtle.dot(10)

# 피라미드
# def draw_pyramid(org_x, org_y, n):
#     for y in range(n):
#         for x in range(n-y):
#             turtle.penup()
#             turtle.goto(org_x + x*20 + (20/2)*y , org_y + y*20)
#             turtle.pendown()
#             turtle.dot(10)

def draw_pyramid(org_x, org_y, n):
    w = n*2-1 

    for i in range(n):
        y = i * 20
        for j in range(w-(i*2)):
            x = j * 20

            if i == 0 and j == 0:
                turtle.color('green')
            else:
                turtle.color('black')

            turtle.goto(org_x + x+20*i, org_y + y)
            turtle.dot(10)
    turtle.home()

x = None
y = None
n = None

while True:
    print(f"\n현재 입력값: X:{x}, Y:{y}, N:{n}")
    c = input("x: 피라미드를 지을 x좌표, y: 피라미드를 지을 y좌표, n: 피라미드 층 수, q: 그만두기: ")
    
    if c == 'x':
        x = int(input('파라미드를 지을 위치의 x 좌표: '))
    elif c == 'y':
        y = int(input('파라미드를 지을 위치의 y 좌표: '))
    elif c == 'n':
        n = int(input('파라미드 층 수: '))
    elif c == 'q':
        print('종료')
        break

    if x != None and y != None and n != None:
        draw_pyramid(x, y, n)
        x = None
        y = None
        n = None
