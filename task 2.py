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

  print(list_of_integer)


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

  raise NotImplementedError

result = roll_dice(5)
print(result[0])
print(result[1])