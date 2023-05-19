import turtle as t

t.setup(width = 500, height = 500)
t.color('red')
t.dot(20)
t.color('black')
t.penup()

# double for version
n = 5

for i in range(n):
    y = i * 20
    for j in range(n-i):
        x = j*20
        t.goto(x, y)    
        t.dot(10)

c = input()