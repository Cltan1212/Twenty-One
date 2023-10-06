import random

def solo_game(players):
    """
    This function defines a game loop for a solo game of Twenty One against
    AI.
    """
    round = 0
    print(players)
    end_of_game(players) == False

    while end_of_game(players) == False:
        round += 1
        display_round_stats(round, players)
        display_game_options(players)
        end_of_game(players)

        if end_of_game(players) == True:
            return True


def display_round_stats(round, players):
    """
    Print the round statistics provided a list of players.

    Arguments:
      - round: Integer for round number
      - players: A list of player-dictionary objects
    """

    print("-----------Round " + str(round) + "-----------")
    for player in players:
        print(player['name'] + " is at " + str(player['score']))



def display_game_options(players):
    """
    Prints the game options depending on if a player's score is
    >= 14.

    Arguments:
      - player: A player dictionary object
    """
    for player in players:
        if player['score'] >= 14:
            print("------------ " + player['name'] + "'s turn------------")
            print(player['name'] + "'s score: " + str(player['score']))
            print('1. Roll \n2. Stay \n3. Roll one')

            if player['name'] == 'CPU Player':
                player_input = random.randint(1, 3)
                execute_turn(player, player_input)

            else:
                player_input = int(input("Please enter an option: "))
                execute_turn(player, player_input)

        else:
            print("------------ " + player['name'] + "'s turn------------")
            print(player['name'] + "'s score: " + str(player['score']))
            print('1. Roll \n2. Stay')

            if player['name'] == 'CPU Player':
                player_input = random.randint(1, 2)
                execute_turn(player, player_input)

            else:
                player_input = int(input("Please enter an option: "))
                execute_turn(player, player_input)

    return players



def execute_turn(player, player_input):
    """
    Executes one turn of the round for a given player.

    Arguments:
      - player: A player dictionary object

    Returns an updated player dictionary object.
    """
    if player_input == 1:
        print("Rolling both...")
        roll_dice(player,2)
        print(player['name'] + " is now on " + str(player['score']))

    if player_input == 2:
        player['stayed'] = True

    if player_input == 3:
        print("Rolling one...")
        roll_dice(player,1)
        print(player['name'] + " is now on " + str(player['score']))

    if player['score'] >= 14:
        player['at_14'] = True

    if player['score'] > 21:
        player['bust'] = True

    print(player)



def roll_dice(player,num_of_dice=1):
    """
    Rolls dice based on num_of_dice passed as an argument.

    Arguments:
      - num_of_dice: Integer for amount of dice to roll

    Returns the following tuple: (rolls, display_string)
      - rolls: A list of each roll result as an int
      - display_string: A string combining the dice art for all rolls into one string
    """
    list_of_integer = []

    while num_of_dice > 0:
        dice_number = random.randint(1, 6)
        num_of_dice -= 1
        list_of_integer.append(dice_number)

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

    die_art_string = ""
    for i in range(5):
        for n in list_of_integer:
            die_art_string += die_art[n][i]
        die_art_string += '\n'

    print(die_art_string)
    return player['score']



def end_of_game(players):
    """
    Takes the list of all players and determines if the game has finished,
    returning false if not else printing the result before returning true.

    Arguments:
      - players: A list of player-dictionary objects

    Returns True if round has ended or False if not. If true results are
    printed before return.
    """
    for player in players:
        if player['bust'] == True:

            if check_all_bust(players) == True:
                print("Everyone's gone bust! No one wins :(")
                return True

            if check_all_bust((players)) == False:
                check_the_winner(players)
                return True

        if player['score'] == 21:
            print(player['name'] + " is the winner!")
            return True

    return False


def check_all_bust(players):
    for player in players:
        if player['bust'] == False:
            return False

    return True

def check_the_winner(players):
    lst = []
    count_lst = 0
    for player in players:
        if player['bust'] == False:
            lst.append(player['score'])

    for n in lst:
        count_lst += 1

    if count_lst >= 2:

        if lst[-1] == lst[-2]:
            print("The game is a draw! No one wins :(")
            return True

    if lst == []:
        return False

    for player in players:
        if player['bust'] == True:
            print(player['name'] + " goes bust!")
            break

    for player in players:

        if lst == []:
            continue

        if max(lst) == player['score']:
            print(player['name'] + " is the winner!")
            return True

players = [{'name': 'Player 1', 'score': 0, 'stayed': False, 'at_14': False, 'bust': False}, {'name': 'CPU Player', 'score': 0, 'stayed': False, 'at_14': False, 'bust': False}]
solo_game(players)

