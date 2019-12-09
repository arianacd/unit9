class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __gt__(self, other):
        if self.rank > other.rank:
            return True
        elif other.rank > self.rank:
            return False
        else:
            order = ["Clubs", "Diamonds", "Hearts", "Spades"]
            index_user = order.index(self.suit)
            index_dealer = order.index(other.suit)
            if index_user > index_dealer:
                return True
            else:
                return False

    def __str__(self):
        values = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                  "Jack", "Queen", "King"]
        return values[self.rank-1] + " of " + self.suit
