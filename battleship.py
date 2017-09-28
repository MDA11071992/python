from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)


def print_board(board):
    for row in board:
        print(" ".join(row))


print(print_board(board))


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)

print(ship_row)
print(ship_col)

turn = 0
for turn in range(4):
    print()
    print("Turn:", turn + 1)
    print()
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

    if ship_row == guess_row and ship_col == guess_col:
        print("Congratulations! You sank my battleship!")
        print("You WIN!")
        break
    else:
        # (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
        if guess_row not in range(5) or guess_col not in range(5):
            print("Oops, that's not even in the ocean.")
        elif board[guess_col][guess_row] == "X":
            print("You guessed that one already.")
        else:
            print()
            print("You missed my battleship!")
            board[guess_col][guess_row] = "X"
        print()
        print(print_board(board))

    if turn == 3:
        print()
        print('Game Over')