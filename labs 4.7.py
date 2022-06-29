from random import randrange

board = [i+1 for i in range(9)]
board = [board[0:3],board[3:6], board[6:]]
print(board)

def display_board(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3,"|", sep="")
        for col in range(3):
            print("|   "+str(board[row][col])+"   ", end="") #put in number in each square
        print("|")
        print("|       " * 3,"|", sep="")
        print("+-------" * 3, "+", sep="")

def enter_move(board):
    ok = False
    while not ok:
        move = input("Enter your move: ")
        ok = len(move) == 1 and move >= '1' and move <= '9' # check if its a number between 1 and 9
        if not ok:
            print("invalid move") 
            continue
        move = int(move) - 1 	# change number from 0 to 8 for cell number
        row = move // 3 	# cell's row
        col = move % 3		# cell's column
        sign = board[row][col]	# check the selected square
        ok = sign not in ['O','X']
        if not ok:	# field already filled
            print("Field already occupied - enter another move")
            continue

    board[row][col] = "O"



def make_list_of_free_fields(board):
    freeCells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] != ["X","O"]:
                freeCells.append((row,col))
    return freeCells            



def victory_for(board,sgn):
	if sgn == "X":	
		who = 'me'
	elif sgn == "O": 
		who = 'you'	
	
	cross1 = cross2 = True  
	for rc in range(3):
		if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:	# check row rc
			return who
		if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn: # check column rc
			return who
		if board[rc][rc] != sgn: # check 1st diagonal
			cross1 = False
		if board[2 - rc][2 - rc] != sgn: # check 2nd diagonal
			cross2 = False
	if cross1 or cross2:
		return who
	return None


def draw_move(board):
    free = make_list_of_free_fields(board)
    freeCells = len(free)
    if freeCells > 0: # if the list is not empty, pick a random location for "X"
        locX = randrange(freeCells)
        row, col = free[locX]
        board[row][col] = 'X'

    # The function draws the computer's move and updates the board.3


board = [i+1 for i in range(9)]
board = [board[0:3],board[3:6], board[6:]]
board[1][1] = 'X' # first move for computer
free = make_list_of_free_fields(board)
human_turn = True # which turn is it now?
while len(free):
	display_board(board)
	if human_turn:
		enter_move(board)
		victor = victory_for(board,'O')
	else:	
		draw_move(board)
		victor = victory_for(board,'X')
	if victor != None:
		break
	human_turn = not human_turn		
	free = make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
	print("You won!")
elif victor == 'me':
	print("I won")
else:
	print("Tie!")
