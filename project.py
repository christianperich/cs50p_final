import random
import sys
import os

COLOR_RESET = "\033[0m"
COLOR_BLUE = "\033[94m"
COLOR_GREEN = "\033[92m"
COLOR_RED = "\033[91m"


def repartir(all_cards):
    human_player = []
    cpu_player = []
    table_cards = [[], [], [], []]
    for _ in range(10):
        card = random.choice(all_cards)
        human_player.append(card)
        all_cards.remove(card)     

        card = random.choice(all_cards)
        cpu_player.append(card)
        all_cards.remove(card)    

    for index in range (4):
      card = random.choice(all_cards)
      table_cards[index].append(card)
      all_cards.remove(card)    
      
    
    return(human_player, cpu_player, table_cards)
  
  
def show_table(human_cards, cpu_cards, table_cards):
  print()  
  print(COLOR_GREEN)
  print('********************* TABLE *********************')
  for index in range (0, 4):
    print(table_cards[index])
  print(COLOR_RESET)  
  print('********************* MY CARDS *********************')
  print(sorted(human_cards))
  
  
def choose_cards(human_cards, cpu_cards):  
  card2 = random.choice(cpu_cards)
  cpu_cards.remove(card2)
  
  while True:
    try:      
      card1 = int(input('Choose a card: '))
      if card1 in human_cards:
        human_cards.remove(card1)
        print(COLOR_BLUE)
        print('********************* CARDS PLAYED *********************')
        print(f'Player: {card1}')
        print(f'CPU: {card2}')    
        print(COLOR_RESET)   
        
        return (card1, card2, human_cards, cpu_cards)
    except KeyboardInterrupt:
      sys.exit()
    except:
      pass
  

def put_cards(card, table_cards):  
  diferencia_minima = 100
  for index in range(0, 4):
    if card > table_cards[index][-1]:
      diferencia_actual = card - table_cards[index][-1]
      if diferencia_actual < diferencia_minima:
        diferencia_minima = diferencia_actual
        min_index = index
    elif card < table_cards[index][0]:
      diferencia_actual = table_cards[index][0] - card
      if diferencia_actual < diferencia_minima:
        diferencia_minima = diferencia_actual
        min_index = index
    else:
      continue
  
  
  if diferencia_minima == 100:
    print(COLOR_RED)
    print('***********************************************')
    print(COLOR_RESET)
    sys.exit(sys.exit(f"GAME OVER: The card {card} can't be played in any row"))
  elif card > table_cards[min_index][-1]:
    table_cards[min_index].append(card)
  elif card < table_cards[min_index][0]:
    table_cards[min_index].insert(0, card)
    
  for index in range(0, 4):
    if len(table_cards[index]) == 6:
      print(COLOR_RED)
      for index in range (0, 4):
        print(table_cards[index])
      print(COLOR_RESET)
      sys.exit(f'GAME OVER: The card {card} has exceeded the allowed limit(5) in the row.')
  
  return(table_cards)  


def main():
    all_cards = []
    for card in range(1,101):
      all_cards.append(card)     
    
    human_cards, cpu_cards, table_cards = repartir(all_cards)
    
    while True:    
      os.system('cls')

      show_table(human_cards, cpu_cards, table_cards)
      card1, card2, human_cards, cpu_cards = choose_cards(sorted(human_cards), sorted(cpu_cards))
      
      input('Press Enter to put the cards on the table...')
      
      if card1 < card2:
        table_cards = put_cards(card1, table_cards)
        table_cards = put_cards(card2, table_cards)
      else: 
        table_cards = put_cards(card2, table_cards)
        table_cards = put_cards(card1, table_cards)
    

if __name__ == '__main__':
    main()