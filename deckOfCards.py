from random import shuffle


class Card:
    def __init__(self, face, suit):
        self.suit = suit
        self.face = face

    def __repr__(self):
        return "{} of {}".format(self.face, self.suit)


class Deck:

    def __init__(self):
        self.cards = self.construct_cards()
        shuffle(self.cards)

    def __repr__(self):
        return "Deck of {} cards".format(len(self.cards))

    def construct_cards(self):
        suits = ('Spades', "Hearts", "Diamonds", "Clubs")
        faces = ('2', '3', '4', '5', '6', '7', '8',
                 '9', '10', 'J', 'Q', 'K', 'A')
        return [Card(face, suit) for suit in suits for face in faces]

    def _deal(self, num):
        if num > len(self.cards):
            raise ValueError("There are no cards left!!!!")
        else:
            return [self.cards.pop() for i in range(num)]

    def deal_hand(self):
        return self._deal(5)


deck = Deck()
print(deck)
print(deck.deal_hand())
print(deck.cards)
print(len(deck.cards))
print(deck.deal_hand())
print(deck.deal_hand())
print(deck.deal_hand())
print(deck.deal_hand())
print(deck.deal_hand())
print(len(deck.cards))
print(deck.deal_hand())
print(deck.deal_hand())
print(deck.deal_hand())
print(deck.deal_hand())
print(deck.deal_hand())
print(len(deck.cards))
