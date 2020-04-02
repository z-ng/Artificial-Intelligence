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
                        # return [-best[0]+best[1:]] # the actual pruning
                        return [-best[0]]+best[1:]
    return [-best[0]]+best[1:]

def minimizeEnemyMoves(board,token,moves,lookUp):
    minMoves = -1
    bestMove = moves[0]
    enemy = findEnemy(token)
    for x in moves:
        tmpBoard = board[:]
        tmpBoard = makeMove(tmpBoard,token,x)
        totalEnemyMoves = len(findPossibleMoves(tmpBoard,enemy,lookUp))
        if totalEnemyMoves > minMoves:
            bestMove = x
            minMoves = totalEnemyMoves
    return bestMove

def maximizeMyMoves(board,token,moves,lookUp):
    minMoves = -1
    bestMove = moves[0]
    enemy = findEnemy(token)
    for x in moves:
        tmpBoard = board[:]
        tmpBoard = makeMove(tmpBoard,token,x)
        totalEnemyMoves = len(findPossibleMoves(tmpBoard,enemy,lookUp))
        if totalEnemyMoves > minMoves:
            bestMove = x
            minMoves = totalEnemyMoves
    return bestMove

def isOnBoundry(game,nextMove,stableMoves):
    upLeft = False
    downLeft = False
    upRight = False
    downRight = False
    right = False
    left = False
    up = False
    down = False
    #RIGHT
    if (nextMove%8 ==7):
        right = True
    elif nextMove+1 in stableMoves:
        right = True
    else:
        tmp = nextMove+1
        while tmp%8 != 7 and game[tmp] != ".":
            tmp = tmp+1
        if tmp%8 ==7:
            right = True
    #UP
    if (nextMove <= 7):
        up = True
    elif nextMove-8 in stableMoves:
        up = True
    else:
        tmp = nextMove-8
        while (tmp > 7) and game[tmp] != ".":
            tmp = tmp-8
        if (tmp <= 7):
            up = True
    #LEFT
    if (nextMove%8 == 0):
        left = True
    elif nextMove-1 in stableMoves:
        left = True
    else:
        tmp = nextMove-1
        while tmp%8 != 0 and game[tmp] != ".":
            tmp = tmp-1
        if tmp%8 == 0:
            left = True
    #DOWN
    if (nextMove >= 56):
        down = True
    elif nextMove+8 in stableMoves:
        down = True
    else:
        tmp = nextMove+8
        while tmp < 56 and game[tmp] != ".":
            tmp = tmp+8
        if (tmp >= 56):
            down = True
    #UPRIGHT
    if right == True or up == True:
        upRight = True
    elif nextMove-7 in stableMoves:
        upRight = True
    else:
        tmp = nextMove-7
        while tmp>7 and tmp%8 != 7 and game[tmp] != ".":
            tmp = tmp-7
        if tmp < 7 or tmp%8 == 7:
            upRight = True
    #DOWNRIGHT
    if right == True or down == True:
        downRight = True
    elif nextMove+9 in stableMoves:
        downRight = True
    else:
        tmp = nextMove+9
        while tmp < 56 and tmp%8 != 7 and game[tmp] != ".":
            tmp = tmp+9
        if tmp >56 or tmp%8 == 7:
            downRight = True
    #UPLEFT
    if up == True or left == True:
        upLeft = True
    elif nextMove-9 in stableMoves:
        upLeft = True
    else:
        tmp = nextMove-9
        while tmp > 7 and tmp%8 != 0 and game[tmp] != ".":
            tmp = tmp-9
        if tmp <= 7 or tmp%8 == 0:
            right = True
    #DOWNLEFT
    if down == True or left == True:
        downLeft = True
    elif nextMove+7 in stableMoves:
        downLeft = True
    else:
        tmp = nextMove+7
        while tmp%8 != 0 and tmp<56 and game[tmp] != ".":
            tmp = tmp+7
        if tmp >= 56 or tmp%8 == 0:
            downLeft = True
    if left == True and right == True and up == True and down == True and upRight == True and downRight == True and downLeft == True and upLeft == True:
        return True
def findStableMoves(board,token,lookUp):
    moves = findPossibleMoves(board,token,lookUp)
    stableMoves = []
    if board[0] == "." and board[7] == "." and board[56] == "." and board[63] == ".":
        return []
    if len(moves) != 0:
        for x in moves:
            if isOnBoundry(board,x,stableMoves) == True:
                stableMoves.append(x)
        orig = []
        while orig != stableMoves:
            orig = stableMoves[:]
            for x in moves:
                if isOnBoundry(board,x,stableMoves):
                    stableMoves.append(x)
        return stableMoves


def main():
    t = time.time()
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
    for x in range(64):
        if game[x] == "x" or game[x] == "o":
            game = game[:x] + game[x].upper() + game[x + 1:]
    # still running is timer running
    # best_move = stored best move overall
    game = ''.join(game).replace('?', "").replace("@", "X").replace('o', "O")
    lookUp = buildLookUp()
    print(game)
    print(findPossibleMoves(game,nextMove,lookUp))
    # nextMove = "X" if nextMove == "@" else 'O'
    # for x in range(64):
    #     if game[x] == "x" or game[x] == "o":
    #         game = game[:x] + game[x].upper() + game[x + 1:]
    moves = findPossibleMoves(game, nextMove,lookUp)
    moves = list(moves)
    print(moves)
    best_move = moves[0]
    found = False
    board = game
    # best_move.value = 11 + ((best_move.value // 8) * 10) + (best_move.value % 8)
    if len(moves) == 0:
        print("No moves are possible")
    else:
        if 64 - board.count("X") - board.count("O") >= 11 :
            movesCopy = moves[:]
            for x in moves:
                if ((x == 1 or x == 8 or x == 9) and (game[0] != nextMove)) or (
                    (x == 6 or x == 15 or x == 14) and game[7] != nextMove) \
                        or ((x == 48 or x == 57 or x == 49) and game[56] != nextMove) or (
                    (x == 62 or x == 55 or x == 54) and game[63] != nextMove):
                    if len(movesCopy) != 1:
                        movesCopy.remove(x)
            moves = movesCopy[:]
            for x in moves:
                if x == 0 or x == 7 or x == 56 or x == 63:
                    best_move = x
                    print(best_move)
                    found = True
                    exit(0)
            for x in moves:
                if x <= 7:
                    tmp = x + 0
                    check = False
                    while tmp >= 0 and check == False:
                        tmp = tmp - 1
                        if game[tmp] != nextMove:
                            check = True
                    if check == False:
                        best_move = x
                    check = False
                    while tmp <= 7 and check == False:
                        tmp = tmp + 1
                        if game[tmp] != nextMove:
                            check = True
                    if check == False:
                        best_move = x
                        print(best_move)
                        found = True
                        exit(0)
                if x < 64 and x >= 56:
                    tmp = x + 0
                    check = False
                    while tmp >= 56 and check == False:
                        tmp = tmp - 1
                        if game[tmp] != nextMove:
                            check = True
                    if check == False:
                        best_move = x
                        print(best_move)
                        found = True
                        exit(0)
                    check = False
                    while tmp <= 63 and check == False:
                        tmp = tmp + 1
                        if game[tmp] != nextMove:
                            check = True
                    if check == False:
                        best_move = x
                        print(best_move)
                        found = True
                        exit(0)
                if x % 7 == 0:
                    tmp = x + 0
                    check = False
                    while tmp >= 7 and check == False:
                        tmp = tmp - 8
                        if game[tmp] != nextMove:
                            check = True
                    if check == False:
                        best_move = x
                        print(best_move)
                        found = True
                        exit(0)
                    check = False
                    while tmp <= 63 and check == False:
                        tmp = tmp + 8
                        if game[tmp] != nextMove:
                            check = True
                    if check == False:
                        best_move = x
                        print(best_move)
                        found = True
                        exit(0)
                if x % 8 == 0:
                    tmp = x + 0
                    check = False
                    while tmp >= 0 and check == False:
                        tmp = tmp - 8
                        if game[tmp] != nextMove:
                            check = True
                    if check == False:
                        best_move = x
                        print(best_move)
                        found = True
                        exit(0)
                    check = False
                    while tmp <= 56 and check == False:
                        tmp = tmp + 8
                        if game[tmp] != nextMove:
                            check = True
                    if check == False:
                        best_move = x
                        print(best_move)
                        found = True
                        exit(0)
                        #best_move = 11 + ((best_move // 8) * 10) + (best_move % 8)
                # enemy = findEnemy(nextMove)
                # if x%8 == 0 and game[16] != enemy and game[24] != enemy and game[32] != enemy and game[40] != enemy:
                #     best_move = x
                #     found = True
                #     print(best_move)
                #     exit(0)
                # if x%8 == 7 and game[23] != enemy and game[31] != enemy and game[39] != enemy and game[47] != enemy:
                #     best_move = x
                #     found = True
                #     print(best_move)
                #     exit(0)
                # if x <= 7 and game[2] != enemy and game[3] != enemy and game[4] != enemy and game[5] != enemy:
                #     best_move = x
                #     found = True
                #     print(best_move)
                #     exit(0)
                # if x>= 56 and game[58] != enemy and game[59] != enemy and game[60] != enemy and game[61] != enemy:
                #     best_move = x
                #     found = True
                #     print(best_move)
                #     exit(0)
                # else:
                #     movesCopy.remove(x)
            if len(movesCopy) != 0 and found == False:
                #best_move = movesCopy.pop()
                best_move = minimizeEnemyMoves(board,nextMove,movesCopy,lookUp)
                # if board.count(".") > 25:
                #     mostStable = -99
                #     for x in moves:
                #         tmp = makeMove(board,nextMove,x)
                #         if len(findStableMoves(tmp,nextMove,lookUp)) - len(findStableMoves(tmp,findEnemy(nextMove),lookUp)) > mostStable:
                #             best_move = x
                #             mostStable = len(findStableMoves(tmp,nextMove,lookUp)) - len(findStableMoves(tmp,findEnemy(nextMove),lookUp))
                # else:
                #     best_move = minimizeEnemyMoves(board, nextMove, moves, lookUp)

            elif found == False:
                best_move = minimizeEnemyMoves(board,nextMove,moves,lookUp)
                # best_move = moves.pop()
                # if board.count(".") > 25:
                #     mostStable = -99
                #     for x in moves:
                #         tmp = makeMove(board,nextMove,x)
                #         if len(findStableMoves(tmp,nextMove,lookUp)) - len(findStableMoves(tmp,findEnemy(nextMove),lookUp)) > mostStable:
                #             best_move = x
                #             mostStable = len(findStableMoves(tmp,nextMove,lookUp)) - len(findStableMoves(tmp,findEnemy(nextMove),lookUp))
                # else:
                #     best_move = minimizeEnemyMoves(board, nextMove, moves, lookUp)
        else:
            nm = negamaxTerminal(game,nextMove,-65,65,lookUp)
            best_move = nm[-1]
    print(best_move)

class Strategy:

    def best_strategy(self, board, player, best_move, still_running): #player is token, board i the gameboard
        #still running is timer running
        #best_move = stored best move overall
        lookUp = buildLookUp()
        game = ''.join(board).replace('?',"").replace("@","X").replace('o',"O")
        print(game)
        nextMove = "X" if player =="@" else 'O'
        for x in range(64):
            if game[x] == "x" or game[x] == "o":
                game = game[:x]+ game[x].upper()+game[x+1:]
        moves = findPossibleMoves(game,nextMove,lookUp)
        moves = list(moves)
        best_move.value = moves[0]
        best_move.value = 11 + ((best_move.value // 8) * 10) + (best_move.value % 8)
        if len(moves) == 0:
            print("No moves are possible")
        else:
            if 64-board.count("X")-board.count("O") >= 11:
                movesCopy = moves.copy()
                for x in moves:
                    if ((x==1 or x==8 or x==9) and (game[0] != nextMove)) or ((x==6 or x==15 or x==14) and game[7] != nextMove) \
                                or ((x == 48 or x == 57 or x==49) and game[56] != nextMove) or ((x==62 or x==55 or x==54) and game[63] != nextMove):
                        if len(movesCopy) != 1:
                            movesCopy.remove(x)
                moves = movesCopy.copy()
                for x in moves:
                    notRemoved = True
                    if x == 0 or x == 7 or x == 56 or x == 63:
                        best_move.value = x
                        best_move.value = 11 + ((best_move.value // 8) * 10) + (best_move.value % 8)
                    if x <= 7:
                        tmp = x+0
                        check = False
                        while tmp >= 0 and check == False:
                            tmp = tmp-1
                            if game[tmp] != nextMove:
                                check = True
                        if check == False:
                            best_move.value = x
                            best_move.value = 11 + ((best_move.value // 8) * 10) + (best_move.value % 8)
                        check = False
                        while tmp <= 7 and check == False:
                            tmp = tmp+1
                            if game[tmp] != nextMove:
                                check = True
                        if check == False:
                            best_move.value = x
                            best_move.value = 11 + ((best_move.value // 8) * 10) + (best_move.value % 8)
                    if x < 64 and x >= 56:
                        tmp = x+0
                        check = False
                        while tmp >= 56 and check == False:
                            tmp = tmp-1
                            if game[tmp] != nextMove:
                                check = True
                        if check == False:
                            best_move.value = x
                            best_move.value = 11 + ((best_move.value // 8) * 10) + (best_move.value % 8)
                        check = False
                        while tmp <= 63 and check == False:
                            tmp = tmp+1
                            if game[tmp] != nextMove:
                                check = True
                        if check == False:
                            best_move.value = x
                            best_move.value = 11 + ((best_move.value // 8) * 10) + (best_move.value % 8)
                    if x%7 == 0:
                        tmp = x+0
                        check = False
                        while tmp >= 7 and check == False:
                            tmp = tmp-8
                            if game[tmp] != nextMove:
                                check = True
                        if check == False:
                            best_move.value = x
                            best_move.value = 11 + ((best_move.value // 8) * 10) + (best_move.value % 8)
                        check = False
                        while tmp <= 63 and check == False:
                            tmp = tmp+8
                            if game[tmp] != nextMove:
                                check = True
                        if check == False:
                            best_move.value = x
                            best_move.value = 11 + ((best_move.value // 8) * 10) + (best_move.value % 8)
                    if x%8 == 0:
                        tmp = x+0
                        check = False
                        while tmp >= 0 and check == False:
                            tmp = tmp-8
                            if game[tmp] != nextMove:
                                check = True
                        if check == False:
                            best_move.value = x
                            best_move.value = 11 + ((best_move.value // 8) * 10) + (best_move.value % 8)
                        check = False
                        while tmp <= 56 and check == False:
                            tmp = tmp+8
                            if game[tmp] != nextMove:
                                check = True
                        if check == False:
                            best_move.value = x
                            best_move.value = 11 + ((best_move // 8) * 10) + (best_move % 8)
                    if (x%8 == 0 or x%7 == 0 or x < 7 or (x > 56 and x < 63)) and notRemoved == True and len(moves) != 1:
                        moves.remove(x)
                if len(moves) != 0:
                    # best_move.value = moves.pop()
                    mostStable = -99
                    for x in moves:
                        tmp = makeMove(board,nextMove,x)
                        if len(findStableMoves(tmp,nextMove,lookUp)) - len(findStableMoves(tmp,findEnemy(nextMove),lookUp)) > mostStable:
                            best_move = x
                            mostStable = len(findStableMoves(tmp,nextMove,lookUp)) - len(findStableMoves(tmp,findEnemy(nextMove),lookUp))
                    best_move.value = 11 + ((best_move.value // 8) * 10) + (best_move.value % 8)
                else:
                    # best_move.value = findPossibleMoves(game,nextMove,lookUp).pop()
                    mostStable = -99
                    for x in moves:
                        tmp = makeMove(board,nextMove,x)
                        if len(findStableMoves(tmp,nextMove,lookUp)) - len(findStableMoves(tmp,findEnemy(nextMove),lookUp)) > mostStable:
                            best_move = x
                            mostStable = len(findStableMoves(tmp,nextMove,lookUp)) - len(findStableMoves(tmp,findEnemy(nextMove),lookUp))
                    best_move.value = 11 + ((best_move.value // 8) * 10) + (best_move.value % 8)
            else:
                # nm = negamax(game, nextMove, 8)
                nm = negamaxTerminal(game,nextMove,-65,65,lookUp)
                best_move.value = nm[-1]
                best_move.value = 11+((best_move.value//8)*10)+(best_move.value%8)
if __name__ == "__main__":
    main()


