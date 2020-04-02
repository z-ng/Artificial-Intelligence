import time
import sys
import msvcrt
import string

def display(game):
    for x in range(8):
        print(" ".join(game[0+(8*x):8+(8*x)]))
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
    while space < 0 and pos < 64 and game[pos] != "."  and pos//8 == index//8: # maybe add pos%8 != 0
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
    if space != index+7 and space != -1: #try to add this to all and pos//8 != space//8 may not be neccessary
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

def findVerticalPossible(game,nextMove,index):
    s = set()
    pos = index-8
    space = -1
    while space < 0 and pos >= 0 and game[pos] != nextMove:
        if game[pos] == ".":
            space = pos
        pos = pos-8
    if space != index-8 and space != -1:
        s.add(space)
    pos = index+8
    space = -1
    while space < 0 and pos < 64 and game[pos] != nextMove:
        if game[pos] == ".":
            space = pos
        pos = pos+8
    if space != index+8 and space != -1:
        s.add(space)
    return s
def findHorizontalPossible(game,nextMove,index):
    s = set()
    pos = index-1
    space = -1
    while space < 0 and pos >= 0 and game[pos] != nextMove and pos%8 != 0:
        if game[pos] == ".":
            space = pos
        pos = pos-1
    if space != index-1 and space != -1 and pos//8 == index//8:
        s.add(space)
    pos = index+1
    space = -1
    while space < 0 and pos < 64 and game[pos] != nextMove and pos%8 != 0:
        if game[pos] == ".":
            space = pos
        pos = pos+1
    if space != index+1 and space != -1:
        s.add(space)
    return s
def findDiagnolsPossible(game,nextMove,index):
    s = set()
    pos = index-7
    space = -1
    while space < 0 and pos >= 0 and game[pos] != nextMove and (pos+7)//8 != pos//8:
        if game[pos] == ".":
            space = pos
        pos = pos-7
    if space != index-7 and space != -1:
        s.add(space)
    pos = index+7
    space = -1
    while space < 0 and pos < 64 and game[pos] != nextMove and (pos-7)//8 != pos//8:
        if game[pos] == ".":
            space = pos
        pos = pos+7
    if space != index+7 and space != -1:
        s.add(space)

    pos = index-9 #other diagnol
    space = -1
    while space < 0 and pos >= 0 and game[pos] != nextMove and (pos+9)//8 != pos//8 and ((pos+9)//8)-(pos//8) <= 1:
        if game[pos] == ".":
            space = pos
        pos = pos-9
    if space != index-9 and space != -1:
        s.add(space)
    pos = index+9
    space = -1
    while space < 0 and pos < 64 and game[pos] != nextMove and (pos-9)//8 != pos//8 and (pos//8)-((pos-9)//8) <= 1:
        if game[pos] == ".":
            space = pos
        pos = pos+9
    if space != index+9 and space != -1:
        s.add(space)
    return s
def findPossibleMoves(game,nextMove):
    moves = set()
    for x in range(64):
        if game[x] == nextMove:
            moves = moves|findVerticalPossible(game,nextMove,x)
            moves = moves|findHorizontalPossible(game,nextMove,x)
            moves = moves|findDiagnolsPossible(game,nextMove,x)
    return moves

def flipBoard(game,token,position):
    board = findVertical(game,token,position)
    board = findHorizontal(board,token,position)
    board = findDiagnols(board,token,position)
    return board
def totalTokens(game):
    count = 0
    for x in game:
        if x != ".":
            count+=1
    return count
def findNextMove(game):
    if totalTokens(game) % 2 == 0:
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
    print("X Score:",xCount,"O Score:",oCount)

dictOfLetters = dict(enumerate(string.ascii_lowercase, 1))
board = "...........................XO......OX..........................."
allMoves = []
compMove = "X"
token = "X"
if len(sys.argv) > 1:
    if len(''.join(sys.argv[1])) > 3:
        board = ''.join(sys.argv[1])
        token = findNextMove(board)
    else:
        if ''.join(sys.argv[1]).upper() == "X":
            compMove = "O"
        elif ''.join(sys.argv[2]).upper() == "O":
            compMove = "X"
    if len(sys.argv) > 2:
        if len(''.join(sys.argv[2])) > 3:
            board = ''.join(sys.argv[2])
            token = findNextMove(board)
        else:
            if ''.join(sys.argv[2]).upper() == "X":
                compMove = "O"
            elif ''.join(sys.argv[2]).upper() == "O":
                compMove = "X"
board = board.upper()
display(board)
print("To exit the game, type q")
while "." in board:
    if len(findPossibleMoves(board,token)) == 0:
        if token == "X":
            token = "O"
        else:
            token = "X"
        if len(findPossibleMoves(board,token)) == 0:
            print("Game Over")
            displayScore(board)
            print(board)
            print(' '.join(allMoves))
            exit(0)
    if compMove != token:
        tmp = findPossibleMoves(board,token)
        posMoves = set()
        for x in tmp:
            s = dictOfLetters[(x%8)+1].upper()+" "+str((x//8)+1)
            posMoves.add(s)
        print("Possible Moves",posMoves)
        posLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h']
        posNumbers = ['1', '2', '3', '4', '5', '6', '7', '8']
        index = -1
        while index not in findPossibleMoves(board,token):
            letter = ''+str(msvcrt.getche())[2:3]
            if letter == "q":
                print("")
                print("You chose to exit, thank you for playing!")
                exit(0)
            number = ''+str(msvcrt.getche())[2:3]
            print("")
            if number == "q":
                print("You chose to exit, thank you for playing!")
                exit(0)
            if letter.lower() in posLetters and number in posNumbers:
                index = (ord(letter.lower()) - 97) + ((int(number) - 1) * 8)
                if index not in findPossibleMoves(board,token):
                    print("Error position not availible for move, try again")
                    index = -1
            else:
                print("Error you typed an invalid position, try again")
        print("")
        print("The position you chose was",letter.upper()+number)
        print("")
        allMoves.append(str(index))
        board = board[:index]+token+board[index+1:]
        board = flipBoard(board,token,index)
        displayScore(board)
        display(board)
        print(board)
        token = compMove
    else:
        randomMove = findPossibleMoves(board,token).pop()
        board = board[:randomMove] + token + board[randomMove+1:]
        board = flipBoard(board,token,randomMove)
        displayScore(board)
        display(board)
        print(board)
        allMoves.append(str(randomMove))
        if compMove == "X":
            token = "O"
        else:
            token = "X"
print("")
print("")
print("Final Score:")
displayScore(board)
print("Moves taken")
print(' '.join(allMoves))