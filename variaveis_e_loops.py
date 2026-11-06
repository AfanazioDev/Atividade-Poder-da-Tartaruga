from turtle import *
speed(11)
shape("turtle")

lados = 4
angulo = 360 / lados

for count in range(lados):
    forward(100)
    right(angulo)

done()
