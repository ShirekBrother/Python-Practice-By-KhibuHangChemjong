import turtle
import colorsys

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.speed(0)
turtle.tracer(2,0)

h=0.5
n=120
for i in range(360):
    c=colorsys.hsv_to_rgb(h,0.9,1)
    h+=1/n
    t.color(c)
    t.forward(i)
    t.circle(i*0.5,90)
    t.left(179)
    t.forward(i*0.2)

    t.width(i/200+1)

turtle.done()