print("         LET'S PLAY TIC TAC TOE          ")
#Game board
board=['-','-','-',
       '-','-','-',
       '-','-','-']

# If the game is still going
game_is_still_going=True
#Who won or tie?
winner=None
#Whos turn its is
current_player="X"

def display_board():
    print(board[0]+' | '+board[1]+' | '+board[2])
    print(board[3]+' | '+board[4]+' | '+board[5])
    print(board[6]+' | '+board[7]+' | '+board[8])
'''
While we call the function of display_board it will print the empty board
as  - | - | -
    - | - | -
    - | - | -
'''
def play_game():
    #inital we had to play game means we need to print the board
    display_board()
    #while the game is still ON
    while game_is_still_going:
        #players turn to play
        handle_turn(current_player)
        #The game is over
        check_if_game_over()
        #Give to the other player
        flip_player()
    if winner=="X" or winner=="O":
        print(winner+" "+"won")
    elif winner==None:
        print("TIE ")

def handle_turn(current_player):
    print(current_player+"'s turn.")
    position=input("Please choose an position from 0-8 : ")
    valid=False
    while not valid:
        while position not in ["0","1","2","3","4","5","6","7","8"]:
            position=input("Invalid Input.\nPlease choose an position fron 0-8 : ")
    
        position=int(position)
        #It will print the X in the place where we need in the empty board
        if board[position] == "-":
            valid =True
        else:
            print("You can't go there.Please Go again")
    board[position]=current_player 
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()
    return
    
def check_for_winner():
    global winner
    #Check rows
    row_winner=check_rows()
    #Check columns
    column_winner=check_columns()
    #Check diagonals
    diagonal_winner=check_diagonals()
    if row_winner:
        winner=row_winner
    elif column_winner:
        winner=column_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner=None
    return 
def check_rows(): 
    #Set the global varable 
    global game_is_still_going
    #check the rows all are same without a empty of a single board in it
    row_1=board[0]==board[1]==board[2] !='-'
    row_2=board[3]==board[4]==board[5] !='-'
    row_3=board[6]==board[7]==board[8] !='-'
    if row_1 or row_2 or row_3:
        game_is_still_going=False
    #retruning the winner in the tik tac toe (X or O)
    if row_1:
       return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return
def check_columns():
    #Set the global varable 
    global game_is_still_going
    #check the column all are same without a empty of a single board in it
    column_1=board[0]==board[3]==board[6] !='-'
    column_2=board[1]==board[4]==board[7] !='-'
    column_3=board[2]==board[5]==board[8] !='-'
    if column_1 or column_2 or column_3:
        game_is_still_going=False
    #retruning the winner in the tik tac toe (X or O)
    if column_1:
       return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return
def check_diagonals():
    #Set the global varable 
    global game_is_still_going
    #check the diagonal all are same without a empty of a single board in it
    diagonal_1=board[0]==board[4]==board[8] != '-'
    diagonal_2=board[2]==board[4]==board[6] != '-'
    if diagonal_1 or diagonal_2 :
        game_is_still_going=False
    #retruning the winner in the tik tac toe (X or O)
    if diagonal_1:
       return board[0]
    elif diagonal_2:
        return board[2]
    return


def check_if_tie():
    global game_is_still_going
    if "-" not in board:
        game_is_still_going=False
    return
def flip_player():
    global current_player
    #if current player is X,then it will change to O
    if current_player=="X":
        current_player='O'
    #if current player is O,then it will change to X
    elif current_player=="O":
        current_player='X'
    return

play_game()

