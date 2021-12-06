def input_txt(file_name):
    board_num = 0
    board = []
    board_list = []
    with open(file_name,'r') as f:
        for index,line in enumerate(f):
            line = line.strip()
            if index == 0:
                drawn_numbers = list(map(int,line.split(',')))
            else:
                if line:
                    board_row = list(map(int,line.split()))
                    board.append(board_row)
                else:
                    if board:
                        board_list.append(board)
                        board_num +=1
                        board = []
    return board_list,drawn_numbers,board_num

def confirm_win(board):
    for board_row in board:
        if sum(board_row) == 5:return True
    for index in range(len(board_row)):
        counter = 0
        for board_row in board:
            if board_row[index]:
                counter += 1
        if counter == 5:
            return True
        else:
            counter = 0

def score(board_list,winning_boards,drawn_number,score_board,score_board_num):
    score_sum = 0
    for entries in winning_boards:
         if score_board_num in entries:
             return
    for index_row,row in enumerate(board_list[score_board_num]):
        for index_num,number in enumerate(row):
            if score_board[index_row][index_num] != 1:
                score_sum += number
    winning_boards.append((board_list[score_board_num],score_board_num,score_sum*drawn_number))


def main():
    winning_boards = []
    board_list,drawn_numbers,board_num = input_txt('./Day-4/input.txt')
    score_boards = [[[0 for _ in range(5)] for _ in range(5)]for _ in range(board_num)]
    for drawn_number in drawn_numbers:
        for board_num,board in enumerate(board_list):
            for row_num,board_row in enumerate(board):
                if drawn_number in board_row:
                    number_pos = board_row.index(drawn_number)
                    score_boards[board_num][row_num][number_pos] = 1

        for score_board_num,score_board in enumerate(score_boards):
            if confirm_win(score_board):
                score(board_list = board_list,
                drawn_number = drawn_number,
                score_board = score_board,
                score_board_num = score_board_num,
                winning_boards = winning_boards,
                )
                
        else:
            continue
    return winning_boards[-1][2]
if __name__ == '__main__':
    print(main())
