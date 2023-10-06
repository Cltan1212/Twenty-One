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



players = [{'name': 'Player 1', 'score': 21, 'stayed': False, 'at_14': True, 'bust': False},
           {'name': 'Player 2', 'score': 22, 'stayed': True, 'at_14': True, 'bust': True},
           {'name': 'Player 3', 'score': 22, 'stayed': True, 'at_14': True, 'bust': True},
           {'name': 'Player 4', 'score': 22, 'stayed': True, 'at_14': True, 'bust': True}]

end_of_game(players)