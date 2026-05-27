import turtle
import colorsys

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.speed(0)

h=0
n=50

for i in range(300):
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=1/n
    t.color(c)
    t.circle(i,60)
    t.left(120)
    t.circle(i,60)
    t.left(60)
    t.width(i/150+1)

turtle.done()    