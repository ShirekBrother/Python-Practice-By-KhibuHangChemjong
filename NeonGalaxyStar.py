import turtle
import colorsys

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.speed(0)

h=0
n=80
for i in range(220):
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=1/n
    t.color(c)
    t.forward(i*3)
    t.left(155)
    t.forward(i)
    t.left(45)

    t.width(i/100+1)

turtle.done()    