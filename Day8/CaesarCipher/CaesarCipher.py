from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(input_msg, shift_amount, operation_type):
  is_encode = operation_type == "encode"
  is_decode = operation_type == "decode"
  if not (is_decode or is_encode):
    print("Only decode and encode operations are supported")
    return

  if is_decode:
    shift_amount *= -1

  total_alphabets = len(alphabet)
  new_message = ""
  for character in input_msg:
    if character not in alphabet:
      new_message += character
      continue

    new_index = alphabet.index(character) + shift_amount
    new_index %= total_alphabets
    new_message += alphabet[new_index]

  print(f"The {operation_type}d text is {new_message}")


print(logo)

restart_program = True
while restart_program:
  direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  if shift < 0:
    print("Warning! The absolute value of shift will be used.")
    shift = abs(shift)

  caesar(input_msg=text, shift_amount=shift, operation_type=direction)

  want_to_restart = input("Enter yes to restart the program. Otherwise enter no or any other thing.\n").lower()
  restart_program = want_to_restart == "yes"

print("Goodbye.\n")
