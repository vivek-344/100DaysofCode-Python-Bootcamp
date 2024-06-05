import os
import random

from day11_blackjack_art import logo


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
dealer_cards = []


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def start_game():
    user_cards.clear()
    dealer_cards.clear()
    clear_screen()
    print(logo)
    user_card()
    user_card()
    dealer_card()
    dealer_card()


def user_card():
    random_card = random.choice(cards)
    user_cards.append(random_card)
    if sum(user_cards) > 21:
        for i in range(len(user_cards)):
            if user_cards[i] == 11:
                user_cards[i] = 1


def dealer_card():
    random_card = random.choice(cards)
    dealer_cards.append(random_card)
    if sum(dealer_cards) > 21:
        for i in range(len(dealer_cards)):
            if dealer_cards[i] == 11:
                dealer_cards[i] = 1


def break_loop():
    if sum(user_cards) >= 21 or sum(dealer_cards) >= 21:
        return True


def winner(player_score, computer_score):
    if player_score > 21 and computer_score > 21:
        return "You busted. You lose."
    elif player_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Computer went over. You win."
    elif player_score == computer_score:
        return "You both have same score. It's a draw."
    elif player_score == 21:
        return "YOU GOT A BLACKJACK!! YOU WIN!!"
    elif computer_score == 21:
        return "Computer got blackjack. You lose."
    elif player_score > computer_score:
        return "You win."
    else:
        return "You lose."


play = input("Do you want to play blackjack? Type 'y' or 'n': ")
while play == 'y':
    start_game()
    while True:
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer's first card: {dealer_cards[0]}")
        if break_loop():
            break
        draw = input("Type 'y' to draw another card, or type 'n' to pass: ")
        if draw == 'y':
            user_card()
            if break_loop():
                break
            dealer_card()
        else:
            break
        if break_loop():
            break
    while sum(dealer_cards) < 17:
        dealer_card()
    user_score = sum(user_cards)
    dealer_score = sum(dealer_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(winner(user_score, dealer_score))
    play = input("\nPlay again? Type 'y' or 'n': ")

print("Exiting game..")
