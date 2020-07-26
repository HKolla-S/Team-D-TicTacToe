# Main
# This is the file to run

from tictactoe import TicTacToe

print('Welcome to Tic Tac Toe!')

board = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letter = ''
move = ''
bo = ''
le = ''

self = TicTacToe(board, letter, move, bo, le)

# Prompting rules

print('Would you like to know the rules of tic-tac-toe? (yes or no)')
if input().lower().startswith('y'):
    print('''Tic-Tac-Toe is a two player game where both players alternate turns placing a mark of their choice (typically O or X) on a 3x3 grid, until either:

# One of the players gets 3 of their marks in a row; whether its horizontal, vertical, or diagonal. The player who gets 3 of their marks in a row wins.
# The grid is entirely filled with marks and neither of the players have 3 marks in a row. This ends in a stalemate.

Good luck!''')

while True:
    # Reset the board
    player1Letter, player2Letter = self.inputPlayerLetter()
    turn = self.whoGoesFirst()
    print(turn + ' will go first.')
    gameIsAlive = True

    while gameIsAlive:
        if turn == 'Player 1':
            # Player 1's turn
            self.drawBoard(board)
            move = self.getPlayer1Move(board)
            self.makeMove(board, player1Letter, move)
            if self.isWinner(board, player1Letter):
                self.drawBoard(board)
                print('Player 1 has won!')
                gameIsAlive = False
                break
            else:
                if self.isBoardFull(board):
                    self.drawBoard(board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 2'
        else:
            # Player 2's turn
            self.drawBoard(board)
            move = self.getPlayer2Move(board)
            self.makeMove(board, player2Letter, move)
            if self.isWinner(board, player2Letter):
                self.drawBoard(board)
                print('Player 2 has won!')
                gameIsAlive = False
                break
            else:
                if self.isBoardFull(board):
                    self.drawBoard(board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    nNext = self.playAgain()
    if not nNext.lower().startswith('y'):
        break
