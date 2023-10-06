def execute_turn(player, player_input):
  """
  Executes one turn of the round for a given player.

  Arguments:
    - player: A player dictionary object

  Returns an updated player dictionary object.
  """
  if player_input == 1:
    print("Rolling both...")
    roll_dice(2)
    print(player['name'] + " is now on " + str(player['score']))


  if player_input == 2:
    player['stayed'] = True


  if player_input == 3:
    print("Rolling one...")
    roll_dice(1)
    print(player['name'] + " is now on " + str(player['score']))

  if player['score'] >= 14:
    player['at_14'] = True

  if player['score'] > 21:
    player['bust'] = True

  print(player)


import random
def roll_dice(num_of_dice=1):
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


  for n in range(len(list_of_integer)):
      player['score'] += int(list_of_integer[n])



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


player = {'name': 'Player 1', 'score': 0, 'stayed': False, 'at_14': False, 'bust': False}
player = execute_turn(player, 1)
