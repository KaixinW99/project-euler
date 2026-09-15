"""Project Euler Problem 96: Su Doku

https://projecteuler.net/problem=96
(Copied verbatim from project_euler.ipynb, cell 96.)
"""
import os as _os  # added for the repository layout: data files live in ../data
_os.chdir(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "data"))

# Problem 96: Su Doku
def Sudoku(board):
    for y in range(9):
        for x in range(9):
            
            # already solved cell
            if board[x][y]!=0:
                continue
            
            # track which numbers could be placed in the current cell
            available = [False] + [True]*9
            
            # same row and column
            for i in range(9):
                if board[i][y]!=0:
                    available[board[i][y]] = False
                if board[x][i]!=0:
                    available[board[x][i]] = False

            # same region (3x3)
            rx = (x//3)*3                   
            ry = (y//3)*3
            for i in range(3):
                for j in range(3):
                    if board[i+rx][j+ry]!=0:
                        available[board[i+rx][j+ry]] = False

            # try all still available numbers
            for i in range(1,10):
                if available[i]:
                    board[x][y] = i
                    if Sudoku(board): return True
            # all failed, restore old board
            board[x][y] = 0
            return False

    # solve it
    return True

def combine_digit(l): return int("".join(str(i) for i in l))

f = open("p096_sudoku.txt","r")
All_board = []
for line in f:
    if line.startswith("Grid"):
        board = []
        continue
    board.append(list(map(int,list(line.strip()))))
    if len(board) == 9:
        All_board.append(board)
f.close()

for board in All_board:
    Sudoku(board)

ans = sum(combine_digit(it[0][:3]) for it in All_board)
print(ans)
