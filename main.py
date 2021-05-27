'''
Game will be automatically played by two players.

The goal is to be the first player to win all 52 cards.

Card rank are as follows:

2, 3, 4, 5, 6, 7, 8, 9, 10, Jack(11), Queen(12), King(13), Ace(14)

Please the document README.md for the rules of the game.
'''

import random

# LIST THAT MAKES UP A FULL DECK OF CARDS
suits_list = ('Spades', 'Clubs', 'Hearts', 'Diamonds')
values_list = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
ranks_list = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


# CREATING A SINGLE CARD TYPE
class CardType:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values_list[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# print(suits_list[0])
# random_card = CardType(suits_list[0], ranks_list[0])
# print(random_card)


# CREATING THE DECK, SHUFFLE, AND DEALING ONE CARD.
class Deck:

    def __init__(self):
        # Creates a new deck of cards
        self.all_cards = []
        for suit in suits_list:
            for rank in ranks_list:
                self.all_cards.append(CardType(suit, rank))

    def deal_one(self):
        # Removes one card from the top
        return self.all_cards.pop

    def shuffle_deck(self):
        # Shuffles the deck
        random.shuffle(self.all_cards)


# CREATES THE PLAYERS FOR THE GAME
class Players:

    def __init__(self, player):
        self.player = player
        self.all_cards = []

    def add_card(self, new_card):
        if type(new_card) == type([]):
            self.all_cards.extend(new_card)
        else:
            self.all_cards.append(new_card)

    def remove_one(self):
        # index 0 is the top of the deck and -1 is the bottom of the deck.
        return self.all_cards.pop(0)

    def __str__(self):
        return f"Player {self.player} has {len(self.all_cards)} cards. "


# TWO PLAYERS
first_player = Players('One')
second_player = Players('Two')

# SETUP NEW GAME
new_deck = Deck()
new


