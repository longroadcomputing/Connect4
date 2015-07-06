# Connect 4
An exercise in creating an AI for a Connect4 game.
Requires knowledge of OOP in Python, including base classes, subclasses and polymorphism.

##PlayerBase.py
This is the base class for any kind of player.  It defines a method called ChooseColumn which must be overridden in your derived class.  The current state of the board is passed in to enable your AI to choose which column to choose.  You *must* return a number between 0 and 6 from this method.

##HumanPlayer.py and RandomAIPlayer.py
These are examples of classes derived from PlayerBase.  HumanPlayer asks the user to enter a column and returns that.  RandomAIPlayer chooses a number randomly between 0 and 6, regardless of the state of the board, and returns that.

##Board.py
A representation of the board.  You can change the board in any way you like in your ChooseColumn method as the changes won't be reflected in the actual game board.  How you use the board's functions is up to you.  Perhaps the most useful method to you will be GetSpace which simply returns which token is in the space given.

##Connect4.py
The main Connect 4 game class.  The only bit you'll need to change is the players at the bottom.
