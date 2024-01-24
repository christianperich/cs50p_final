from project import repartir, put_cards, choose_cards
from unittest.mock import patch
import random

def test_repartir():
  all_cards = list(range(1, 101))
  human_cards, cpu_cards, table_cards = repartir(all_cards)

  assert len(human_cards) == 10
  assert len(cpu_cards) == 10
  assert len(table_cards) == 4
  
def test_put_cards():
  table_cards = [[1], [10], [20], [30]]
  card = 15
  updated_table_cards = put_cards(card, table_cards)

  assert any(len(row) > 1 for row in updated_table_cards)

def test_choose_Cards():
  human_cards = [1, 2, 3]
  cpu_cards = [4, 5, 6]

  with patch("builtins.input", side_effect=["2"]):
      choose_cards(human_cards, cpu_cards)
      
  assert human_cards == [1, 3]
  

  