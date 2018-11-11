#!/usr/bin/python3

from mp2_lib import deck_of_cards, hand_score, print_card_table
from os import system
from random import shuffle
from time import sleep


class Dealer():

    def __init__(self):
        self.deck = deck_of_cards()
        self.hand = []
        self.score = 0

    def shuffle(self):
        for _ in range(7):
            shuffle(self.deck)

    @staticmethod
    def collect_bet():
        player.bet = 0

    def collect_cards(self):
        self.hand = []
        self.score = 0
        player.hand = []
        player.score = 0
        self.deck = deck_of_cards()

    def deal_card(self, player):
        player.hand.append(self.deck[0])
        player.update_score()
        self.deck.pop(0)
        sleep(1)

    @staticmethod
    def pay_out_bet():
        player.bankroll += player.bet * 2
        player.bet = 0

    @staticmethod
    def push():
        player.bankroll += player.bet
        player.bet = 0

    def update_score(self):
        self.score = hand_score(self.hand)


class Player():

    def __init__(self, bankroll, name):
        self.bankroll = bankroll
        self.bet = 0
        self.hand = []
        self.name = name
        self.score = 0

    def __str__(self):
        return self.name

    def place_bet(self, amount):
        self.bankroll -= amount
        self.bet = amount

    def update_score(self):
        self.score = hand_score(self.hand)


def print_game(announcement="", dealer_score=0, hole=False):
    system("clear")
    print_card_table(
        dealer_score, dealer.hand,
        player.hand, player.bankroll,
        player.bet, player.score,
        announcement, hole
    )


if __name__ == "__main__":
    dealer = Dealer()
    bankroll_start = 100
    name = input("Player, please enter your name: ")
    player = Player(bankroll_start, name)
    print_game(announcement=f"Welcome, {player}!")
    sleep(3)

    while True:
        print_game()
        bet = int(input(f"\n{player}, place your bet: "))
        bet = player.bankroll if bet > player.bankroll else bet
        player.place_bet(bet)
        print_game()

        dealer.shuffle()
        dealer.deal_card(player)
        print_game()
        dealer.deal_card(dealer)
        print_game(dealer_score=dealer.score)
        dealer.deal_card(player)
        print_game(dealer_score=dealer.score)
        dealer.deal_card(dealer)

        while player.score <= 21:
            print_game(dealer_score="?")
            hit = input(f"\n{player}, hit or stand [H/S]? ")
            if hit.casefold() == "h":
                dealer.deal_card(player)
            else:
                break

        if player.score > 21:
            dealer.collect_bet()
            if player.bankroll == 0:
                print_game(
                    announcement="A fool and his money are soon parted...",
                    dealer_score="?"
                )
                break
            game_over = True
            print_game(
                announcement=f"Sorry {player}, you lose.",
                dealer_score="?"
            )
        else:
            game_over = False

        if not game_over:
            sleep(1)
            print_game(dealer_score=dealer.score, hole=True)

            while dealer.score < 17:
                dealer.deal_card(dealer)
                print_game(dealer_score=dealer.score)

            if dealer.score > 21:
                dealer.pay_out_bet()
                game_over = True
                print_game(
                    announcement=f"Congratulations {player}, you win!",
                    dealer_score=dealer.score
                )

        if not game_over:
            game_over = True
            if player.score > dealer.score:
                dealer.pay_out_bet()
                print_game(
                    announcement=f"Congratulations {player}, you win!",
                    dealer_score=dealer.score,
                    hole=True
                )
            elif player.score < dealer.score:
                dealer.collect_bet()
                if player.bankroll == 0:
                    print_game(
                        announcement="A fool and his money are soon parted...",
                        dealer_score=dealer.score,
                        hole=True
                    )
                    break
                print_game(
                    announcement=f"Sorry {player}, you lose.",
                    dealer_score=dealer.score,
                    hole=True
                )
            else:
                dealer.push()
                print_game(
                    announcement="It's a push.",
                    dealer_score=dealer.score,
                    hole=True
                )

        if game_over:
            play_again = input(
                f"\n{player}, do you want to play again [Y/N]? "
            )
            if play_again.casefold() == "y":
                dealer.collect_cards()
                continue
            else:
                dealer.collect_cards()
                bankroll_end = abs(player.bankroll - bankroll_start)
                if player.bankroll >= bankroll_start:
                    print_game(
                        announcement=f"Well done, {player}! You won {bankroll_end}€."
                    )
                else:
                    print_game(
                        announcement=f"Too bad, {player}. You lost {bankroll_end}€."
                    )
                break
