from poker.validators import RankValidator

class FourOfAKindValidator(RankValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Four Of A Kind"
    
    def is_valid(self):
        ranks_with_three_of_a_kind = self._ranks_with_count(4)
        return len(ranks_with_three_of_a_kind) == 1 

    def valid_cards(self):
        return [card for card in self.cards if card.rank in self._ranks_with_count(4).keys()]