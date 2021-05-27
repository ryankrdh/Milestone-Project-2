'''
Game will be automatically played by two players.

The goal is to be the first player to win all 52 cards.

Card rank are as follows:

2, 3, 4, 5, 6, 7, 8, 9, 10, Jack(11), Queen(12), King(13), Ace(14)

Please the document README.md for the rules of the game.
'''

import random
import pdb


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
        return self.all_cards.pop()

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
new_deck.shuffle_deck()

# SPLITTING THE DECK BETWEEN TWO PLAYERS
# I'm using the number 26 because 52/2.
for num in range(26):
    first_player.add_card(new_deck.deal_one())
    second_player.add_card(new_deck.deal_one())


# Gameplay
game_on = True
game_round = 0
while game_on:

    game_round += 1
    print(f"Round {game_round}")

    # Win check
    if len(first_player.all_cards) == 0:
        print("Player One has no more cards. Game over. \nPlayer Two wins!")
        game_on = False
        break

    if len(second_player.all_cards) == 0:
        print("Player Second has no more cards. Game over. \nPlayer One wins!")
        game_on = False
        break

    # New round and resets current cards on the table
    first_player_cards = []
    first_player_cards.append(first_player.remove_one())

    second_player_cards = []
    second_player_cards.append(second_player.remove_one())

    play_round = True

    while play_round:

        if first_player_cards[-1].value > second_player_cards[-1].value:
            # Player one wins the round
            first_player.add_card(first_player_cards)
            first_player.add_card(second_player_cards)

            # On to the next round
            play_round = False

        elif first_player_cards[-1].value < second_player_cards[-1].value:
            # Player two wins the round
            second_player.add_card(first_player_cards)
            second_player.add_card(second_player_cards)

            # On to the next round
            play_round = False

        else:
            # When the cards played by the players are equal.
            # Each player will draw 5 more cards and compare the ranks of the last drawn card.
            # If player doesn't have enough cards, game will end.
            print("WAR!")

            if len(first_player.all_cards) < 5:
                print("Player One does not have enough cards to play WAR! GAME OVER AT WAR!")
                print("Player Two WINS!")
                game_on = False
                break

            elif len(second_player.all_cards) < 5:
                print("Player Two does not have enough cards to play WAR! GAME OVER AT WAR!")
                print("Player One WINS!")
                game_on = False
                break

            # Still at war, add next cards

            else:
                for num in range(5):
                    first_player_cards.append(first_player.remove_one())
                    second_player_cards.append(second_player.remove_one())
