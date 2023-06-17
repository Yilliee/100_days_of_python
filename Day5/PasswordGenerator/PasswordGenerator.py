import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
ordered_password = ""
max_letter_index = len(letters) - 1
max_number_index = len(numbers) - 1
max_symbol_index = len(symbols) - 1

for i in range(nr_letters):
    ordered_password += random.choice(letters)
for i in range(nr_symbols):
    ordered_password += random.choice(symbols)
for i in range(nr_numbers):
    ordered_password += random.choice(numbers)

print(f"Your random ordered password is : {ordered_password}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Personal Attempt # 1

unordered_password = ""
total_length = nr_letters + nr_symbols + nr_numbers
remaining_characters = [nr_letters, nr_symbols, nr_numbers]
total_characters = [letters, symbols, numbers]
type_of_characters = len(total_characters)

for index in range(total_length):
    type = random.randint(0, type_of_characters - 1)
    
    unordered_password += random.choice(total_characters[type])
    
    remaining_characters[type] -= 1

    if remaining_characters[type] == 0:
        total_characters.pop(type)
        type_of_characters -= 1


print(f"Your random unordered password is : {unordered_password}")