def read_input():
    with open("./input/day04.txt") as f:
        draws = list(map(int, f.readline().split(",")))
        f.readline()

        raw_boards = "".join(f.readlines())
        raw_boards = raw_boards.split("\n\n")
        boards = []
        for b in raw_boards:
            lines = b.split("\n")
            board = []
            for line in lines:
                l = line.split(" ")
                r = list(map(int, filter(lambda a: a, l)))

                if len(r):
                    board.append(r)
            boards.append(board)
    return draws, boards

def mark_items(draw, line):
    result = []
    for item in line:
        result.append(None if draw == item else item)
    return result

def mark_board(draw, board):
    result = []
    for line in board:
        result.append(mark_items(draw, line))
    return result

def mark_all(draw, boards):
    result = []
    for board in boards:
        board = mark_board(draw, board)
        result.append(board)
    return result

def check_board(board):
    for line in board:
        complete = True
        for c in line:
            if c is not None:
                complete = False
        if complete:
            return True

    for i in range(5):
        complete = True
        for l in range(5):
            if board[l][i] is not None:
                complete = False
        if complete:
            return True

    return False


def check_boards(boards):
    winners = []
    for i, board in enumerate(boards):
        if check_board(board):
            winners.append((i, board))
    return winners

def sum_unmarked(board):
    s = 0
    for l in board:
        for c in l:
            if c:
                s += c
    return s

draws, boards = read_input()
for draw in draws:
    boards = mark_all(draw, boards)

    winners = check_boards(boards)
    if len(winners) == 1:
        _, winner = winners[0]
        s = sum_unmarked(winner)
        print("Part 1 %s" % (draw * s))
        break

draws, boards = read_input()
for draw in draws:
    boards = mark_all(draw, boards)

    winners = check_boards(boards)
    winners.reverse()
    for i, winner in winners:
        if len(boards) == 1:
            s = sum_unmarked(winner)
            print("Part 2 %s" % (draw * s))
        boards.pop(i)
