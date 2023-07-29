from dataclasses import dataclass
from enum import Enum
from itertools import product, combinations
from random import sample
from collections import Counter

class Color(Enum):
    RED = 1
    GREEN = 2
    PURPLE = 3

class Fill(Enum):
    FILLED = 1
    STRIPES = 2
    EMPTY = 3

class Shape(Enum):
    SQUIGGLE = 1
    CAPSULE = 2
    DIAMOND = 3

class Count(Enum):
    ONE = 1
    TWO = 2
    THREE = 3

attributes = [("shape", Shape), ("fill", Fill), ("color", Color), ("count", Count)]

@dataclass
class SetCard():
    shape: Shape
    color: Color
    fill: Fill
    count: Count

    def get_different_or_same(self, other, property):
        ours = getattr(self, property)
        theirs = getattr(other,property)
        if ours == theirs:
            return "same"
        else:
            return "different"
    
    def get_third_card(self, other):
        def get_card_from_dict(da_dict):
            card = SetCard(Shape.CAPSULE, Color.GREEN, Fill.EMPTY, Count.ONE)
            for key in da_dict:
                setattr(card, key, da_dict[key])
            return card

        new_card = {}
        for property_name, property in attributes:
            if self.get_different_or_same(other, property_name) == "same":
                new_card[property_name] = getattr(self, property_name)
            else:
                ours = getattr(self, property_name)
                theirs = getattr(other,property_name)
                diffs = set()
                diffs.add(ours)
                diffs.add(theirs)
                new_card[property_name] = list(set(property) - diffs)[0]
        return get_card_from_dict(new_card)



def generate_all_cards():
    for shape, fill, color, count in product(list(Shape), list(Fill), list(Color), list(Count)):
        yield SetCard(shape, color, fill, count)

def run():
    all_cards = generate_all_cards()
    board = sample(list(all_cards), 12)
    count = 0
    for card1, card2 in combinations(board, 2):
        card3 = card1.get_third_card(card2)
        if card3 in board:
            count += 1
    return count // 3

def get_percentages(da_counter):
    percentages = {}
    total = sum(da_counter.values())
    for key in da_counter:
        percentages[key] = da_counter[key] / total
    return dict(sorted(percentages.items()))

if __name__ == '__main__':
    # card1 = SetCard(Shape.CAPSULE, Color.RED, Fill.FILLED, Count.TWO)
    # card2 = SetCard(Shape.CAPSULE, Color.RED, Fill.FILLED, Count.ONE)
    # print(card1.get_third_card(card2))
    # print(card1)
    # print(card2)
    # print(card1.get_different_or_same(card2, "shape"))
    
    c = Counter()
    for i in range(10000):
        sets = run()
        c[sets] += 1
    print(c)
    print(get_percentages(c))
