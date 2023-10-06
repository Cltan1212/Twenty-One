"""
Group name: Friends
Authors:
"""

import time
import random


def display_rules():
  print("""
  _____________________________________________________________________________
  Twenty One is a game of chance where players take turns rolling two dice every 
  round until they decide to stop rolling and lock in their score or end up 
  going bust with a total over 21. The objective is to be the closest to 21 
  when everyone is done rolling.

  Rules are as per follows:
    - Players begin with a score of 0.
    - Each player has one turn to either roll or stop rolling each round.
    - Players can only do a regular roll of two dice until they 
      reach a score of at least 14.
    - Players with a score >= 14 have the option to only roll one dice.
    - If a player scores more than 21 they go bust and are out of the game.
    - The winning player is the one with the score closest to 21 when everyone 
      has finished rolling.
    - If all players go bust, no one wins.
    - If more than one player has the winning score, no one wins.
  _____________________________________________________________________________
  """)
  input("Press enter to go back")
  return


def display_main_menu():
    print("------------Main Menu------------")
    print("Welcome to Twenty One!")
    print("1. Solo")
    print("2. Local Multiplayer")
    print("3. Rules")
    print("4. Exit")
    print("---------------------------------")


def int_input(prompt="", restricted_to=None):
    """
  Helper function that modifies the regular input method,
  and keeps asking for input until a valid one is entered. Input
  can also be restricted to a set of integers.

  Arguments:
    - prompt: String representing the message to display for input
    - restricted: List of integers for when the input must be restricted
                  to a certain set of numbers

  Returns the input in integer type.
  """
    while True:
        player_input = input(prompt)
        try:
            int_player_input = int(player_input)
        except ValueError:
            continue
        if restricted_to is None:
            break
        elif int_player_input in restricted_to:
            break

    return int_player_input


def cpu_player_choice(score):
    """
  This function simply returns a choice for the CPU player based
  on their score.

  Arguments:
    - score: Int

  Returns an int representing a choice from 1, 2 or 3.
  """
    # here is the cpu player choice, for solo players
    time.sleep(2)
    if score < 14:
        return 1
    elif score < 17:
        return 3
    else:
        return 2


def display_game_options(players):
    """
    Prints the game options depending on if a player's score is
    >= 14.

    Arguments:
      - player: A player dictionary object
    """

    # we should check the player's score to determine the option for rolling one
    for player in players:
        if player['at_14']:
            print("------------ " + player['name'] + "'s turn------------")
            print(player['name'] + "'s score: " + str(player['score']))
            print('1. Roll \n2. Stay \n3. Roll one')

            # for CPU player, random choose the option
            if player['name'] == 'CPU Player':
                player_input = cpu_player_choice(player['score'])
                execute_turn(player, player_input)

            # for player, choice is input by player
            else:
                player_input = int_input(prompt="Please enter an option: ", restricted_to=[1,2,3])
                execute_turn(player, player_input)

        # for the player that score lower than 14, they only have two options
        else:
            print("------------ " + player['name'] + "'s turn------------")
            print(player['name'] + "'s score: " + str(player['score']))
            print('1. Roll \n2. Stay')

            if player['name'] == 'CPU Player':
                player_input = cpu_player_choice(player['score'])
                execute_turn(player, player_input)

            else:
                player_input = int_input(prompt="Please enter an option: ", restricted_to=[1,2])
                execute_turn(player, player_input)

    return players


def display_round_stats(round, players):
    """
    Print the round statistics provided a list of players.

    Arguments:
      - round: Integer for round number
      - players: A list of player-dictionary objects
    """

    # print the player score when the new round begin so that player can see their score
    print("-----------Round " + str(round) + "-----------")
    for player in players:
        print(player['name'] + " is at " + str(player['score']))


def roll_dice(player, num_of_dice=1):
    """
    Rolls dice based on num_of_dice passed as an argument.

    Arguments:
      - num_of_dice: Integer for amount of dice to roll

    Returns the following tuple: (rolls, display_string)
      - rolls: A list of each roll result as an int
      - display_string: A string combining the dice art for all rolls into one string
    """
    # we create a list for printing dice_art
    list_of_integer = []

    # based on the num_of_dice, we generate random number between 1 and 6 (which is dice number),
    # and append into list_of_integer
    while num_of_dice > 0:
        dice_number = random.randint(1, 6)
        num_of_dice -= 1
        list_of_integer.append(dice_number)

    # based on the random number that generate, add to the player's score
    for n in list_of_integer:
        player['score'] += n

    die_art = {
        1: ["┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"],
        2: ["┌─────────┐", "│  ●      │", "│         │", "│      ●  │", "└─────────┘"],
        3: ["┌─────────┐", "│  ●      │", "│    ●    │", "│      ●  │", "└─────────┘"],
        4: ["┌─────────┐", "│  ●   ●  │", "│         │", "│  ●   ●  │", "└─────────┘"],
        5: ["┌─────────┐", "│  ●   ●  │", "│    ●    │", "│  ●   ●  │", "└─────────┘"],
        6: ["┌─────────┐", "│  ●   ●  │", "│  ●   ●  │", "│  ●   ●  │", "└─────────┘"]
    }

    # we have to print the dice picture based on the list of integer that we generate
    die_art_string = ""
    for i in range(5):
        for n in list_of_integer:
            die_art_string += die_art[n][i]
        die_art_string += '\n'

    print(die_art_string)
    return player['score']  # return player's score


def execute_turn(player, player_input):
    """
    Executes one turn of the round for a given player.

    Arguments:
      - player: A player dictionary object

    Returns an updated player dictionary object.
    """
    # roll the die and calculate the score player has rolled for this round
    if player_input == 1:
        print("Rolling both...")
        roll_dice(player, 2)  # go to the function roll_dice, and return the score
        print(player['name'] + " is now on " + str(player['score']))  # print the player and score

    if player_input == 2:
        player['stayed'] = True

    if player_input == 3:
        print("Rolling one...")
        roll_dice(player, 1)  # go to the function roll dice
        print(player['name'] + " is now on " + str(player['score']))

    # for player's score larger or equal than 14, we change the status of 'at_14'
    # -> we have to use this status for display game options
    if player['score'] >= 14:
        player['at_14'] = True

    # for player's score larger than 21, we know that player is bust
    # -> we use this status to determine whether which player win
    if player['score'] > 21:
        player['bust'] = True

    return player


def end_of_game(players):
    """
    Takes the list of all players and determines if the game has finished,
    returning false if not else printing the result before returning true.

    Arguments:
      - players: A list of player-dictionary objects

    Returns True if round has ended or False if not. If true results are
    printed before return.
    """

    # check the game status
    active_player_count = 0
    players_num = len(players)
    for player in players:

        if player['stayed'] == True:
            active_player_count += 1
            player['stayed'] == False

    for player in players:
        lst = []
        if player['bust']:

            count_lst = 0
            for player in players:
                if not player['bust']:
                    lst.append(player['score'])

            for _ in lst:
                count_lst += 1

            if check_all_bust(players):  # go to the function check_all_bust
                print("Everyone's gone bust! No one wins :(")
                return True

            if not check_all_bust(players):
                check_the_winner(players,lst)
                return True

        if active_player_count == players_num:
            for player in players:
                lst.append(player['score'])
            check_the_winner(players,lst)

        if player['score'] == 21:
            print(player['name'] + " is the winner!")
            return True

    return False


def check_all_bust(players):
    for player in players:
        if not player['bust']:
            return False

    return True


def check_the_winner(players,lst):

    if len(lst) >= 2:

        if lst.sort()[-1] == lst.sort()[-2]:
            print("The game is a draw! No one wins :(")
            return True

    if not lst:
        return False

    for player in players:
        if player['bust']:
            print(player['name'] + " goes bust!")
            break

    for player in players:

        if not lst:
            continue

        if max(lst) == player['score']:
            print(player['name'] + " is the winner!")
            return True


def solo_game(players):
    """
    This function defines a game loop for a solo game of Twenty One against
    AI.
    """
    # initially, we let the round be 0
    round = 0
    display_round_stats(round, players)
    display_game_options(players)

    # use while loop to check whether end game or not
    while not end_of_game(players):
        round += 1
        display_round_stats(round, players)
        display_game_options(players)

    return True


def multiplayer_game(num_of_players):
    """
  This function defines a game loop for a local multiplayer game of Twenty One,
  where each iteration of the while loop is a round within the game.
  """
    # create a list for multiplayer
    players = []
    for n in range(num_of_players):
        player = {'name': 'Player ' + str(n + 1), 'score': 0, 'stayed': False, 'at_14': False, 'bust': False}
        players.append(player)

    # same as solo game, run the below function and check whether the game is over
    round = 0
    display_round_stats(round, players)
    display_game_options(players)

    while not end_of_game(players):
        round += 1
        display_round_stats(round, players)
        display_game_options(players)

    return True


def main():
    """
  Defines the main loop that allows the player to start a game, view rules or quit.
  """
    game = False
    while not game:
        display_main_menu()
        prompt = int_input(prompt="Please select the option(1-4): ", restricted_to=[1,2,3,4])

        # select the game type
        if prompt == 1:
            players = [{'name': 'Player 1', 'score': 0, 'stayed': False, 'at_14': False, 'bust': False},
                       {'name': 'CPU Player', 'score': 0, 'stayed': False, 'at_14': False, 'bust': False}]
            solo_game(players)  # solo game type
            return True

        if prompt == 2:
            num_of_players = int_input(prompt="Number of players: ", restricted_to=None)
            multiplayer_game(num_of_players)  # multiplayer game type
            return True

        if prompt == 3:
            display_rules()

        if prompt == 4:
            exit =
            return False


while not main():
    continue