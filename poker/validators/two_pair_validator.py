from poker.validators import RankValidator

class TwoPairValidator(RankValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Two Pair"

    def is_valid(self):
        ranks_with_pair = self._ranks_with_count(2)
        return len(ranks_with_pair) >= 2 

    def valid_cards(self):
        return [card for card in self.cards if card.rank in self._ranks_with_count(2).keys()]