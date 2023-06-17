from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
visuals = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Valid input ?
if user_choice > 2 or user_choice < 0:
    print("Invalid input, enter a number between 0 - 2")
else:
    # Since our conditions are based on indices,
    # random.randint is used instead of random.choice
    computer_choice = randint(0, 2)

    print("\nYou chose:")
    print(visuals[user_choice])

    print("Computer chose:")
    print(visuals[computer_choice])

    is_draw = user_choice == computer_choice
    # Simplified version of Rock x Scissor, Paper x Rock, Scissor x Paper 
    user_won = user_choice == 0 and computer_choice == 2 \
                or user_choice - 1 == computer_choice

    if is_draw:
        print("It's a draw!")
    elif user_won:
        print("You win!")
    else:
        print("You lose!")