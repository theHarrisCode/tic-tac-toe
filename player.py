import math
import random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    # we want all players to get their next move given a game
    def getMove(self,game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def getMove(self, game):
        square = random.choice(game.availableMoves()) #chooses a random spot on the board to move onto
        return square

class HumanPlayer(Player): 
    def __init__(self,letter):
        super().__init__(letter)

    def getMove(self,game):
        validSquare = False
        val = None
        while not validSquare:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            # we're going to check that this is a correct value by trying to cast
            # it to an interger, and if it's not, then we say its invalid
            # if that spot is not available on the board, we also say its invalid
            try:
                val = int(square)
                if val not in game.availableMoves():
                    raise ValueError
                validSquare =True # If these are successful, then yay!
            except ValueError:
                print('Invalid square. Try again.')