from turtle import Turtle, Screen, colormode
from random import randint


TOTAL_TURTLES = 6
ENDPOINT_OF_SCREEN = 500

#Setup the screen
colormode(255)
screen = Screen()
screen.setworldcoordinates(llx=-50, lly=-50, urx=ENDPOINT_OF_SCREEN, ury=50 * TOTAL_TURTLES)

turtles = [Turtle(shape="turtle") for _ in range(TOTAL_TURTLES)]
for i in range(TOTAL_TURTLES):
    # turtles[i].speed("fast")
    turtles[i].color(randint(0, 255), randint(0, 255), randint(0, 255))
    turtles[i].penup()
    turtles[i].sety(i * 50)


user_guess = int(screen.numinput(title="Make a guess of the winner", default=1, minval=1, maxval=TOTAL_TURTLES,
                                 prompt=f"Guess which numbered turtle from the bottom will win the race?"
                                       f" (Turtle Number : 1-{TOTAL_TURTLES})"))

game_completed = False
winner_turtle = -1

while not game_completed:
    for i in range(TOTAL_TURTLES):
        turtles[i].forward(randint(5, 20))
        if turtles[i].xcor() >= ENDPOINT_OF_SCREEN:
            winner_turtle = i
            game_completed = True
            break

if winner_turtle + 1 == int(user_guess):
    print("Congrats! Your selected turtle won!")
else:
    print("Alas! Your selected turtle did not win!")

print(f"Winner : Turtle No. {winner_turtle + 1}")
