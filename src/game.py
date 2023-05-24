from deck import Deck
from player import Player

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Joueur 1")
        self.computer = Player("Ordinateur")

    def start(self):
        self.deck.shuffle()
        self.deck.deal(self.player, self.computer)

        self.player.show_hand()
        self.computer.show_hand()

       
