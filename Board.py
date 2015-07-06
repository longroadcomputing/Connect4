class Board:
  def __init__(self, boardClone = None):
    self._board = [[" " for x in range(0,6)] for x in range(0,7)]
    if (boardClone != None):
      for x in range(0,7):
        for y in range(0,6):
          self._board[x][y] = boardClone.GetSpace(x,y)
    
  def GetSpace(self, x, y):
    return self._board[x][y]
    
  def DropToken(self, column, token):
    if (self._board[column][0] != " "): # If column is full
      return False
    lowest = 0
    for y in range(1,6):
      if (self._board[column][y] == " "):
        lowest = y
    self._board[column][lowest] = token
    return True
    
  def IsFull(self):
    isfull = True
    for x in range(0,7):
      for y in range(0,6):
        if (self._board[x][y] == " "):
          isfull = False
          break
    return isfull
    
  def GetWinner(self):
    # Check columns
    for x in range(0,7):
      lastFound = ""
      foundLength = 1
      for y in range(0,6):
        if (self._board[x][y] == " "):
          lastFound = ""
          foundLength = 1
          continue
        if (self._board[x][y] == lastFound):
          foundLength += 1
          if (foundLength == 4):
            return lastFound
        else:
          lastFound = ""
          foundLength = 1
          lastFound = self._board[x][y]

    # Check rows
    for y in range(0,6):
      lastFound = ""
      foundLength = 1
      for x in range(0,7):
        if (self._board[x][y] == " "):
          lastFound = ""
          foundLength = 1
          continue
        if (self._board[x][y] == lastFound):
          foundLength += 1
          if (foundLength == 4):
            return lastFound
        else:
          lastFound = ""
          foundLength = 1
          lastFound = self._board[x][y]
          
    # Check \ diagonals
    for xStart in range(0,4):
      for yStart in range(0,3):
        lastFound = ""
        foundLength = 1
        y = yStart - 1
        for x in range(xStart, 7):
          y += 1
          if (y == 6):
            break
          if (self._board[x][y] == " "):
            lastFound = ""
            foundLength = 1
            continue
          if (self._board[x][y] == lastFound):
            foundLength += 1
            if (foundLength == 4):
              return lastFound
          else:
            lastFound = ""
            foundLength = 1
            lastFound = self._board[x][y]

    # Check / diagonals
    for xStart in range(4,7):
      for yStart in range(0,3):
        lastFound = ""
        foundLength = 1
        y = yStart - 1
        for x in range(xStart, 0, -1):
          y += 1
          if (y == 6):
            break
          if (self._board[x][y] == " "):
            lastFound = ""
            foundLength = 1
            continue
          if (self._board[x][y] == lastFound):
            foundLength += 1
            if (foundLength == 4):
              return lastFound
          else:
            lastFound = ""
            foundLength = 1
            lastFound = self._board[x][y]
            
    # If no matches found, return ""
    return ""
