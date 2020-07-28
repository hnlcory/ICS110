#July 25 2020 - Project 1
''' TicTacToe game using rows and user input by Cory Parker'''
input("Python Tic-Tac-Toe\nPress Enter to continue...")
print('Player 1 is X\nPlayer 2 is O\nPlayer 1 Start\n')

def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)
    
row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']
display(row1,row2,row3)
row2[1] = 'X'
