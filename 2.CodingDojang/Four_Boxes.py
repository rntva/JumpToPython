#사각형 좌표만큼 채워주기
def set_square(board, x_1,y_1,x_2,y_2) :
    for y in range(y_1-1, y_2-1) :
        for x in range(x_1-1, x_2-1) :
            board[x][y] = 1
    return board
#list.count()가 안 먹혀서 걍 for문 돌림
def counting_area(board) :
    count = 0
    for x in board :
        for y in x :
            if y == 1 : count += 1
    return count

#판 초기화 하기
board = [[0] * 10 for x in range(10)]
#판 채우기
board = set_square(board, 1, 2, 4, 4)
board = set_square(board, 2, 3, 5, 7)
board = set_square(board, 3, 1, 6, 5)
board = set_square(board, 7, 3, 8, 6)
#면적출력
print(counting_area(board))




