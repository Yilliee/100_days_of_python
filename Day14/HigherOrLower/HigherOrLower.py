from art import logo, vs
from game_data import data
from random import choice
import os

def get_new_page(old_page = None):
  """Get's a new page's details from the game_data.data
     list. Makes sure it's not same as old_page if passed"""
  new_page = choice(data)

  if old_page is None:
    return new_page

  # Get a new page until both are different
  while new_page == old_page:
    new_page = choice(data)

  return new_page

def verify_guess(data_A, data_B):
  """Asks the user for a guess and then returns whether
     it's correct or not. Returns None on invalid input"""
  guess = input(f"Who has more followers? Type 'A' or 'B' : ")

  key = 'follower_count'
  guess_is_A = guess == 'A'
  guess_is_B = guess == 'B'
  A_is_greater = data_A[key] > data_B[key]

  if not (guess_is_A or guess_is_B):
    return

  if guess_is_A and A_is_greater or \
     guess_is_B and not A_is_greater:
    return True

  return False

def format_details(page):
  """Returns the details of the page, formatted
     into a string"""
  return f"{page['name']}, a {page['description']}, from {page['country']}"

def clear():
  """Uses os module to clear screen according
     to the underlying os"""
  if os.name == "posix":
    os.system("clear")
  else:
    os.system("CLS")

def higher_or_lower():
  """The main game"""
  score = 0

  page_A = get_new_page()
  page_B = get_new_page()

  correct_guess = True

  while correct_guess or correct_guess is None:
    clear()
    print(logo)

    if correct_guess is None:
      print("Invalid Guess, Retry..")
    elif score > 0:
      print(f"You are Correct! Current Score : {score}")

    print(f"Compare A: {format_details(page_A)}")
    print(vs)
    print(f"Against B: {format_details(page_B)}")

    correct_guess = verify_guess(page_A, page_B)

    if correct_guess:
      score += 1
      page_A = page_B
      page_B = get_new_page(page_A)

  clear()
  print(logo)
  print(f"Sorry, that's Wrong. Final Score : {score}")

higher_or_lower()
