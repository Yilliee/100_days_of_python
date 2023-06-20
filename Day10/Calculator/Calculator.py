from art import logo
import os

def clear():
  if os.name == "posix":
    os.system("clear")
  else:
    os.system("CLS")

def add(num1, num2):
  """Add 2 numbers together"""
  return num1 + num2

def subtract(num1, num2):
  """Subtract num2 from num1"""
  return num1 - num2

def divide(num1, num2):
  """Divide num1 by num2"""
  return num1 / num2

def multiply(num1, num2):
  """Multiply num1 by num2"""
  return num1 * num2

operations = {
  '+' : add,
  '-' : subtract,
  '*' : multiply,
  '/' : divide,
}

def calculate():
  continueCalculation = True
  last_number = float(input("Enter the first number : "))
  print("Available operations : ")
  for symbol in operations:
    print(symbol, end=" ")
  print()
  
  while continueCalculation:
    operation = input("Enter the operation : ")
    
    new_number = float(input("Enter the next number : "))
    
    calc = operations[operation]
    result = calc(last_number, new_number)
   
    print(f"{last_number:.2f} {operation} {new_number:.2f} = {result:.2f}")
    
    if input(f"Type 'y' to continue calculating with {result:.2f} : ") == 'y':
      last_number = result
    else:
      continueCalculation = False

new_calculation = True
while new_calculation:
  print(logo)

  calculate()
  
  restart = input("Type 'y' to start a new Calculation, 'n' to exit...\n")
  new_calculation = restart == 'y'
  clear()
  