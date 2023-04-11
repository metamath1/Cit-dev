import turtle as t

t.setup(width = 500, height = 500)
t.color('red')
t.dot(20)
t.color('black')
t.penup()

# double for version
n = 5
w = n*2-1 

for i in range(n):
    y = i * 20
    for j in range(w-(i*2)):
        x = j * 20
        t.goto(x+20*i, y)
        t.dot(10)
    
c = input()