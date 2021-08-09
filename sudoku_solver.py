import numpy as np
board = [
    [0,0,0,2,6,0,7,0,1],
    [6,8,0,0,7,0,0,9,0],
    [1,9,0,0,0,4,5,0,0],
    [8,2,0,1,0,0,0,4,0],
    [0,0,4,6,0,2,9,0,0],
    [0,5,0,0,0,3,0,2,8],
    [0,0,9,3,0,0,0,7,4],
    [0,4,0,0,5,0,0,3,6],
    [7,0,3,0,1,8,0,0,0]
]

#print(board)
#print(np.matrix(board))
def possible(x,y,num):
    global board
    for i in range(0,9):
        if board[i][y] == num:
            return False
    for j in range(0,9):
        if board[x][j] ==num:
            return False
    x0=(x//3)*3
    y0=(y//3)*3
    for i in range(3):
        for j in range(3):
            if board[x0 + i][y0 + j] == num:
                return False
            return True


def solve():
    global board
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for num in range(1,10):
                    if possible(y,x,num):
                        board[y][x]=num
                        solve()
                        board[y][x] =0
                return
    print(np.matrix(board))
    input("ANYMORE?")

solve()