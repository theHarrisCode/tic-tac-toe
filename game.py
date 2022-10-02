import math
import time
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # using a single list to represent 3x3 board
        self.currentWinner = None # keeps track of winner

    def printBoard(self):
        #loop that gets the rows of the board
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def printBoardNums():
        # 0 | 1 | 2 etc (tells us what number correspongs to what box on the board)
        numberBoard = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in numberBoard:
            print('| ' + ' | '.join(row) + ' |')

    def availableMoves(self):
        return[i for i, spot in enumerate(self.board) if spot == ' ']
        #**alternative for line 19**
        # moves = []
        # for (i,spot) in enumerate(self.board):
        #     # ['x', 'x', 'o'] --> [(0, 'x'), (1,'x'), (2,'o')]
        #     if spot == ' ':
        #         moves.append(i)
        # return moves 
    
    def emptySquares(self):
        return ' ' in self.board

    def numEmptySquares(self):
        return self.board.count(' ')
        # return len(self.availableMoves())

    def makeMove(self,square,letter):
        # if valid move, then make the move (assign square to letter)
        # then return true, if invalid return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square,letter):
                self.currentWinner = letter
            return True
        return False

    def winner(self,square,letter):
        # winner is  player that has a letter 3 times in a row,
        # but we have to checl ALL possibilites!
        # first lets check the row
        rowInd = square // 3
        row = self.board[rowInd*3 : (rowInd + 1) *3]
        if all([spot == letter for spot in row]):
            return True
        
        # check column
        colInd = square % 3
        column = [self.board[colInd+i*3] for i in range (3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonals
        # but only if the square is an even number (0, 2, 4, 6, 8)
        # these are the only moves possible to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]] #left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]] #right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        # if all of these fail
        return False

def play(game, xPlayer, oPlayer, printGame=True):
    #returns winner of game or non for a tie
    if printGame:
        game.printBoardNums()

    letter = 'X' # starting letter
        # iterate while the game still has empty squares
        # (we don't have to worry about winner because we'll just return that
        # which breaks the loop)
    while game.emptySquares():
        #get the move from the appropiate player
        if letter == 'O':
            square = oPlayer.getMove(game)
        else:
            square = xPlayer.getMove(game)
        # define a function to actually make the move
        if game.makeMove(square,letter):
            if printGame:
                print(letter + f"makes a move to square {square}" )
                game.printBoard()
                print('') # empty line
            if game.currentWinner:
                if printGame:
                    print(letter + ' wins!')
                return letter

            #after user makes move, the letters need to alternate (O ---> X)
            letter = 'O' if letter == 'X' else 'X' #switches player
            #if letter == 'X':
                #letter = 'O'
            #else:
                #letter = 'X'

        #tiny break in between CPU's moves
        time.sleep(0.8)
    if printGame:
        print('It\'s a tie!')

if __name__ == '__main__':
    xPlayer = HumanPlayer('X')
    oPlayer = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t,xPlayer,oPlayer,printGame=True)