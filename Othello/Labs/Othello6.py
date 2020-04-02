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
    if totalTokens(game)%2 == 0:
        nextMove = "X"
    else:
        nextMove = "O"
for x in range(64):
    if game[x] == "x" or game[x] == "o":
        game = game[:x]+ game[x].upper()+game[x+1:]
display(game)
print(game)
moves = findPossibleMoves(game,nextMove)
moves = list(moves)
if len(moves) == 0:
    print("No moves are possible")
else:
    for x in moves:
        notRemoved = True
        if x == 0 or x == 7 or x == 56 or x == 63:
            print(x)
            exit(0)
        if ((x==1 or x==8 or x==9) and (game[0] != nextMove)) or ((x==6 or x==15 or x==14) and game[7] != nextMove) \
                    or ((x == 48 or x == 57 or x==49) and game[56] != nextMove) or ((x==62 or x==55 or x==54) and game[63] != nextMove):
            if len(moves) != 1:
                moves.remove(x)
                notRemoved = False
        if x <= 7:
            tmp = x+0
            check = False
            while tmp >= 0 and check == False:
                tmp = tmp-1
                if game[tmp] != nextMove:
                    check = True
            if check == False:
                print(x)
                exit(0)
            check = False
            while tmp <= 7 and check == False:
                tmp = tmp+1
                if game[tmp] != nextMove:
                    check = True
            if check == False:
                print(x)
                exit(0)
        if x < 64 and x >= 56:
            tmp = x+0
            check = False
            while tmp >= 56 and check == False:
                tmp = tmp-1
                if game[tmp] != nextMove:
                    check = True
            if check == False:
                print(x)
                exit(0)
            check = False
            while tmp <= 63 and check == False:
                tmp = tmp+1
                if game[tmp] != nextMove:
                    check = True
            if check == False:
                print(x)
                exit(0)
        if x%7 == 0:
            tmp = x+0
            check = False
            while tmp >= 7 and check == False:
                tmp = tmp-8
                if game[tmp] != nextMove:
                    check = True
            if check == False:
                print(x)
                exit(0)
            check = False
            while tmp <= 63 and check == False:
                tmp = tmp+8
                if game[tmp] != nextMove:
                    check = True
            if check == False:
                print(x)
                exit(0)
        if x%8 == 0:
            tmp = x+0
            check = False
            while tmp >= 0 and check == False:
                tmp = tmp-8
                if game[tmp] != nextMove:
                    check = True
            if check == False:
                print(x)
                exit(0)
            check = False
            while tmp <= 56 and check == False:
                tmp = tmp+8
                if game[tmp] != nextMove:
                    check = True
            if check == False:
                print(x)
                exit(0)
        if (x%8 == 0 or x%7 == 0 or x < 7 or (x > 56 and x < 63)) and notRemoved == True and len(moves) != 1:
            moves.remove(x)
    if len(moves) != 0:
        print(moves.pop())
    else:
        print(findPossibleMoves(game,nextMove).pop())