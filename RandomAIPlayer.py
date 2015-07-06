import random

from PlayerBase import *

class RandomAIPlayer(PlayerBase):
  def __init__(self):
    super().__init__("Human")
    random.seed()
    
  def ChooseColumn(self, board):
    return random.randint(0,6)