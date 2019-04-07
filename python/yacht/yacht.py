from collections import Counter

# Score categories
# Change the values as you see fit
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    dice_count = Counter(dice)

    if category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
        return category * dice_count[category]

    if (category == FULL_HOUSE and sorted(list(dice_count.values())) == [2, 3]) or category == CHOICE:
        return sum(dice)

    if category == FOUR_OF_A_KIND:
        if sorted(list(dice_count.values())) == [1, 4]:
            return sum(dice) - list(dice_count.keys())[list(dice_count.values()).index(1)]
        if list(dice_count.values()) == [5]:
            return 4 * dice[0]
        return 0

    if (category == LITTLE_STRAIGHT and sorted(dice) == [1, 2, 3, 4, 5]
            or category == BIG_STRAIGHT and sorted(dice) == [2, 3, 4, 5, 6]):
        return 30

    if category == YACHT and list(dice_count.values()) == [5]:
        return 50

    return 0