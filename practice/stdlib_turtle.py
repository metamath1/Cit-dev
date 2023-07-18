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

# 원점에 빨간색 점 찍기
turtle.color('red')
turtle.dot(15)
turtle.color('black')

# 뒤집어진 직각삼각형
# for y in range(0, 200, 20):
#     for x in range(0, y+20, 20):
#         turtle.penup()
#         turtle.goto(x, y)
#         turtle.pendown()
#         turtle.dot(10)

# 피라미드
# n = int(input('피라미드 층 수: '))
# for y in range(n):
#     for x in range(n-y):
#         turtle.penup()
#         turtle.goto(x*20 + (20/2)*y , y*20)
#         turtle.pendown()
#         turtle.dot(10)

def heading_right():
    # 거북이의 머리를 무조건 오른쪽(각도로 0도)로 만든다.
    cur_direction = turtle.heading()
    turtle.right(cur_direction)

# 거북이 머리 오른쪽으로 실험
print()
turtle.shape('turtle')
turtle.left(100)
c = input("현재 거북이 머리를 화면 오른쪽(동쪽)으로 두게 합니다.")
heading_right()


# 원그리기 케이스 1: 진행방향에서 반시계방향으로 전진, 진행방향 왼쪽에 원이 생김
c = input("현재 진행방향 왼쪽에 원을 전진하면서 그립니다.")
turtle.circle(100, 360)

# 원그리기 케이스 2: 진행방향에서 시계방향으로 후진, 진행방향 왼쪽에 원이 생김
c = input("현재 진행방향 왼쪽에 원을 후진하면서 그립니다.")
turtle.circle(100, -360)



# 원그리기 케이스 3: 진행방향에서 시계방향으로 전진, 진행방향 오른쪽에 원이 생김
c = input("현재 진행방향 오른쪽에 원을 전진하면서 그립니다.")
turtle.circle(-100, 360)


# 원그리기 케이스 4: 진행방향에서 반시계방향으로 후진, 진행방향 오른쪽에 원이 생김
c = input("현재 진행방향 오른쪽에 원을 후진하면서 그립니다.")
turtle.circle(-100, -360)

c = input()