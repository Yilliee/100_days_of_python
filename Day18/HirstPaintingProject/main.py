from turtle import Turtle, Screen, colormode
from random import choice

# import colorgram
#
# colors_from_img = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colorgram.extract("image.jpg", 30)]

colors_from_img = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162),
                   (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157),
                   (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166),
                   (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188),
                   (34, 151, 210), (65, 66, 56)]

screen = Screen()
screen.setworldcoordinates(0, -50, 550, 500)

tur = Turtle()
tur.penup()
tur.speed("fastest")
colormode(255)

dot_size = 20
space = 50
length, width = 10, 10
start_x, start_y = tur.position()

for i in range(length):
    tur.setposition(start_x, start_y + space * i)
    for j in range(width):
        tur.color(choice(colors_from_img))
        tur.forward(space)
        tur.dot(dot_size)

screen.exitonclick()
