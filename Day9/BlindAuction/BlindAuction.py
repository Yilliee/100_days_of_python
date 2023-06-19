from art import logo
import os

def clear():
    if os.name == "posix":
        os.system("clear")
    else:  # Windows
        os.system("cls")

def print_bid_winner(bid_records):
  max_bidder_name = ""
  max_bid = 0
  for bidder, bid in bid_records.items():
  
    if bid > max_bid:
      max_bid = bid
      max_bidder_name = bidder
  
  print(f"The winner is {max_bidder_name} with a bid of ${max_bid}")

def take_new_bid(bid_records):
  bidder_name = input("What is your name?: ")
  bid_amount = int(input("What's your bid?: $"))

  bid_records[bidder_name] = bid_amount

# Start of main program
print(logo)
print("Welcome to the secret auction program.")

bid_records = {}
continue_bidding = True

while continue_bidding:
    take_new_bid(bid_records)

    should_continue = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    continue_bidding = should_continue == "yes"

    clear()

print_bid_winner(bid_records)