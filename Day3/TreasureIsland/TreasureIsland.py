#PreMade graphic from replit
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
# Welcome message
print("""
Welcome to Treasure Island.
Your mission is to find the treasure.
""")

# Start game
invalidInput = False

print('You\'re at a cross road. Where do you want to go? Type "left" or "right"')
decision = input().lower()

if decision == "left":
    print('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.')
    decision = input().lower()
    
    if decision == "wait":
        print('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?')
        decision = input().lower()

        if decision == "yellow":
            print("You found the treasure! You Win!")
        elif decision == "blue":
            print("You enter a room of beasts. Game Over.")
        elif decision == "red":
            print("It's a room full of fire. Game Over.")
        else:
            invalidInput = True
    elif decision == "swim":
        print("You get attacked by an angry trout. Game Over.")
    else:
        invalidInput = True

elif decision == "right":
    print("You fell into a hole. Game Over.")
else:
    invalidInput = True

if invalidInput:
    print("Invalid input. Aborting...")
