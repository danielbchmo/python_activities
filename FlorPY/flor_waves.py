from turtle import *
import colorsys

bgcolor('black')
tracer(2)
pensize(2)
h=0

for i in range(400):
    color = colorsys.hsv_to_rgb(h,1,1)
    h += 0.005
    pencolor(color)
    rt(120)
    circle(-i * 0.5, 120)
    circle(i * 0.5, 120)
    circle(i * 0.5, 60)

done()