#Main
#This is the file to run

from tictactoe import TicTacToe

print('Welcome to Tic Tac Toe!')

board = []
letter = ''
move = ''
bo = ''
le = ''

self = TicTacToe(board, letter, move, bo, le)

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1Letter, player2Letter = TicTacToe.inputPlayerLetter(self)
    turn = TicTacToe.whoGoesFirst(self)
    print('The ' + turn + ' will go first.')
    gameIsAlive = True

    while gameIsAlive:
        if turn == 'player 1':
            # Player 1's turn.
            TicTacToe.drawBoard(self, theBoard)
            move = TicTacToe.getPlayer1Move(self, theBoard)
            TicTacToe.makeMove(self, theBoard, player1Letter, move)
            if TicTacToe.isWinner(self, theBoard, player1Letter):
                TicTacToe.drawBoard(self, theBoard)
                print('Player 1 has won!')
                gameIsAlive = False
                break
            else:
                if TicTacToe.isBoardFull(self, theBoard):
                    TicTacToe.drawBoard(self, theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player 2'
        else:
            # Player 2's turn.
            TicTacToe.drawBoard(self, theBoard)
            move = TicTacToe.getPlayer2Move(self, theBoard)
            TicTacToe.makeMove(self, theBoard, player2Letter, move)
            if TicTacToe.isWinner(self, theBoard, player2Letter):
                TicTacToe.drawBoard(self, theBoard)
                print('Player 2 has won!')
                gameIsAlive = False
                break
            else:
                if TicTacToe.isBoardFull(self, theBoard):
                    TicTacToe.drawBoard(self, theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player 1'

    nNext = TicTacToe.playAgain(self)
    if not nNext.lower().startswith('y'):
        break