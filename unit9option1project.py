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
        return True
    elif user_card < dealer_card:
        print("the dealer wins!")
        return False


def main():
    my_deck = deck.Deck()
    my_deck.shuffle()
    user_deal = deal_cards(my_deck)
    dealer_deal = deal_cards(my_deck)
    user_score = 0
    dealer_score = 0
    for x in range(5):
        print("the user has", user_deal[x])
        print("the dealer has", dealer_deal[x])
        if compare_cards(user_deal[x], dealer_deal[x]):
            user_score += 1
        else:
            dealer_score += 1
        print("")
        print("the final score is user:", user_score, "and dealer:", dealer_score)



main()

