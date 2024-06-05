import os
from day9_blind_auction_art import logo

print(logo)


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def add_bid(bidders, amount):
    bids[bidders] = amount


def declare_winner():
    highest_bid = 0
    bid_winner = ""
    for bidder in bids:
        if bids[bidder] > highest_bid:
            highest_bid = bids[bidder]
            bid_winner = bidder
    print(f"The winner is {bid_winner} with a bid of ${highest_bid}")


bids = {}
repeat = "yes"
while repeat == "yes":
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    add_bid(name, bid)
    repeat = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    clear_screen()

declare_winner()
