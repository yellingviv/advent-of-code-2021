# bingo y'all -- only rows and columns, no diagonals
# sum of all unmarked numbers left on first board to bingo
# multiply that sum by the final number called to get bingo
# that number is the winning score - solution to puzzle

# break out numbers to be called
# break out boards
# process through the calls

input_raw = open('input-day4.txt', 'r')
input_read = input_raw.readlines()
call_order = input_read[0].strip().split(',')
boards = []

def create_boards():
    # parse input to break boards into an array of arrays

    board = []
    for i in range(1, len(input_read)):
        if input_read[i] != '\n':
            board.append(input_read[i].strip())
        elif input_read[i] == '\n':
            boards.append(board)
            board = []
    return boards 
