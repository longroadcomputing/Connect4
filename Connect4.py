import os

from PlayerBase import *
from HumanPlayer import *
from RandomAIPlayer import *
from Board import *

# Class project to create an AI to play connect 4
    
##############################################
# GameState
class GameState:
  def __init__(self):
    self._turn = "X"
    self._winner = ""
    
  def ChangeTurn(self):
    if (self._turn == "X"):
      self._turn = "O"
    else:
      self._turn = "X"
      
  def GetTurn(self):
    return self._turn
    
##############################################
# Connect4Game object - The main object
class C4Game:
  def __init__(self):
    self._board = Board()
    self._gamestate = GameState()
    
  def DrawBoard(self, board):
    print(" 1 2 3 4 5 6 7\n")
    for y in range(0,6):
      print("|{}|{}|{}|{}|{}|{}|{}|".format(board.GetSpace(0,y), board.GetSpace(1,y), board.GetSpace(2,y), board.GetSpace(3,y), board.GetSpace(4,y), board.GetSpace(5,y), board.GetSpace(6,y)))
      print("+-+-+-+-+-+-+-+")
      
  def PlayGame(self, playerX, playerO):
    validPlayers = False
    if (isinstance(playerX, PlayerBase) and isinstance(playerO, PlayerBase)):
      validPlayers = True
    if (not validPlayers):
      print("Error - Both players must derive from PlayerBase")
      return
    gameWinner = ""
    while gameWinner == "":
      os.system('cls' if os.name == 'nt' else 'clear')
      self.DrawBoard(self._board)
      gameWinner = self._board.GetWinner()
      if (gameWinner != ""):
        print(gameWinner, "wins!")
        break
      if (self._board.IsFull()):
        print("Draw! - Board is full")
        break
      
      print("\nIt's", self._gamestate.GetTurn(), "to play")
      dropSuccessful = False
      while (not dropSuccessful):
        if (self._gamestate.GetTurn() == "X"):
          column = playerX.ChooseColumn(self._board)
        else:
          column = playerO.ChooseColumn(self._board)
        if (column == -1):
          return
        if (self._board.DropToken(column, self._gamestate.GetTurn())):
          print("Token dropped")
          self._gamestate.ChangeTurn()
          dropSuccessful = True
        else:
          print("Couldn't drop token there")
    
if __name__ == "__main__":
  game = C4Game()
  playerX = RandomAIPlayer()
  playerO = RandomAIPlayer()
  game.PlayGame(playerX, playerO)