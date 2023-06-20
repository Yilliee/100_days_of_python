from random import randint

EASY_MODE_LIVES = 10
HARD_MODE_LIVES = 5

def select_total_lives(mode):
  if mode == "easy":
    return EASY_MODE_LIVES
  elif mode == "hard":
    return HARD_MODE_LIVES
  else: # Invalid Input
    return -1

def is_correct_answer(guess, answer):
  difference = guess - answer

  if abs(difference) > 10:
    print("Too", end=" ")

  if difference > 0:
    print("High\n")
  elif difference < 0:
    print("Low\n")

  if difference == 0:
    return True

  return False

def calculate_result(lives):
  if lives > 0:
    return "Congrats! You guessed the correct value"
  elif lives == 0:
    return "You ran out lives! Better luck next time!"
  else: # lives == - 1 # Invalid mode
    return "Invalid mode selected. Aborting..."

def number_guessing_game():
  print("Welcome to the Number Guessing Game")
  print("Ready to try your luck?")
  print("Guess the randomly choosen number between 1-100 (inclusive)")
  print("Available modes:")
  print(" • Easy")
  print(" • Hard")
  mode = input("Enter your preferred mode : ").lower()

  lives = select_total_lives(mode)

  number = randint(1, 100)

  while lives > 0:
    print(f"You have {lives} guesses left.")
    guess = int(input("Enter your guess : "))

    if guess < 1 or guess > 100:
      print("Please Enter a number between 1-100\n")
      continue

    if is_correct_answer(guess, number):
      break

    lives -= 1

  result = calculate_result(lives)
  print(result)

number_guessing_game()
