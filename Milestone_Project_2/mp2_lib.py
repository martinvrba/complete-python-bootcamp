"""
Library for Milestone Project 2
"""


def ascii_hand(hand, hole=True):
    if len(hand) == 0:
        ascii_hand = [""] * 4
    if len(hand) == 1:
        ascii_hand = [
            ",---,",
            f"|{hand[0][0]}|",
            f"|{hand[0][1]}|",
            "'---'"
        ]
    if len(hand) == 2:
        if not hole:
            ascii_hand = [
                ",---,  " * 2,
                f"|{hand[0][0]}|  |   |  ",
                f"|{hand[0][1]}|  |   |  ",
                "'---'  " * 2
            ]
        else:
            ascii_hand = [
                ",---,  " * 2,
                f"|{hand[0][0]}|  |{hand[1][0]}|  ",
                f"|{hand[0][1]}|  |{hand[1][1]}|  ",
                "'---'  " * 2
            ]
    if len(hand) == 3:
        ascii_hand = [
            ",---,  " * 3,
            f"|{hand[0][0]}|  |{hand[1][0]}|  |{hand[2][0]}|  ",
            f"|{hand[0][1]}|  |{hand[1][1]}|  |{hand[2][1]}|  ",
            "'---'  " * 3
        ]
    if len(hand) == 4:
        ascii_hand = [
            ",---,  " * 4,
            (
                f"|{hand[0][0]}|  |{hand[1][0]}|  |{hand[2][0]}|  "
                f"|{hand[3][0]}|  "
            ),
            (
                f"|{hand[0][1]}|  |{hand[1][1]}|  |{hand[2][1]}|  "
                f"|{hand[3][1]}|  "
            ),
            "'---'  " * 4
        ]
    if len(hand) == 5:
        ascii_hand = [
            ",---,  " * 5,
            (
                f"|{hand[0][0]}|  |{hand[1][0]}|  |{hand[2][0]}|  "
                f"|{hand[3][0]}|  |{hand[4][0]}|  "
            ),
            (
                f"|{hand[0][1]}|  |{hand[1][1]}|  |{hand[2][1]}|  "
                f"|{hand[3][1]}|  |{hand[4][1]}|  "
            ),
            "'---'  " * 5
        ]
    if len(hand) == 6:
        ascii_hand = [
            ",---,  " * 6,
            (
                f"|{hand[0][0]}|  |{hand[1][0]}|  |{hand[2][0]}|  "
                f"|{hand[3][0]}|  |{hand[4][0]}|  |{hand[5][0]}|  "
            ),
            (
                f"|{hand[0][1]}|  |{hand[1][1]}|  |{hand[2][1]}|  "
                f"|{hand[3][1]}|  |{hand[4][1]}|  |{hand[5][1]}|  "
            ),
            "'---'  " * 6
        ]
    if len(hand) == 7:
        ascii_hand = [
            ",---,  " * 7,
            (
                f"|{hand[0][0]}|  |{hand[1][0]}|  |{hand[2][0]}|  "
                f"|{hand[3][0]}|  |{hand[4][0]}|  |{hand[5][0]}|  "
                f"|{hand[6][0]}|  "
            ),
            (
                f"|{hand[0][1]}|  |{hand[1][1]}|  |{hand[2][1]}|  "
                f"|{hand[3][1]}|  |{hand[4][1]}|  |{hand[5][1]}|  "
                f"|{hand[6][1]}|  "
            ),
            "'---'  " * 7
        ]
    if len(hand) == 8:
        ascii_hand = [
            ",---,  " * 8,
            (
                f"|{hand[0][0]}|  |{hand[1][0]}|  |{hand[2][0]}|  "
                f"|{hand[3][0]}|  |{hand[4][0]}|  |{hand[5][0]}|  "
                f"|{hand[6][0]}|  |{hand[7][0]}|  "
            ),
            (
                f"|{hand[0][1]}|  |{hand[1][1]}|  |{hand[2][1]}|  "
                f"|{hand[3][1]}|  |{hand[4][1]}|  |{hand[5][1]}|  "
                f"|{hand[6][1]}|  |{hand[7][1]}|  "
            ),
            "'---'  " * 8
        ]
    if len(hand) == 9:
        ascii_hand = [
            ",---,  " * 9,
            (
                f"|{hand[0][0]}|  |{hand[1][0]}|  |{hand[2][0]}|  "
                f"|{hand[3][0]}|  |{hand[4][0]}|  |{hand[5][0]}|  "
                f"|{hand[6][0]}|  |{hand[7][0]}|  |{hand[8][0]}|  "
            ),
            (
                f"|{hand[0][1]}|  |{hand[1][1]}|  |{hand[2][1]}|  "
                f"|{hand[3][1]}|  |{hand[4][1]}|  |{hand[5][1]}|  "
                f"|{hand[6][1]}|  |{hand[7][1]}|  |{hand[8][1]}|  "
            ),
            "'---'  " * 9
        ]
    return ascii_hand


def deck_of_cards():
    return [
        ("A  ", "  H"), ("2  ", "  H"), ("3  ", "  H"), ("4  ", "  H"),
        ("5  ", "  H"), ("6  ", "  H"), ("7  ", "  H"), ("8  ", "  H"),
        ("9  ", "  H"), ("10 ", "  H"), ("J  ", "  H"), ("Q  ", "  H"),
        ("K  ", "  H"), ("A  ", "  C"), ("2  ", "  C"), ("3  ", "  C"),
        ("4  ", "  C"), ("5  ", "  C"), ("6  ", "  C"), ("7  ", "  C"),
        ("8  ", "  C"), ("9  ", "  C"), ("10 ", "  C"), ("J  ", "  C"),
        ("Q  ", "  C"), ("K  ", "  C"), ("K  ", "  D"), ("Q  ", "  D"),
        ("J  ", "  D"), ("10 ", "  D"), ("9  ", "  D"), ("8  ", "  D"),
        ("7  ", "  D"), ("6  ", "  D"), ("5  ", "  D"), ("4  ", "  D"),
        ("3  ", "  D"), ("2  ", "  D"), ("A  ", "  D"), ("K  ", "  S"),
        ("Q  ", "  S"), ("J  ", "  S"), ("10 ", "  S"), ("9  ", "  S"),
        ("8  ", "  S"), ("7  ", "  S"), ("6  ", "  S"), ("5  ", "  S"),
        ("4  ", "  S"), ("3  ", "  S"), ("2  ", "  S"), ("A  ", "  S")
    ]


def hand_score(hand):
    hand_score = 0
    ace_in_hand = False
    for card in hand:
        if card[0].strip() == "A":
            hand_score += 11
            ace_in_hand = True
        elif card[0].strip() in ("J", "Q", "K"):
            hand_score += 10
        else:
            hand_score += int(card[0])
    if hand_score > 21 and ace_in_hand:
        hand_score -= 10
    return hand_score


def print_card_table(
    dealer_score, dealer_hand,
    player_hand, player_bankroll,
    player_bet, player_score,
    announcement, hole
):
    card_table = [f"Dealer's Score: {dealer_score}"]
    card_table.append(
        "-------------------------------------------------------------"
    )
    card_table.extend(ascii_hand(dealer_hand, hole))
    card_table.extend([""] * 3)
    card_table.extend(
        [" " * round((61 - len(announcement)) / 2) + f"{announcement}"]
    )
    card_table.extend([""] * 3)
    card_table.extend(ascii_hand(player_hand))
    card_table.append(
        "-------------------------------------------------------------"
    )
    card_table.append(f"Your Bankroll: {player_bankroll}€")
    card_table.append(f"Your Bet: {player_bet}€")
    card_table.append("")
    card_table.append(f"Your Score: {player_score}")
    for item in card_table:
        print(item)
