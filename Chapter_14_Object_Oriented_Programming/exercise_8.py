"""
Write a class that inherits from the Card_group class of this chapter. The class should represent
a deck of cards that contains only hearts and spaces, with only the cards 2 through 10
in each suit. Add a method to the class called next2 that returns the top two cards from the
deck.
"""
from random import shuffle


# Class Card_group Page 134 in "A Practical Introduction Into Python Programming"
class CardGroup:
    def __init__(self, cards=[]):
        self.cards = cards

    def next_card(self):
        return self.cards.pop(0)

    def has_card(self):
        return len(self.cards) > 0

    def size(self):
        return len(self.cards)

    def shuffle(self):
        shuffle(self.cards)


class SpecialCardGroup(CardGroup):
    def __init__(self):
        super().__init__(cards=[{'suit': s, 'value': v} for s in ['Heart', 'Space'] for v in range(2, 11)])

    def next2(self):
        if len(self.cards) > 1:
            return [self.cards.pop(0), self.cards.pop(0)]
