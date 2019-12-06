# by ariana daney
# last modified december 5, 2019
# unit 9 option 1 - this program creates a small game of war that the user can play

import card
import deck


def deal_cards(my_deck):
    user_cards = []
    for x in range(5):
        user_card = my_deck.deal()
        user_cards.append(user_card)
    return user_cards


def compare_cards(user_card, dealer_card):
    if user_card > dealer_card:
        print("the user wins")
    elif user_card < dealer_card:
        print("the dealer wins!")
    else:
        print("its a tie!")


def main():
    my_deck = deck.Deck()
    my_deck.shuffle()
    user_deal = deal_cards(my_deck)
    dealer_deal = deal_cards(my_deck)


main()

