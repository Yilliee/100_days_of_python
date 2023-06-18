from random import choice

word_list = ["aardvark", "baboon", "camel"]

chosen_word = choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = [ '_' ] * len(chosen_word)

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
while '_' in display:
  guess = input("Guess a letter: ").lower()
  if len(guess) != 1:
    print("Warning: Only the first character will be considered")
    guess = guess[:1]
  
  #Check guessed letter

  if guess in display:
    print("You already guessed this letter!")
    # Skip everything and ask for a new letter
    continue

  correct_guess = False
  for index, letter in enumerate(chosen_word):
    if letter == guess:
      display[index] = letter
      correct_guess = True

  if correct_guess:
    print("You guessed a correct letter!")
  else:
    print("You guessed an incorrect letter!")

  print(display)

print("You Win!")
