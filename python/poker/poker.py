from collections import Counter

# hand ranks
STRAIGHT_FLUSH = 1
FOUR_OF_A_KIND = 2
FULL_HOUSE = 3
FLUSH = 4
STRAIGHT = 5
THREE_OF_A_KIND = 6
TWO_PAIR = 7
ONE_PAIR = 8
NADA = 9

def best_hands(hands):
    if len(hands) == 1:
        return hands

    hand_ranks = []
    clean_hands = []
    for h in hands:
        clean_hand = get_clean_hand(h)
        clean_hands.append(clean_hand)
        hand_rank = get_hand_rank(clean_hand)
        hand_ranks.append(hand_rank)

    winner = min(hand_ranks)
    if hand_ranks.count(winner) == 1:
        return [hands[hand_ranks.index(winner)]]

    # All NADA hands
    print(hand_ranks)
    print(clean_hands)
    if winner == 9:
        largest_cards = [int(x[-1][:-1]) for x in clean_hands]
        max_card = max(largest_cards)

        # tie breaker???
        if largest_cards.count(max_card) > 1:
            max_card_tie = [i for i, m in enumerate(largest_cards) if m == max_card]
            print(max_card_tie)
        print(largest_cards)
        return [hands[largest_cards.index(max(largest_cards))]]

    return hand_ranks

# def get_highest_card(cards):




def get_clean_hand(hand):
    cleaned = hand.replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14')
    return sorted(cleaned.split(), key=lambda x: int(x[:-1]))

def get_hand_rank(hand):
    vals = [int(x[:-1]) for x in hand]
    suits = [x[-1] for x in hand]
    val_count = Counter(vals).values()

    # check straight flush or straight
    consecutive_vals = list(range(min(vals), min(vals) + 5))
    if consecutive_vals == vals:
        if suits == [suits[0]] * 5:
            return STRAIGHT_FLUSH
        return STRAIGHT

    # check four of a kind
    if 4 in val_count:
        return FOUR_OF_A_KIND

    # check full house or three of a kind
    if 3 in val_count:
        if 2 in val_count:
            return FULL_HOUSE
        return THREE_OF_A_KIND

    # check flush
    if suits == [suits[0]] * 5:
        return FLUSH

    # check for pairs
    if 2 in val_count:
        if list(val_count).count(2) == 2:
            return TWO_PAIR
        return ONE_PAIR

    # if no hand
    return NADA


hands1 = [
    "4D 5S 6S 8D 3C",
    "2S 4C 7S 9H 10H",
    "3S 4S 5D 6H JH",
    "3H 4H 5C 6C JD",
]

print(best_hands(hands1), '\n')
