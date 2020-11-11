from poker.validators import FiveCardRankInARowValidator

class StraightValidator(FiveCardRankInARowValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Staright"

    def is_valid(self):
        return len(self._collections_of_five_straight_cards_in_a_row) >= 1

    def valid_cards(self):
        return self._collections_of_five_straight_cards_in_a_row[-1]