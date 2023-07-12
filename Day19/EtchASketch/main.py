from turtle import Turtle, Screen
# All our functions used for moving the turtle
import turtle_movement as tm

# Actual Controls
tm.screen.listen()
tm.screen.onkey(fun=tm.move_forward, key="w")
tm.screen.onkey(fun=tm.turn_left, key="a")
tm.screen.onkey(fun=tm.move_back, key="s")
tm.screen.onkey(fun=tm.turn_right, key="d")
tm.screen.onkey(fun=tm.screen.resetscreen, key="c")
tm.screen.exitonclick()
