import unittest

from poker.card import Card
from poker.validators import ThreeOfAKindValidator

class ThreeOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        five_of_clubs = Card(rank = "5", suit = "Clubs")
        self.king_of_clubs = Card(rank = "King", suit = "Clubs")
        self.king_of_diamonds = Card(rank = "King", suit = "Diamonds")
        self.king_of_hearts = Card(rank = "King", suit = "Hearts")
        ace_of_spades = Card(rank = "Ace", suit = "Spades")

        self.cards = [
            five_of_clubs,
            self.king_of_clubs,
            self.king_of_diamonds,
            self.king_of_hearts,
            ace_of_spades
        ]

    def test_validates_that_cards_have_three_of_a_kind(self):
        validator = ThreeOfAKindValidator(cards = self.cards)
        
        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_collection_of_cards_that_have_three_of_a_kind(self):
        validator = ThreeOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.king_of_clubs, 
                self.king_of_diamonds, 
                self.king_of_hearts
            ]
        )