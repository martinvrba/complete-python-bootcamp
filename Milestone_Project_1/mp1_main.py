#!/usr/bin/python3

from collections import namedtuple
from os import system
from random import randint
from time import sleep


def check_game_state():
    game_over = False
    winner = is_winner()
    if winner:
        clear_screen()
        draw_board()
        print(f"Congratulations {winner}, you are the winner!")
        game_over = True
    if not winner and len(remaining_spaces) == 0:
        clear_screen()
        draw_board()
        print("It's a tie.")
        game_over = True
    if game_over:
        play_again = input("\nDo you want to play again [Y/N]? ")
        if play_again.casefold() == "y":
            return (True, "y")
        else:
            return (False, "n")
    return (True, "n")


def clear_screen():
    system("clear")


def draw_board():
    rows = [
        "\n     |     |     ", f"\n  {board['7']}  |  {board['8']}  |  {board['9']}  ", "\n     |     |     ",
        "\n", "-" * 18,
        "\n     |     |     ", f"\n  {board['4']}  |  {board['5']}  |  {board['6']}  ", "\n     |     |     ",
        "\n", "-" * 18,
        "\n     |     |     ", f"\n  {board['1']}  |  {board['2']}  |  {board['3']}  ", "\n     |     |     ",
        "\n" * 2
    ]
    for row in rows:
        print(row, end="")


def get_player_information(player_number):
    name = input(f"Player {player_number}, please enter your name: ")
    mark = input(f"{name}, please choose your mark [{'/'.join(marks)}]: ")
    marks.remove(mark)
    return Player(player_number, name, mark)


def is_winner():
    if look_for_winning_combination(current_player.mark) == "Found!":
        return current_player.name
    else:
        return None


def look_for_winning_combination(mark):
    winning_combinations = [
        ["1", "2", "3"], ["1", "4", "7"], ["1", "5", "9"], ["2", "5", "8"],
        ["3", "5", "7"], ["3", "6", "9"], ["4", "5", "6"], ["7", "8", "9"]
    ]
    marked_spaces = list(filter(lambda key: board[key] == mark, board.keys()))
    for winning_combination in winning_combinations:
        for space in winning_combination:
            if space not in marked_spaces:
                break
        else:
            return "Found!"
    return "Not found."


def place_mark(mark, space):
    board[space] = f"{mark}"
    remaining_spaces.pop()


def randomly_pick_starting_player():
    return player_1 if randint(1, 2) == 1 else player_2


def start_game():
    empty_board = {
        "7": " ", "8": " ", "9": " ",
        "4": " ", "5": " ", "6": " ",
        "1": " ", "2": " ", "3": " ",
    }
    empty_spaces = [" "] * 9
    starting_player = randomly_pick_starting_player()
    print(f"\n{starting_player.name} will have the opening move.")
    sleep(5)
    return (True, "n", empty_board, empty_spaces, starting_player)


def switch_player():
    return player_2 if current_player == player_1 else player_1


Player = namedtuple("Player", ["number", "name", "mark"])
marks = ["O", "X"]
player_1 = get_player_information("1")
player_2 = get_player_information("2")

play, play_again, board, remaining_spaces, current_player = start_game()

while play:
    clear_screen()
    draw_board()
    space = input(f"{current_player.name}, where do you want to place {current_player.mark} [1-9]? ")
    place_mark(current_player.mark, space)
    play, play_again = check_game_state()
    if not play:
        continue
    if play_again == "y":
        play, play_again, board, remaining_spaces, current_player = start_game()
        continue
    current_player = switch_player()
