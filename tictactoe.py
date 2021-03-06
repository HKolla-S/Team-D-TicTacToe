# Tic Tac Toe
import random


class TicTacToe:
    def __init__(self, board, letter, move, bo, le):
        self.board = board
        self.letter = letter
        self.move = move
        self.bo = bo
        self.le = le

    def drawBoard(self, board):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('       |       |')
        print('   ' + board[7] + '   |   ' + board[8] + '   |   ' + board[9])
        print('       |       |')
        print('-------|---------------')
        print('       |       |')
        print('   ' + board[4] + '   |   ' + board[5] + '   |   ' + board[6])
        print('       |       |')
        print('---------------|------')
        print('       |       |')
        print('   ' + board[1] + '   |   ' + board[2] + '   |   ' + board[3])
        print('       |       |')

    def inputPlayerLetter(self):
        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Player 1, Do you want to be X or O?')
            letter = input().upper()

        # the first element in the tuple is the player's letter, the second is the computer's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def whoGoesFirst(self):
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return 'Player 2'
        else:
            return 'Player 1'

    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        nNext = input()
        return nNext

    def makeMove(self, board, letter, move):
        board[move] = letter

    def isWinner(self, bo, le):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
                (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
                (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
                (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
                (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
                (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
                (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
                (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal

    def isSpaceFree(self, board, move):
        # Return true if the passed move is free on the passed board.
        return board[move] in ' 1 2 3 4 5 6 7 8 9 '

    def getPlayer1Move(self, board):
        # Let player 1 type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.isSpaceFree(board, int(move)):
            print('Player 1, What is your move? (1-9)')
            move = input()
        return int(move)

    def getPlayer2Move(self, board):
        # Let player 2 type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.isSpaceFree(board, int(move)):
            print('Player 2, What is your move? (1-9)')
            move = input()
        return int(move)

    def isBoardFull(self, board):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(board, i):
                return False
        return True
