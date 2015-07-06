class PlayerBase:
  def __init__(self, name, token):
    self._name = name
    self._token = token
    
  def GetName(self):
    return self._name
    
  def GetToken(self):
    return self._token
    
  def ChooseColumn(self, board):
    # This function must be overridden in a derived class.  It must return a value between 0 and 6
    raise NotImplementedError()