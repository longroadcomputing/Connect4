import os
from time import sleep

from PlayerBase import *
from HumanPlayer import *
from RandomAIPlayer import *
from Board import *

# Class project to create an AI to play connect 4
    
##############################################
# GameState
class GameState:
  def __init__(self, parentGame):
    self._turn = parentGame._playerX
    self._winner = ""
    self._parentGame = parentGame
    
  def ChangeTurn(self):
    if (self._turn == self._parentGame._playerX):
      self._turn = self._parentGame._playerO
    else:
      self._turn = self._parentGame._playerX
      
  def GetTurn(self):
    return self._turn

##############################################
# Connect4Game object - The main object
class C4Game:
  def __init__(self, playerX, playerO):
    self._board = Board()
    self._playerX, self._playerO = playerX, playerO
    self._gamestate = GameState(self)
    
  def DrawBoard(self):
    print(" 1 2 3 4 5 6 7\n")
    for y in range(0,6):
      print("|{}|{}|{}|{}|{}|{}|{}|".format(self._board.GetSpace(0,y), self._board.GetSpace(1,y), self._board.GetSpace(2,y), self._board.GetSpace(3,y), self._board.GetSpace(4,y), self._board.GetSpace(5,y), self._board.GetSpace(6,y)))
      print("+-+-+-+-+-+-+-+")
   
  def PlayGame(self):
    validPlayers = False
    if (isinstance(self._playerX, PlayerBase) and isinstance(self._playerO, PlayerBase)):
      validPlayers = True
    if (not validPlayers):
      print("Error - Both players must derive from PlayerBase")
      return
    gameWinner = ""
    while gameWinner == "":
      os.system('cls' if os.name == 'nt' else 'clear')
      self.DrawBoard()
      gameWinner = self._board.GetWinner()
      if (gameWinner != ""):
        if (gameWinner == self._playerO.GetToken()):
          print(self._playerO.GetName(), "wins!")
        else:
          print(self._playerX.GetName(), "wins!")
        break
      if (self._board.IsFull()):
        print("Draw! - Board is full")
        break
      
      print("\nIt's", self._gamestate.GetTurn().GetName(), "to play")
      dropSuccessful = False
      while (not dropSuccessful):
        boardClone = Board(self._board)
        column = self._gamestate.GetTurn().ChooseColumn(boardClone)
        del boardClone
        if (column == -1):
          return
        if (self._board.DropToken(column, self._gamestate.GetTurn().GetToken())):
          print("Token dropped")
          self._gamestate.ChangeTurn()
          dropSuccessful = True
          sleep(0.1)
        else:
          print("Couldn't drop token there")
    
if __name__ == "__main__":
  playerAIBob = RandomAIPlayer("AI Bob", "X")
  playerAICharlie = RandomAIPlayer("AI Charlie", "O")
  playerHuman = HumanPlayer("Dave", "O")
  game = C4Game(playerAICharlie, playerAIBob)
  game.PlayGame()