import random

from PlayerBase import *

class RandomAIPlayer(PlayerBase):
  def __init__(self, name, token):
    super().__init__(name, token)
    random.seed()
    
  def ChooseColumn(self, board):
    return random.randint(0,6)