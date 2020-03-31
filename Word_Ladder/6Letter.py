import sys
import time

input = ''.join(sys.argv[1:])
start = time.time()
dict = {}
edge = 0
with open("6letter.txt","r") as ins:
    for lines in ins:
        dict[str(lines)[0:6]] = set()
        for word in dict.keys():
            count = 0
            for x in range(0, len(word), 1):
                if str(lines)[x:x + 1] == str(word)[x:x + 1]:
                    count = count + 1
            if count == 5:
                dict[str(lines)[0:6]].add(word[0:6])
                if str(lines)[0:6] not in dict.get(word[0:6]):
                    edge = edge+1
                dict[str(word)[0:6]].add(str(lines)[0:6])
print("Time to construct",time.time()-start)
max = 0
maxset = set()
boolean = False
for key in dict:
    if len(dict.get(key)) == max:
        maxset.add(key)
    elif len(dict.get(key)) > max:
        maxset.clear()
        max = len(dict.get(key))
        maxset.add(key)
print("Number of keys",len(dict.keys()))


connection = {}
seen = set() #

for key in dict.keys(): #iterates through keys
    if key not in seen:
        connection[key] = set()
        seen.add(str(key))
        parseMe = list(dict.get(key))
        move = 0
        while len(parseMe) > move:
            if str(parseMe[move]) not in seen:
                parseMe = parseMe + list(dict.get(parseMe[move]))
                seen.add(str(parseMe[move]))
                connection[key].add(parseMe[move])
            move = move+1
connect = len(connection.keys())
maxconnect = 0
for key, value in connection.items():
    if len(value) > maxconnect:
        maxconnect = len(value)
if maxconnect != 0:
    maxconnect = maxconnect+1

print("# of connections",str(connect))
print("max connection",str(maxconnect))
print("# of edges:", str(edge))
if dict.get(input) != None:
    print("For",input,dict.get(input),"are neighbors")
else:
    print("There are no neighbors for:",input)
print(maxset,"all have",max,"neighbors")
print("Time to run",str(time.time()-start))