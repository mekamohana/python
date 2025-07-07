#turtle design2
import turtle
t=turtle.Turtle()
t.speed(-4)
t.pensize(2)
turtle.bgcolor('black')
color=('red','yellow')
for i in range(300):
   t.color(color[i%2])
   t.goto(0,0)
   t.fd(i)
   t.circle(44,30)
   t.rt(40)
turtle.done()