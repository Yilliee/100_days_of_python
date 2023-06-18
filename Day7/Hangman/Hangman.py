from hangman_words import word_list
from hangman_art import logo, stages
from random import choice
import os

chosen_word = choice(word_list)

end_of_game = False
lives = len(stages) - 1

display = [ '_' ] * len(chosen_word)
wrong_answers = []

print(logo)
print(f"{' '.join(display)}")
print(stages[lives])

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if len(guess) > 1:
        print("Warning: Only the first character will be considered")
        guess = guess[:1]

    # Clear screen after every input
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


    if not guess.isalpha():
        print("Only letters are allowed!")
    elif ( guess in display ) or ( guess in wrong_answers ):
        print(f"You've already guessed {guess}!")
    elif not guess in chosen_word:
        wrong_answers.append(guess)

        lives -= 1
        print(f"{guess} is not part of the word!")

        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was {chosen_word}")
    else:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = letter

        # Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")
  
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
  
    print(stages[lives])
