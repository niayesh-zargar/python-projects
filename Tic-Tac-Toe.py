import random

while True:
    user_mark = input ("'x' or 'o' or 'q': ")
    if user_mark in ['x' , 'o'  ,'q']:
        if user_mark == 'x': pc_mark = 'o'
        elif user_mark == 'q':
            GameRunning = False 
            break
        else: pc_mark = 'x' 
        GameRunning = True
        break
    else: 
        print('invalid choose')
        
GameRunning = True
winner = None
board =[
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-'] 
]
def quit():
    global GameRunning 
    if user_mark == 'q':
        print("thanks for playing.")
        GameRunning = False
        

def print_board(board): 
    for row in board :
        for splot in row :
            if splot.isnumeric() and not '-' :
                print("try again! this splot is used")
                continue
            else: 
                print(splot , end = ' ')
        print()

def user_choose_def():
    while True:
        row = input ("row: ")
        row = int(row) -1
        splot = input ("splot: ")
        splot = int(splot) -1
        if row in [0, 1, 2] and splot in [0, 1, 2] :
            if board[row][splot] == '-':
                board[row][splot] = user_mark
                break
            else:
                print("this item is full")
        else:
            print('invalid input.Please enter a number between 1 to 3.')
def pc_choose_def():
    while True:
        pc_row = random.randint(1,3) - 1  
        pc_splot = random.randint(1,3) - 1
        if board[pc_row][pc_splot] == '-':
            board[pc_row][pc_splot] = pc_mark
            break
def HorezentalWinning():
    global winner
    if board[0][0] ==board[0][1] == board[0][2] and board[0][0] != '-':
        winner = board[0][1]
        return True
    elif board[1][0] == board[1][1] == board[1][2] and board[1][1] !="-":
        winner = board[1][0]
        return True
    elif board[2][0] == board[2][1] == board[2][2] and board[2][2] !="-":
        winner = board[2][0]
        return True
    return False
def RowWinnning():
    global winner
    if board[0][0] == board[1][0] == board[2][0] and board[1][0] !="-":
        winner = board[1][0]
        return True   
    elif board[0][1] == board[1][1] == board[2][1] and board[1][1] !="-":
        winner = board[1][1]
        return True
    elif board[0][2] == board[1][2] == board[2][2] and board[1][2] !="-":
        winner = board[1][2]
        return True
        
    return False
def DiagWinning():
    global winner
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] !="-":
        winner = board[1][1]
        return True
    elif board[0][2] == board[1][1] == board[2][0] and board[1][1] !="-":
        winner = board[1][1]
        return True
    return False
def TieNOWin():
    global GameRunning
    if all(splot != '-' for row in board for splot in row):
        print("Noone win...")
        GameRunning = False
        return True
    return False
while GameRunning :
    quit()
    if not GameRunning :
        break
    print_board(board)
    user_choose_def()
    
    if RowWinnning() or DiagWinning() or   HorezentalWinning() :
        print_board(board)
        print(f"The winner is {winner}")
        GameRunning = False
    elif TieNOWin():
        break
    pc_choose_def()
    
    if RowWinnning() or DiagWinning() or   HorezentalWinning() :
        print_board(board)
        print(f"The winner is {winner}")
        GameRunning = False
    elif TieNOWin():
        break
    

