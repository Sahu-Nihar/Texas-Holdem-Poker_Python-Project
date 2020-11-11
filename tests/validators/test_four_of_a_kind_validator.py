import unittest

from poker.card import Card
from poker.validators import FourOfAKindValidator

class FourOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        self.three_of_clubs = Card(rank = "3", suit = "Clubs")
        self.three_of_diamonds = Card(rank = "3", suit = "Diamonds")
        self.three_of_hearts = Card(rank = "3", suit = "Hearts")
        self.three_of_spades = Card(rank = "3", suit = "Spades")

        self.cards = [
            Card(rank = "2", suit = "Clubs"),
            self.three_of_clubs,
            self.three_of_diamonds,
            self.three_of_hearts,
            self.three_of_spades,
            Card(rank = "7", suit = "Hearts"),
            Card(rank = "9", suit = "Spades")
        ]
    
    def test_validates_that_four_cards_have_one_rank(self):
        validator = FourOfAKindValidator(cards = self.cards)
        
        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_four_cards_with_same_rank_from_collection(self):
        validator = FourOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.three_of_clubs,
                self.three_of_diamonds,
                self.three_of_hearts,
                self.three_of_spades
            ]
        )