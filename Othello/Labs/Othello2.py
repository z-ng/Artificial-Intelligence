import time
import sys

def display(game):
    for x in range(8):
        print(" ".join(game[0+(8*x):8+(8*x)]))
def findTurn(game):
    if (64-game.count("."))%2 == 0:
        return "X"
    return "O"
def displayScore(board):
    xCount = 0
    oCount = 0
    for x in board:
        if x == "X":
            xCount = xCount+1
        elif x == "O":
            oCount = oCount+1
    print(board,"HW","X Score:",xCount,"O Score:",oCount)
def findVertical(game,nextMove,index):
    board = game
    pos = index-8
    space = -1
    while space < 0 and pos >= 0 and game[pos] != ".":
        if game[pos] == nextMove:
            space = pos
        pos = pos-8
    if space != index-8 and space != -1:
        while pos != index-8:
            pos = pos+8
            board = board[:pos] + nextMove + board[pos+1:]
    pos = index+8
    space = -1
    while space < 0 and pos < 64 and game[pos] != ".":
        if game[pos] == nextMove:
            space = pos
        pos = pos+8
    if space != index+8 and space != -1:
        while pos != index+8 and pos > 0:
            pos = pos-8
            board = board[:pos] + nextMove + board[pos+1:]
    return board
def findHorizontal(game,nextMove,index):
    board = game
    pos = index-1
    space = -1
    while space < 0 and pos >= 0 and game[pos] != "." and pos//8 == index//8:
        if game[pos] == nextMove:
            space = pos
        pos = pos-1
    if space != index-1 and space != -1 and space//8 == index//8:
        while pos != index:
            pos = pos+1
            board = board[:pos] + nextMove + board[pos+1:]
    pos = index+1
    space = -1
    while space < 0 and pos < 64 and game[pos] != "."  and pos//8 == index//8:
        if game[pos] == nextMove:
            space = pos
        pos = pos+1
    if space != index+1 and space != -1 and space//8 == index//8:
        while pos != index and pos > 0:
            pos = pos-1
            board = board[:pos] + nextMove + board[pos+1:]
    return board
def findDiagnols(game,nextMove,index):
    board = game
    pos = index-7
    space = -1
    while space < 0 and pos >= 0 and game[pos] != "." and (pos+7)//8 != pos//8:
        if game[pos] == nextMove:
            space = pos
        pos = pos-7
    if space != index-7 and space != -1:
        while pos != index-7 and pos > 0:
            pos = pos+7
            board = board[:pos] + nextMove + board[pos+1:]
    pos = index+7
    space = -1
    while space < 0 and pos < 64 and game[pos] != "." and (pos-7)//8 != pos//8:
        if game[pos] == nextMove:
            space = pos
        pos = pos+7
    if space != index+7 and space != -1:
        while pos != index+7 and pos > 0:
            pos = pos-7
            board = board[:pos] + nextMove + board[pos+1:]

    pos = index-9 #other diagnol
    space = -1
    while space < 0 and pos >= 0 and game[pos] != "." and (pos+9)//8 != pos//8 and ((pos+9)//8)-(pos//8) <= 1:
        if game[pos] == nextMove:
            space = pos
        pos = pos-9
    if space != index and space != -1 and pos//8 != space//8:
        while pos != index-9 and pos > 0:
            pos = pos+9
            board = board[:pos] + nextMove + board[pos+1:]
    pos = index+9
    space = -1
    while space < 0 and pos < 64 and game[pos] != "." and (pos-9)//8 != pos//8 and (pos//8)-((pos-9)//8) <= 1:
        if game[pos] == nextMove:
            space = pos
        pos = pos+9
    if space != index+9 and space != -1 and pos//8 != space//8:
        while pos != index+9 and pos > 0:
            pos = pos-9
            board = board[:pos] + nextMove + board[pos+1:]
    return board
def flipBoard(game,token,position):
    board = findVertical(game,token,position)
    board = findHorizontal(board,token,position)
    board = findDiagnols(board,token,position)
    return board
board = "...........................OX......XO..........................."
token = "-1"
position = "-12"
if len(sys.argv) > 1:
    if len(''.join(sys.argv[1])) == 64:
        board = ''.join(sys.argv[1])
    elif ''.join(sys.argv[1]).upper() == "X" or ''.join(sys.argv[1]).upper() == "O":
        token = ''.join(sys.argv[1]).upper()
    else:
        position = ''.join(sys.argv[1])
if len(sys.argv) > 2:
    if len(''.join(sys.argv[2])) == 64:
        board = ''.join(sys.argv[2])
    elif ''.join(sys.argv[2]).upper() == "O" or ''.join(sys.argv[2]).upper() == "X":
        token = ''.join(sys.argv[2]).upper()
    else:
        position = ''.join(sys.argv[2])
if len(sys.argv) > 3:
    if len(''.join(sys.argv[3])) == 64:
        board = ''.join(sys.argv[3])
    elif ''.join(sys.argv[3]).upper() == "X" or ''.join(sys.argv[1]).upper() == "O":
        token = ''.join(sys.argv[3]).upper()
    else:
        position = ''.join(sys.argv[3])
board = board.upper()
if token == "-1":
    token = findTurn(board)
if position == "-12":
    display(board)
    displayScore(board)
    exit(0)
posLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
if position[0].lower() in posLetters:
    position = (ord(position[0].lower()) - 97) + ((int(position[1]) - 1) * 8)
else:
    position = int(position)

display(board.upper())
board = board[:position]+token+board[position+1:]
tmpboard = ""+board
board = flipBoard(board,token,int(position))
print("")
display(board)
displayScore(board)