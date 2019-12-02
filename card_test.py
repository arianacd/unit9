import card
import deck

my_card = card.Card(4, "spades")
print(my_card)

my_deck = deck.Deck()
my_deck.shuffle()
card_one = my_deck.deal()
print(card_one)