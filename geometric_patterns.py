import turtle

t = turtle.Turtle()

for _ in range(12):
    for _ in range(12):
        t.forward(100)
        t.right(144)
    t.right(10)

turtle.done()