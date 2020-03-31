import msvcrt
import sys


def findTurn(game):
    if game.count("X") <= game.count("O"):
        return "X"
    return "O"


def display(game):
    print(" ".join(game[0:3]))
    print(" ".join(game[3:6]))
    print(" ".join(game[6:9]))
    print("\n")

def isSolved(game,lst,t):
    for x in lst:
        if game[x[0]] == game[x[1]] == game[x[2]] and game[x[0]] == t:
            return True
        elif game[x[0]] == game[x[1]] == game[x[2]] and game[x[0]] != t and game[x[0]] != ".":
            return True
    if "." not in game:
        print("Tie")
        exit(0)
        return True
    return False

def partitionMoves(game, lst, t):
    for x in lst:
        if game[x[0]] == game[x[1]] == game[x[2]] and game[x[0]] == t:
            return set(), {"."}, set()
        elif game[x[0]] == game[x[1]] == game[x[2]] and game[x[0]] != t and game[x[0]] != ".":
            return {"."}, set(), set()
    if "." not in game:
        return set(), set(), {"."}
    else:
        move = findTurn(game)
        good, bad, tie = set(), set(), set()
        for x in range(9):
            if game[x] == ".":
                newGame = game[0:x] + move + game[x + 1:]
                tmpGood, tmpBad, tmpTie = partitionMoves(newGame, lst, move)
                if len(tmpGood) != 0:
                    bad.add(x)
                elif len(tmpTie) != 0:
                    tie.add(x)
                else:
                    good.add(x)
        return good, bad, tie
game = "........."
t = findTurn(game)
humanToken = "O"
if len(sys.argv) >= 2:
    if len(''.join(sys.argv[1])) > 2:
        game = ''.join(sys.argv[1])
    else:
        if ''.join(sys.argv[1]).upper() == "X":
            humanToken = "X"
        else:
            humanToken = "O"
    if len(sys.argv) >= 3:
        if len(''.join(sys.argv[2])) > 2:
            game = ''.join(sys.argv[2])
        else:
            if ''.join(sys.argv[2]).upper() == "X":
                humanToken = "X"
            else:
                humanToken = "O"
lst = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
lstOfIndex = ['0','1','2','3','4','5','6','7','8']
display(game)
if humanToken == findTurn(game):
    print("\rYour turn:",end= " ")
    s = ''+str(msvcrt.getche())[2:3]
    while s not in lstOfIndex:
        print("")
        print("\rThat is not a valid index, try again: ", end='')
        s = ''+str(msvcrt.getche())[2:3]
    while game[int(s)] != ".":
        print("")
        print("\rYour turn:", end=" ")
        s = ''+str(msvcrt.getche())[2:3]
        while s not in lstOfIndex:
            print("")
            print("\rThat is not a valid index, try again: ", end = '')
            s = ''+str(msvcrt.getche())[2:3]
    game = game[0:int(s)] + findTurn(game) + game[int(s) + 1:]
    print("")
    print("")
    display(game)

while True:
    for x in lst:
        if game[x[0]] == game[x[1]] == game[x[2]] and game[x[0]] == t:
            print(t,"has won")
            exit(0)
        elif game[x[0]] == game[x[1]] == game[x[2]] and game[x[0]] != t and game[x[0]] != ".":
            print(t,"has won")
            exit(0)
    if "." not in game:
        print("Its a tie!")
        exit(0)
    good, bad, tie = partitionMoves(game, lst, t)
    if len(good) > 0:
        index = good.pop()
    elif len(tie) > 0:
        index = tie.pop()
    else:
        index = bad.pop()
    game = game[0:index] + findTurn(game) + game[index + 1:]
    display(game)
    if isSolved(game,lst,findTurn(game)) == True:
        print(t,"has won")
        exit(0)
    print("\rYour turn:",end= " ")
    s = ''+str(msvcrt.getche())[2:3]
    while s not in lstOfIndex:
        print("")
        print("\rThat is not a valid index, try again: ", end='')
        s = ''+str(msvcrt.getche())[2:3]
    while game[int(s)] != ".":
        print("")
        print("\rYour turn:", end=" ")
        s = ''+str(msvcrt.getche())[2:3]
        while s not in lstOfIndex:
            print("")
            print("\rThat is not a valid index, try again: ", end = '')
            s = ''+str(msvcrt.getche())[2:3]
    game = game[0:int(s)] + findTurn(game) + game[int(s) + 1:]
    print("")
    print("")
    display(game)