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
    for i in range(2, len(input_read)):
        if input_read[i] != '\n':
            row = input_read[i].strip().split(' ')
            clean_row = []
            # for j in range(0, len(row)):
            #     if row[j] != '':
                    # clean_row.append(row[j])
            board.append(row)
        elif input_read[i] == '\n':
            boards.append(board)
            board = []
    return boards

def mark_called_num(num):
    # cycle through all boards for a called number
    # i REALLY feel like i should be able to use recursion here, but. idk man.

    for i in range(0, len(boards)):
        for j in range(0, len(boards[i])):
            if num in boards[i][j]:
                index = boards[i][j].index(num)
                boards[i][j][index] = 'X'
        if check_bingo_across(boards[i]):
            print(f'BINGO ACROSS!! Card {boards[i]} is a winner! The number is {num}')
            return boards[i]
        elif check_bingo_down(boards[i], 0):
            print(f'BINGO DOWN!! Card {boards[i]} is a winner! The number is {num}')
            return boards[i]
        else:
            return 'not yet'

def check_bingo_across(card):
    # check for horizontal bingo

    for i in range(0, len(card)):
        print(card[i])
        if card[i] == ['X', 'X', 'X', 'X', 'X']:
            print('this one should win')
            return True

def check_bingo_down(card, index):
    # check for vertical bingo

    print(card)
    for i in range(0, len(card[0])):
        if card[0][i] == 'X':
            print(f'card 0 at {i} is X')
            if card[1][i] == 'X':
                print(f'card 1 at {i} is X')
                if card[2][i] == 'X':
                    print(f'card 2 at {i} is X')
                    if card[3][i] == 'X':
                        print(f'card 3 at {i} is X')
                        if card[4][i] == 'X':
                            print(f'card 4 at {i} is X -- THIS SHOULD WIN')
                            return True

        # while index < 5 and card[index][i] == 'X':
        #     print(f'card index: {index} card value: {card[index][i]}')
        #     if index == '4':
        #         return True
        #         break
        #     index += 1
        # i don't know why this while isn't working but i will fight it

def solve_for_value(winner, num):
    # sum up all the remaining numbers on the card, multiply by last called number

    card_sum = 0
    last_called = int(num)
    for i in range(0, len(winner)):
        if type(winner[i]) is list:
            for j in range(0, len(winner[i])):
                if winner[i][j] != 'X':
                    card_sum = card_sum + int(winner[i][j])
    print(card_sum)
    final_score = card_sum * last_called
    return final_score

def call_bingo_nums():
    # cycle through the numbers

    for i in range(0, len(call_order)):
        status = mark_called_num(call_order[i])
        if status != 'not yet':
            final_score = solve_for_value(status, call_order[i])
            print(f'FINAL SCORE for winning card is: {final_score}')
            break


boards = create_boards()
call_bingo_nums()
