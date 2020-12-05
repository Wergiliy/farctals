import turtle
turtle.hideturtle()
#turtle.speed(0)
turtle.tracer(0)
turtle.penup()
turtle.setposition(-400, -400)
turtle.pendown()
turtle.pensize(2)

axiom = "A"
axmTemp = ""
itr = 9
dl = 2
angl = 60

translate={"+":"+", "-":"-", "A":"B-A-B", "B":"A+B+A"}

for k in range(itr):
    for c in axiom:
        axmTemp +=translate[c]
    axiom = axmTemp
    axmTemp = ''


for ch in axiom:
    if ch == '+':
        turtle.right(60)
    elif ch == '-':
        turtle.left(60)
    else:
        turtle.forward(dl)

turtle.update()
turtle.mainloop()