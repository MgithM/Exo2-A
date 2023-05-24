import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.generate_deck()

    def generate_deck(self):
        suits = ["Coeur", "Carreau", "Trèfle", "Pique"]
        ranks = ["As", "Roi", "Dame", "Valet", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, *players):
        num_cards = 5 

        for _ in range(num_cards):
            for player in players:
                card = self.cards.pop(0)
                player.add_card(card)
