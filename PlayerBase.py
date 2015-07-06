class PlayerBase:
  def __init__(self, name):
    self._name = name
    
  def ChooseColumn(self, board):
    # This function must be overridden in a derived class
    raise NotImplementedError()