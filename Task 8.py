def solve(board, row, n):
    if row == n:
        print(board)
        return

    for col in range(n):
        if col not in board and all(
            abs(board[i] - col) != row - i
            for i in range(row)
        ):
            board.append(col)
            solve(board, row + 1, n)
            board.pop()


n = int(input("Enter N: "))
print("Solutions:")
solve([], 0, n)
