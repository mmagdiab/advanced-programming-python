"""
Use the Standard_deck class of this section to create a simplified version of the game War.
In this game, there are two players. Each starts with half of a deck. The players each deal
the top card from their decks and whoever has the higher card wins the other player’s cards
and adds them to the bottom of his deck. If there is a tie, the two cards are eliminated from
play (this differs from the actual game, but is simpler to program). The game ends when one
player runs out of cards.
"""
from random import shuffle


# Class Card Page 133 in "A Practical Introduction Into Python Programming"
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        names = ['Jack', 'Queen', 'King', 'Ace']
        if self.value <= 10:
            return '{} of {}'.format(self.value, self.suit)
        else:
            return '{} of {}'.format(names[self.value - 11], self.suit)


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


# Class Standard_deck Page 134 in "A Practical Introduction Into Python Programming"
class StandardDeck(CardGroup):
    def __init__(self):
        self.cards = []
        for s in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for v in range(2, 15):
                self.cards.append(Card(v, s))


class GameWar:
    def __init__(self):
        deck = StandardDeck()
        deck.shuffle()
        self.player1_cards = []
        self.player2_cards = []
        while len(deck.cards) > 0:
            self.player1_cards.append(deck.cards.pop(0))
            self.player2_cards.append(deck.cards.pop(0))

    def start(self):
        while len(self.player1_cards) > 0 and len(self.player2_cards) > 0:
            if self.player1_cards[0].value > self.player2_cards[0].value:
                self.player1_cards.append(self.player2_cards.pop(0))
            elif self.player1_cards[0].value < self.player2_cards[0].value:
                self.player2_cards.append(self.player1_cards.pop(0))
            else:
                self.player1_cards.pop(0)
                self.player2_cards.pop(0)

        if self.player1_cards is []:
            print("The winner is player 2")
        else:
            print("The winner is player 1")
