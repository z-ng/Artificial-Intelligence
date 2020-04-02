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

def buildLookUp():
    lookUp = {}
    for x in range(64):
        totalMovesForIndex = []
        listVertDown = []
        pos = x-8
        while pos >= 0:
            listVertDown.append(pos)
            pos = pos - 8
        if len(listVertDown) > 1:
            totalMovesForIndex.append(listVertDown)
        listVertUp = []
        pos = x+8
        while pos < 64:
            listVertUp.append(pos)
            pos = pos+8
        if len(listVertUp) > 1:
            totalMovesForIndex.append(listVertUp)
        ###HORIZONTAL######

        listHorizontalLeft = []
        pos = x-1
        while pos >= 0 and pos //8 == x//8:
            listHorizontalLeft.append(pos)
            pos = pos-1
        if len(listHorizontalLeft) > 1:
            totalMovesForIndex.append(listHorizontalLeft)
        listHorizontalRight = []
        pos = x+1
        while pos < 64 and pos//8 == x//8:
            listHorizontalRight.append(pos)
            pos = pos+1
        if len(listHorizontalRight) > 1:
            totalMovesForIndex.append(listHorizontalRight)

        #####DIAGNOL######

        listDiagnolUpRight = []
        pos = x-7
        while pos >= 0 and (((pos+7) // 8) != (pos //8)) == 1:
            listDiagnolUpRight.append(pos)
            pos = pos-7
        if len(listDiagnolUpRight) > 1:
            totalMovesForIndex.append(listDiagnolUpRight)
        listDiagnolDownLeft = []
        pos = x+7
        while pos < 64 and (((pos-7) //8) - (pos // 8)) == -1:  # was originally pos-7//8 != pos//8 but chagned to prevent outofounds, repeated for others
            listDiagnolDownLeft.append(pos)
            pos = pos+7
        if len(listDiagnolDownLeft) > 1:
            totalMovesForIndex.append(listDiagnolDownLeft)
        listDiagnolUpLeft = []
        pos = x-9
        while pos >= 0 and ((pos+9) //8 - pos //8) == 1:
            listDiagnolUpLeft.append(pos)
            pos = pos -9
        if len(listDiagnolUpLeft) > 1:
            totalMovesForIndex.append(listDiagnolUpLeft)
        pos = x+9
        listDiagnolDownRight = []
        while pos < 64 and (((pos-9)//8) - (pos//8)) == -1:
            listDiagnolDownRight.append(pos)
            pos = pos+9
        if len(listDiagnolDownRight) > 1:
            totalMovesForIndex.append(listDiagnolDownRight)
        # print(x,listDiagnolDownRight,listVertDown)
        lookUp[x] = totalMovesForIndex
        # print(x,totalMovesForIndex)
    # for key,value in lookUp.items():
    #     print(key,value)
    return lookUp



def findPossibleMoves(game,nextMove,lookUp):
    # print("Finding possible moves for",game,nextMove)
    moves = set()
    for x in range(64):
        if(game[x]=="."):
            for seq in lookUp[x]:
                if game[seq[0]] == findEnemy(nextMove):
                    # print(x,"seq",seq,findEnemy(nextMove))
                    found = False
                    for pos in seq[1:]:
                        # if x == 55: print("SPECIAL CASE",seq[1:],game[pos],pos)
                        if game[pos] == ".":
                            break
                        if game[pos] == nextMove:
                            # print("The move",x,seq)
                            moves.add(x)
                            break
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
        while pos != index - 7:
            pos = pos + 7
            board = board[:pos] + nextMove + board[pos + 1:]
    pos = index + 7
    space = -1
    while space < 0 and pos < 64 and game[pos] != "." and (pos - 7) // 8 != pos // 8:
        if game[pos] == nextMove:
            space = pos
        pos = pos + 7
    if space != index + 7 and space != -1:  # try to add this to all and pos//8 != space//8 may not be neccessary
        while pos != index + 7:
            pos = pos - 7
            board = board[:pos] + nextMove + board[pos + 1:]
    #print(index,"in diagnol")
    pos = index - 9  # other diagnol
    space = -1
    while space < 0 and pos >= 0 and game[pos] != "." and (pos + 9) // 8 != pos // 8 and ((pos + 9) // 8) - (pos // 8) <= 1:
        if game[pos] == nextMove:
            space = pos
        pos = pos - 9
    #print(space,"space")
    #print(pos,"pos")
    if space != index and space != -1 and pos // 8 != space // 8:
        while pos != index - 9:
            pos = pos + 9
            board = board[:pos] + nextMove + board[pos + 1:]
    pos = index + 9
    space = -1
    while space < 0 and pos < 64 and game[pos] != "." and (pos - 9) // 8 != pos // 8 and (pos // 8) - ((pos - 9) // 8) <= 1:
        if game[pos] == nextMove:
            space = pos
        pos = pos + 9
    if space != index + 9 and space != -1 and pos // 8 != space // 8:
        while pos != index + 9:
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
def negamax(board, token, levels,lookUp):
    # if not levels:
    if not len(findPossibleMoves(board,"X",lookUp)) and not len(findPossibleMoves(board,"O",lookUp)):
        return [evalBoard(board, token)]
    lm = findPossibleMoves(board, token,lookUp)
    if not lm:
        best = negamax(board, findEnemy(token), levels - 1) + [-1]
    else:
        best = sorted([negamax(makeMove(board, token, mv), findEnemy(token), levels-1) + [mv] for mv in lm])[0]
    return [-best[0]] + best[1:]

def negamaxTerminal(brd, token, improvable, hardbound,lookUp):  # -65 and 65
    lm = findPossibleMoves(brd,token,lookUp)
    if not lm:
        lm = findPossibleMoves(brd, findEnemy(token),lookUp)
        if not lm: return [evalBoard(brd,token), -3]  # game over
        nm = negamaxTerminal(brd, findEnemy(token), -hardbound, -improvable,lookUp)+[-1]
        return [-nm[0]] + nm[1:]
    best = [] #what is returned
    newHB = -improvable
    for mv in lm:
        nm = negamaxTerminal(makeMove(brd,token,mv),findEnemy(token),-hardbound,newHB,lookUp)+[mv]
        if not best or nm[0] < newHB:
            best = nm
            if nm[0] < newHB:
                best = nm
                if nm[0] < newHB:
                    newHB = nm[0]
                    if -newHB >= hardbound:
                        #pruning
                        return [-best[0]]+best[1:]
    return [-best[0]]+best[1:]

start = time.time()
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


lookUp = buildLookUp()
game = game.upper()
nextMove = nextMove.upper()
display(game)
print(game)
print("Legal moves",findPossibleMoves(game,nextMove,lookUp))
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


moves = findPossibleMoves(game,nextMove,lookUp)
best_move = -1
moves = list(moves)
movesCopy = moves[:]
print(moves)
board = game[:]
print(game)
if game.count(".") <= 14:
    nm = negamaxTerminal(board,nextMove,-65,65,lookUp)
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
            #best_move = 11 + ((best_move // 8) * 10) + (best_move % 8)
            print("Best move:", best_move)
            exit(0)
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
    print("board",board)
    print("heuristic move is",findPossibleMoves(board,nextMove,lookUp).pop())
    print("negamax score of",best_move[0],"and I choose move",best_move)
else:
    if nextMove == "X":
        findScore = game.count("X")-game.count("O")
    else:
        findScore = game.count("X")-game.count("O")
    print("board",board)
    print(findScore,"hueristic move is",best_move)
print(time.time()-start)