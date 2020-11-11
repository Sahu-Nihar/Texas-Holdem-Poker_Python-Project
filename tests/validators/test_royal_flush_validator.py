import unittest

from poker.card import Card
from poker.validators import RoyalFlushValidator

class RoyalFlushValidatorTest(unittest.TestCase):
    def setUp(self):
        self.ten_of_clubs = Card(rank = "10", suit = "Clubs")
        self.jack_of_clubs = Card(rank = "Jack", suit = "Clubs")
        self.queen_of_clubs = Card(rank = "Queen", suit = "Clubs")
        self.king_of_clubs = Card(rank = "King", suit = "Clubs")
        self.ace_of_clubs = Card(rank = "Ace", suit = "Clubs")

        self.cards = [
            Card(rank = "2", suit = "Spades"),
            self.ten_of_clubs,
            self.jack_of_clubs,
            self.queen_of_clubs,
            self.king_of_clubs,
            self.ace_of_clubs,
            Card(rank = "Ace", suit = "Diamonds") 
        ]
    
    def test_validates_cards_have_royal_flush(self):
        validator = RoyalFlushValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_five_straight_cards_with_same_rank_ending_in_ace(self):
        validator = RoyalFlushValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.ten_of_clubs,
                self.jack_of_clubs,
                self.queen_of_clubs,
                self.king_of_clubs,
                self.ace_of_clubs
            ]
        )