import time
import sys
def totalTokens(game):
    count = 0
    for x in game:
        if x == ".":
            count+=1
    return count
def display(game):
    for x in range(8):
        print(" ".join(game[0+(8*x):8+(8*x)]))
def findTurn(game):
    if (game.count("X")+game.count("x")) %2 == 0:
        return "X"
    return "O"
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
    while space < 0 and pos >= 0 and game[pos] != nextMove and pos//8 == index//8:
        if game[pos] == ".":
            space = pos
        pos = pos-1
    if space != index-1 and space != -1 and space//8 == index//8:
        s.add(space)
    pos = index+1
    space = -1
    while space < 0 and pos < 64 and game[pos] != nextMove and pos//8 == index//8:
        if game[pos] == ".":
            space = pos
        pos = pos+1
    if space != index+1 and space != -1 and space//8 == index//8:
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
        #print(space,"1")
        s.add(space)
    pos = index+7
    space = -1
    while space < 0 and pos < 64 and game[pos] != nextMove and (pos-7)//8 != pos//8:
        if game[pos] == ".":
            space = pos
        pos = pos+7
    if space != index+7 and space != -1:
        #print(space,"2")
        s.add(space)

    pos = index-9 #other diagnol
    space = -1
    while space < 0 and pos >= 0 and game[pos] != nextMove and (pos+9)//8 != pos//8 and ((pos+9)//8)-(pos//8) <= 1:
        if game[pos] == ".":
            space = pos
        pos = pos-9
    if space != index-9 and space != -1:
        #print(index,space,"3")
        s.add(space)
    pos = index+9
    space = -1
    while space < 0 and pos < 64 and game[pos] != nextMove and (pos-9)//8 != pos//8 and (pos//8)-((pos-9)//8) <= 1:
        if game[pos] == ".":
            space = pos
        pos = pos+9
    if space != index+9 and space != -1:
        #print(index,space,"4")
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

def findHorizontal(game, nextMove, index):
    board = game
    pos = index - 1
    space = -1
    while space < 0 and pos >= 0 and game[pos] != "." and pos // 8 == index // 8:
        if game[pos] == nextMove:
            space = pos
        pos = pos - 1
    if space != index - 1 and space != -1 and space // 8 == index // 8:
        while pos != index:
            pos = pos + 1
            board = board[:pos] + nextMove + board[pos + 1:]
    pos = index + 1
    space = -1
    while space < 0 and pos < 64 and game[pos] != "." and pos // 8 == index // 8:  # maybe add pos%8 != 0
        if game[pos] == nextMove:
            space = pos
        pos = pos + 1
    if space != index + 1 and space != -1 and space // 8 == index // 8:
        while pos != index and pos > 0:
            pos = pos - 1
            board = board[:pos] + nextMove + board[pos + 1:]
    return board

def findVertical(game, nextMove, index):
    board = game
    pos = index - 8
    space = -1
    while space < 0 and pos >= 0 and game[pos] != ".":
        if game[pos] == nextMove:
            space = pos
        pos = pos - 8
    if space != index - 8 and space != -1:
        while pos != index - 8:
            pos = pos + 8
            board = board[:pos] + nextMove + board[pos + 1:]
    pos = index + 8
    space = -1
    while space < 0 and pos < 64 and game[pos] != ".":
        if game[pos] == nextMove:
            space = pos
        pos = pos + 8
    if space != index + 8 and space != -1:
        while pos != index + 8 and pos > 0:
            pos = pos - 8
            board = board[:pos] + nextMove + board[pos + 1:]
    return board

def findDiagnols(game, nextMove, index):
    board = game
    pos = index - 7
    space = -1
    while space < 0 and pos >= 0 and game[pos] != "." and (pos + 7) // 8 != pos // 8:
        if game[pos] == nextMove:
            space = pos
        pos = pos - 7
    if space != index - 7 and space != -1:
        while pos != index - 7 and pos > 0:
            pos = pos + 7
            board = board[:pos] + nextMove + board[pos + 1:]
    pos = index + 7
    space = -1
    while space < 0 and pos < 64 and game[pos] != "." and (pos - 7) // 8 != pos // 8:
        if game[pos] == nextMove:
            space = pos
        pos = pos + 7
    if space != index + 7 and space != -1:  # try to add this to all and pos//8 != space//8 may not be neccessary
        while pos != index + 7 and pos > 0:
            pos = pos - 7
            board = board[:pos] + nextMove + board[pos + 1:]

    pos = index - 9  # other diagnol
    space = -1
    while space < 0 and pos >= 0 and game[pos] != "." and (pos + 9) // 8 != pos // 8 and ((pos + 9) // 8) - (
        pos // 8) <= 1:
        if game[pos] == nextMove:
            space = pos
        pos = pos - 9
    if space != index and space != -1 and pos // 8 != space // 8:
        while pos != index - 9 and pos > 0:
            pos = pos + 9
            board = board[:pos] + nextMove + board[pos + 1:]
    pos = index + 9
    space = -1
    while space < 0 and pos < 64 and game[pos] != "." and (pos - 9) // 8 != pos // 8 and (pos // 8) - (
        (pos - 9) // 8) <= 1:
        if game[pos] == nextMove:
            space = pos
        pos = pos + 9
    if space != index + 9 and space != -1 and pos // 8 != space // 8:
        while pos != index + 9 and pos > 0:
            pos = pos - 9
            board = board[:pos] + nextMove + board[pos + 1:]
    return board

def flipBoard(game, token, position):
    board = findVertical(game, token, position)
    # print(board,"after vert")
    board = findHorizontal(board, token, position)
    # print(board,"after horizontal")
    board = findDiagnols(board, token, position)
    # print(board,"after diagnol")
    board = board[0:position] + token + board[position+1:]
    return board

def evalBoard(board,token):
    xCount = board.count("X")
    oCount = board.count("O")
    if token == "X":
        return xCount-oCount
    return oCount-xCount

def makeMove(board,token,mv):
    return flipBoard(board,token,mv)
def findEnemy(token):
    if token == "X":
        return "O"
    return "X"
def negamax(board, token, levels):
    # if not levels:
    if not len(findPossibleMoves(board,"X")) and not len(findPossibleMoves(board,"O")):
        return [evalBoard(board, token)]
    lm = findPossibleMoves(board, token)
    if not lm:
        best = negamax(board, findEnemy(token), levels - 1) + [-1]
    else:
        best = sorted([negamax(makeMove(board, token, mv), findEnemy(token), levels-1) + [mv] for mv in lm])[0]
    return [-best[0]] + best[1:]

game = "...........................OX......XO..........................."
nextMove = "H"
if len(sys.argv) > 1:
    if len(''.join(sys.argv[1])) > 2:
        game = ''.join(sys.argv[1])
    else:
        nextMove = ''.join(sys.argv[1]).upper()
if len(sys.argv) > 2:
    if len(''.join(sys.argv[2])) > 2:
        game = ''.join(sys.argv[2])
    else:
        nextMove = ''.join(sys.argv[2]).upper()
if nextMove == "H":
    if totalTokens(game) % 2 == 0:
        nextMove = "X"
    else:
        nextMove = "O"
game = game.upper()
nextMove = nextMove.upper()
display(game)
print(game)
print("Legal moves",findPossibleMoves(game,nextMove))
for x in range(64):
    if game[x] == "x" or game[x] == "o":
        game = game[:x] + game[x].upper() + game[x + 1:]
game = "...........................OX......XO..........................."
nextMove = "H"
if len(sys.argv) > 1:
    if len(''.join(sys.argv[1])) > 2:
        game = ''.join(sys.argv[1])
    else:
        nextMove = ''.join(sys.argv[1]).upper()
if len(sys.argv) > 2:
    if len(''.join(sys.argv[2])) > 2:
        game = ''.join(sys.argv[2])
    else:
        nextMove = ''.join(sys.argv[2]).upper()
if nextMove == "H":
    if totalTokens(game) % 2 == 0:
        nextMove = "X"
    else:
        nextMove = "O"
game = game.upper()

moves = findPossibleMoves(game,nextMove)
best_move = -1
moves = list(moves)
movesCopy = moves[:]
#print(moves)
board = game
if game.count(".") <= 9:
    nm = negamax(game,nextMove,8)
    best_move = nm
else:

    for x in moves:
        if ((x == 1 or x == 8 or x == 9) and (game[0] != nextMove)) or (
            (x == 6 or x == 15 or x == 14) and game[7] != nextMove) \
                or ((x == 48 or x == 57 or x == 49) and game[56] != nextMove) or (
            (x == 62 or x == 55 or x == 54) and game[63] != nextMove):
            movesCopy.remove(x)
    moves = movesCopy[:]

    for x in moves:
        notRemoved = True
        if x == 0 or x == 7 or x == 56 or x == 63:
            best_move = x
            best_move = 11 + ((best_move // 8) * 10) + (best_move % 8)
        if x <= 7:
            tmp = x + 0
            check = False
            while tmp >= 0 and check == False:
                tmp = tmp - 1
                if game[tmp] != nextMove:
                    check = True
            if check == False:
                best_move = x
                best_move = 11 + ((best_move // 8) * 10) + (best_move % 8)
            check = False
            while tmp <= 7 and check == False:
                tmp = tmp + 1
                if game[tmp] != nextMove:
                    check = True
            if check == False:
                best_move = x
                best_move = 11 + ((best_move // 8) * 10) + (best_move % 8)
        if x < 64 and x >= 56:
            tmp = x + 0
            check = False
            while tmp >= 56 and check == False:
                tmp = tmp - 1
                if game[tmp] != nextMove:
                    check = True
            if check == False:
                best_move = x
                best_move = 11 + ((best_move // 8) * 10) + (best_move % 8)
                check = False
            while tmp <= 63 and check == False:
                tmp = tmp + 1
                if game[tmp] != nextMove:
                    check = True
            if check == False:
                best_move = x
                best_move = 11 + ((best_move // 8) * 10) + (best_move % 8)
        if x % 7 == 0:
            tmp = x + 0
            check = False
            while tmp >= 7 and check == False:
                tmp = tmp - 8
                if game[tmp] != nextMove:
                    check = True
            if check == False:
                best_move = x
                best_move = 11 + ((best_move // 8) * 10) + (best_move % 8)
            check = False
            while tmp <= 63 and check == False:
                tmp = tmp + 8
                if game[tmp] != nextMove:
                    check = True
            if check == False:
                best_move = x
                best_move = 11 + ((best_move // 8) * 10) + (best_move % 8)
        if x % 8 == 0:
            tmp = x + 0
            check = False
            while tmp >= 0 and check == False:
                tmp = tmp - 8
                if game[tmp] != nextMove:
                    check = True
            if check == False:
                best_move = x
                best_move = 11 + ((best_move // 8) * 10) + (best_move % 8)
            check = False
            while tmp <= 56 and check == False:
                tmp = tmp + 8
                if game[tmp] != nextMove:
                    check = True
            if check == False:
                best_move = x
                best_move = 11 + ((best_move // 8) * 10) + (best_move % 8)
        if (x % 8 == 0 or x % 7 == 0 or x < 7 or (x > 56 and x < 63)) and len(moves) != 1:
            moves.remove(x)
    if len(moves) != 0 and best_move == -1:
        best_move = moves.pop()
    elif best_move == -1:
        best_move = findPossibleMoves(game, nextMove).pop()
if isinstance(best_move, list):
    print("heuristic move is",findPossibleMoves(board,nextMove).pop())
    print("negamax score of",best_move[0],"and I choose move",best_move[-1])
else:
    if nextMove == "X":
        findScore = game.count("X")-game.count("O")
    else:
        findScore = game.count("X")-game.count("O")
    print("Score:",findScore,"hueristic move is",best_move)