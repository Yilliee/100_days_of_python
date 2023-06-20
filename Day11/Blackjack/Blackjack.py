from art import logo
from random import choice
import os

deck = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'K': 10, 'Q': 10}
deck_cards = list(deck.keys())
blackjack_score = 21
min_dealer_score = 17

def clear():
  """Clear the teminal's screen"""
  if os.name == "posix":
    os.system("clear")
  else:
    os.system("CLS")

def start_new_game():
  """Returns a bool based on user's response to a prompt
     asking if they'd like to start a new game"""
  new_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  return new_game == 'y'

def take_new_card():
  """Returns a bool based on user's response to a prompt
     asking if they'd like to draw another card"""
  take_card = input("Type 'y' to get another card, type 'n' to pass: ")
  return take_card == 'y'

def draw_cards(no_of_cards):
  """Returns a list of provided number of randomly
     drawn cards from the deck"""
  new_cards = []
  for i in range(no_of_cards):
    new_cards.append(choice(deck_cards))

  return new_cards

def calculate_score(cards):
  """Calculate the total score of provided a list
     of cards by using values in deck dictionary"""
  total_score = 0
  for card in cards:
    total_score += deck[card]

  if total_score > 21 and 'A' in cards:
    total_score -= 10

  return total_score

def get_result(user_score, user_cards, computer_score, computer_cards):
  """Prints who won the game based on provided score of player and dealer"""
  user_busted = user_score > blackjack_score
  computer_busted = computer_score > blackjack_score

  if user_busted and computer_busted or user_score == computer_score:
    return "It's a push."
  if user_busted:
    return "You got busted! You Lose!!"
  if computer_busted:
    return "Computer got busted! You Win!!"
  if user_score == blackjack_score and user_cards == 2:
    return "You got a blackjack! You Win!!"
  if computer_score == blackjack_score and computer_cards == 2:
    return "Computer got a blackjack! You Lose!!"
  if user_score > computer_score:
    return "You have a greater score. You Win!"
  if computer_score > user_score:
    return "Computer has a greater score. You Lose!"

def blackjack():
  """The actual blackjack game"""
  print(logo)

  user_cards = draw_cards(2)
  user_score = calculate_score(user_cards)
  computer_cards = draw_cards(2)
  computer_score = calculate_score(computer_cards)

  print(f"  Your cards: {user_cards}, current score: {user_score}")
  print(f"  Computer's first card: {computer_cards[0]}\n")

  while user_score < blackjack_score and take_new_card():
    user_cards += draw_cards(1)
    user_score = calculate_score(user_cards)

    print(f"  Your cards: {user_cards}, current score: {user_score}")
    print(f"  Computer's first card: {computer_cards[0]}\n")

  while computer_score < min_dealer_score:
    computer_cards += draw_cards(1)
    computer_score = calculate_score(computer_cards)

  print(f"  Your final hand: {user_cards}, final score: {user_score}")
  print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}\n")

  result = get_result(user_score, len(user_cards), computer_score, len(computer_cards))
  print(f"Result : {result}\n")

while start_new_game():
  clear()
  blackjack()