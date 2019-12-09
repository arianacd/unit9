# by ariana daney
# last modified december 9, 2019
# unit 9 option 1 - this program creates a small game of war that the user can play


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


def main():
    my_deck = deck.Deck()
    my_deck.shuffle()
    user_deal = deal_cards(my_deck)
    print("The user has the cards:")
    for y in user_deal:
        print(y)
    dealer_deal = deal_cards(my_deck)
    print("")
    print("The dealer has the cards:")
    for z in dealer_deal:
        print(z)
    print("")
    for x in range(5):
        compare_cards(user_deal[x], dealer_deal[x])


main()

