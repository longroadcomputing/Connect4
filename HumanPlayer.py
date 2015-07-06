from PlayerBase import *

class HumanPlayer(PlayerBase):
  def __init__(self):
    super().__init__("Human")
    
  def ChooseColumn(self, board):
    return self.GetValidColumn()
      
  def GetValidColumn(self):
    column = -2
    while column == -2:
      try:
        column = int(input("\nEnter column (1-7) or 0 to quit:"))
        column -= 1
        if (column < -1 or column > 6):
          raise ValueError()
      except ValueError:
        print("Please enter a value between 1 and 7")
        column = -2
    return column
