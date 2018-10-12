"""
Module for creating card games. Simple framework for a deck of cards and it's functions
"""

import random

class deck:
    def __init__(self, suits = ['hearts', 'spades', 'diamonds', 'clubs'], numbers = ['1','2','3','4','5','6','7','8','9','10','j','q','k']):
        self.suits = suits 
        self.numbers = numbers
        self.cards = []
        for x in range(len(self.suits)):
            for y in range(len(self.numbers)):
                self.cards.append([self.numbers[y], self.suits[x]])

    def draw(self):
        choice = random.randint(0, len(self.cards)-1)
        card = self.cards[choice]
        self.cards.remove(card)
        return card

    def remove_card(self, card):
        try:
            self.cards.remove(card)
            return True
        except:
            return False

    def shuffle(self):
        temp_cards = self.cards
        self.cards = []
        for x in range(len(temp_cards)):
            choice = random.randint(0, len(temp_cards)-1)
            self.cards.append(temp_cards[choice])
            temp_cards.remove(temp_cards[choice])
        return True
