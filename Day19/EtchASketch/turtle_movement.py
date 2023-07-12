from turtle import Turtle, Screen

tur = Turtle()
screen = Screen()


def move_forward():
    tur.fd(10)


def move_back():
    tur.bk(10)


def turn_right():
    tur.rt(5)


def turn_left():
    tur.lt(5)


def clear_screen():
    screen.clear()
    screen.addshape("turtle")
