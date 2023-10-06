def display_game_options(player):
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

        else:
            print("------------ " + player['name'] + "'s turn------------")
            print(player['name'] + "'s score: " + str(player['score']))
            print('1. Roll \n2. Stay')



def display_round_stats(round, player):
    """
    Print the round statistics provided a list of players.

    Arguments:
      - round: Integer for round number
      - players: A list of player-dictionary objects
    """

    print("-----------Round " + str(round) + "-----------")
    for player in players:
        print(player['name'] + " is at " + str(player['score']))



players = [{'name': 'Player 1', 'score': 23, 'stayed': False, 'at_14': True, 'bust': True},
           {'name': 'Player 2', 'score': 22, 'stayed': True, 'at_14': True, 'bust': True},]
round = 3
display_game_options(players)
display_round_stats(round, players)
