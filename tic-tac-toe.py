#Tic-tac-toe Board
"""
[
[-, -, -],
[-, -, -],
[-, -, -]
]

user_input between 1-9 according to index above.
if input isn't in the index ask user to go again
check if user_input is already used, if so go again
add input to board
check for win: rows, columns, and diagonals
switch between user inputs X-O will be inputs.



"""

board = [
  ["-", "-", "-"],
  ["-", "-", "-"],
  ["-", "-", "-"]
]

user = True # when true it refers to x, otherwise o
turns = 0

def print_board(board): #this is printing the board in terminal
    for row in board:
        for slot in row:
            print(f"{slot} ", end="") # this is putting them all in a line
        print() #this is seperating each row, indent with slots.

def quit(user_input):
    if user_input.lower() == "q":
        print("Thanks for playing")
        return True
    else:
        return False

def check_input(user_input):
    if not isnum(user_input):
        return False # check if its a number
    user_input = int(user_input)
    if not bounds(user_input):
        return False # check if its 1 - 9
    return True

def isnum(user_input):
    if not user_input.isnumeric(): #determining ig input is a number.
        print("This is not a valid input, must be a number.")
        return False
    else:
        return True

def bounds(user_input):
    if user_input > 9 or user_input < 1: #making sure the number is betweeen 1-9
        print("This is number is out of bounds")
        return False
    else:
        return True

def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":
        print("Position is already taken.")
        return True
    else:
        return False

def coordinates(user_input):
    row = int(user_input / 3)
    col = user_input
    if col > 2: col = int(col % 3)
    return (row, col)

def add_to_board(coords, board, active_user):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user

def current_user(user):
  if user: return "x"
  else: return "o"

def iswin(user, board):
  if check_row(user, board): return True #checks index for user having inputs in row for win.
  if check_col(user, board): return True #checks index for user having inputs in column for win.
  if check_diag(user, board): return True #checks index for user having inputs in a diagonal for win.
  return False

def check_row(user, board):
  for row in board:
    complete_row = True
    for slot in row:
      if slot != user:
        complete_row = False
        break
    if complete_row: return True
  return False

def check_col(user, board):
  for col in range(3):
    complete_col = True
    for row in range(3):
      if board[row][col] != user:
        complete_col = False
        break
    if complete_col: return True
  return False

def check_diag(user, board):
  #top left to bottom right
  if board[0][0] == user and board[1][1] == user and board[2][2] == user: return True
  elif board[0][2] == user and board[1][1] == user and board[2][0] == user: return True
  else: return False


while turns < 9:
    active_user = current_user(user)
    print_board(board)
    user_input = input("Enter a position between 1-9. Enter \"q\" to quit:")
    if quit(user_input): break
    if not check_input(user_input):
        print("Please try again.")
        continue
    user_input = int(user_input) - 1
    coords = coordinates(user_input)
    if istaken(coords, board):
        print("Please try again.")
        continue
    add_to_board(coords, board, active_user)
    if iswin(active_user, board):
        print(f"{active_user.upper()} won!")
        break

    turns += 1
    if turns == 9: print("Tie!")
    user = not user
