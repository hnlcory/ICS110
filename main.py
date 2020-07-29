#July 25 2020 - Project 1
''' TicTacToe game using rows and user input by Cory Parker'''
#Testing board
test_board = ['#','X','O','X','O','X','O','X','O','X']
test_board_empty = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

# Board Layout
def display_board(board):
    print(board[1]+' | '+board[2]+' | '+board[3])
    print('-- --- ---')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('-- --- ---')
    print(board[7]+' | '+board[8]+' | '+board[9])

#Chosing X or O
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1 choose X or O\n').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

#Way to place X or O in position on board
def place_marker(board, marker, position):
    board[position] = marker

#all rows, all columns, 2 diagpnals
def winner_check(board,filled):
    return((board[1] ==filled and board[2] ==filled and board[3]==filled) or
    (board[4] ==filled and board[5] ==filled and board[6]==filled) or
    (board[7] ==filled and board[8] ==filled and board[9]==filled) or
    (board[1] ==filled and board[4] ==filled and board[7]==filled) or
    (board[2] ==filled and board[5] ==filled and board[8]==filled) or
    (board[3] ==filled and board[6] ==filled and board[9]==filled) or
    (board[7] ==filled and board[5] ==filled and board[3]==filled) or
    (board[1] ==filled and board[5] ==filled and board[9]==filled))

#Choose who goes first
import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1 Starts'
    else:
        return 'Player 2 Starts'

#Check for open space is 1 spot
def space_check(board, position):
    
    return board[position] == ' '           

#Check for a fully filled board 
def full_board_check(board):
    for f in range(1,10):
        if space_check(board, f):
            return False
    return True

#Choosing where player wants to mark 
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Select a spot 1 - 9 {}\n'.format(turn)))
        
    return position

#If player wants to continue
def replay():
    
    return input('Play again? Y or N\n ')

print('Tic-Tac-Toe by Cory Parker')
input('Press Enter to Continue\n')

while True:
    # Reset and choose turn
    theBoard = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn)
    
    play_game = input('Ready to start Y or N\n')
    
    if play_game.lower() == 'y':
        game_on = True
    else:
        game_on = False
#Game Startup
    while game_on:
        if turn == 'Player 1':
            # Player1 turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if winner_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Player 1 Wins')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Tie')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2 turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if winner_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 Wins')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Tie')
                    break
                else:
                    turn = 'Player 1'

    if replay() in ('n', 'N'):
        break
