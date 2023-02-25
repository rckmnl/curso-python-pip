import random


def choose_option():
  options = ('piedra', 'papel', 'tijera')
  user_option = input('piedra, papel o tijera => ')
  user_option = user_option.lower()

  if not user_option in options:
    print('Hermano juega bien, eso no sirve')
    #continue
    return None, None
  computer_option = random.choice(options)

  print('Usted eligio => ', user_option)
  print('Yo elegi => ', computer_option)
  return user_option, computer_option


def check_rules(
  user_option,
  computer_option,
  user_wins,
  computer_wins,
):
  if user_option == computer_option:
    print('Nadie gana vuelve a jugar tas cagao')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('Has ganado piedra mata a tijera MALA MIA!!')
      user_wins += 1
    else:
      print('Has perdido papel mata piedra, no llevas vida')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('Has ganado papel mata a piedra MALA MIA!!')
      user_wins += 1
    else:
      print('Has perdido tijera mata papel, no llevas vida')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('Has ganado tijera mata a papel MALA MIA!!')
      user_wins += 1
    else:
      print('Has perdido piedra mata tijera, no llevas vida')
      computer_wins += 1
  return user_wins, computer_wins


def check_wins(user_wins, computer_wins):
  if computer_wins == 2:
    print('TE GANE MANAO, A LLORAR SIN SUEÑO')
    exit()

  if user_wins == 2:
    print('ME GANASTE MANAO, DISCULPAME')
    exit()


def run_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1

  while True:

    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('LLEVO ', computer_wins, 'Ganadas')
    print('LLEVAS ', user_wins, 'Ganadas')

    rounds += 1

    user_option, computer_option = choose_option()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
    check_wins(user_wins, computer_wins)


run_game()
