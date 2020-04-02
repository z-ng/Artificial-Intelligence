import sys
import time
import re

def buildRegex(wordString):
    regex = ""
    counter = 0 #counts number of spaces
    for x in wordString:
        if re.search(r"[A-Z]",x):
            if counter != 0:
              regex = regex + ".{"+str(counter)+"}"
              counter = 0
            regex = regex + x
        else:
            counter+=1
    if counter != 0:
      regex = regex + ".{"+str(counter)+"}"
    regex = r"^"+regex+r"$"
    return regex

def buildDctFrequency(dct):
    encodedDict = {}
    for word in dct:
        frequencyInWord = {}
        count = 0
        for letter in word:
            if letter not in frequencyInWord:
                frequencyInWord[letter] = count
                if isinstance(count, str):
                    count = chr(ord(count)+1)
                elif count > 9:
                    count = "A"
                else:
                    count+=1
        encodedString = ""
        for letter in word:
            encodedString = encodedString+str(frequencyInWord[letter])
        if encodedString not in encodedDict.keys():
            encodedDict[encodedString] = [word]
        else:
            encodedDict[encodedString].append(word.lower())
    return encodedDict

def trimDct(dct):
    tmpDct = []
    for word in dct:
        if re.search(r"^[A-Za-z]{1,99}[aeiouyAEIOUY][A-Za-z]{0,99}$|^[A-Za-z]{0,99}[aeiouyAEIOU][a-zA-Z]{1,99}$|^[aAIi]$",word):
            tmpDct.append(word.lower())
    dct.append("a")
    dct.append("i")
    return tmpDct

def trimPossibleWords(possibleWords,word):
    arr = []
    regex = buildRegex(word).lower()
    for x in possibleWords:
        if re.search(regex,x):
            arr.append(x)
    return arr

def encodeString(string):
    tmpArray = []
    for word in string:
        frequencyInWord = {}
        count = 0
        for letter in word:
            if letter not in frequencyInWord:
                frequencyInWord[letter] = count
                if isinstance(count, str):
                    count = chr(ord(count)+1)
                elif count > 9:
                    count = "A"
                else:
                    count+=1
        encodedString = ""
        for letter in word:
            encodedString = encodedString+str(frequencyInWord[letter])
        tmpArray.append(encodedString)
    return tmpArray

def recur(originalString,encodedString,builtString,index,encodedDict,foundLetters,dct):
        returnedLst = builtString
        word = encodedString[index]
        possibleWords = encodedDict[word]
        possibleWords = trimPossibleWords(possibleWords,builtString[index])
        for testWord in possibleWords:
            tmpFrequencyList = foundLetters.copy()
            tmpBuiltString = builtString[0:index] + [testWord.upper()] + builtString[index+1:]
            # print("Testing the word",testWord,"encoded is",originalString[index])
            # print("Testing the string",tmpBuiltString,index)
            isPossible = True
            letter = 0
            while isPossible == True and letter < len(testWord):
                # print(tmpFrequencyList,'frequency list')
                # print("Testing key",originalString[index][letter],"and value",testWord[letter])
                if originalString[index][letter] not in tmpFrequencyList.keys() and testWord[letter] not in tmpFrequencyList.values():
                    # print("Did not find",originalString[index][letter],':',testWord[letter],"in",tmpFrequencyList,'string still possible')
                    tmpFrequencyList[originalString[index][letter]] = testWord[letter]
                elif testWord[letter] in tmpFrequencyList.values() and originalString[index][letter] not in tmpFrequencyList.keys():
                    # print('Did not find',originalString[index][letter],"in keys but value",testWord[letter],"was found string not possible")
                    isPossible = False
                elif originalString[index][letter] in tmpFrequencyList.keys() and testWord[letter] != tmpFrequencyList[originalString[index][letter]]:
                    # print('Found',originalString[index][letter],"in keys and",testWord[letter],"did not match word string not possible")
                    isPossible = False
                letter+=1
            # print(isPossible)
            if isPossible == True:
                replacedString = []
                for wordInBuiltString in tmpBuiltString:
                    replacedWord = ""
                    for letterInBuiltString in wordInBuiltString:
                        if letterInBuiltString in tmpFrequencyList and letterInBuiltString.lower() == letterInBuiltString:
                            replacedWord = replacedWord+tmpFrequencyList[letterInBuiltString].upper()
                        else:
                            replacedWord = replacedWord+letterInBuiltString
                    replacedString.append(replacedWord)
                tmpBuiltString = replacedString.copy()
                # print(testWord,"is a possible word")
                # print(replacedString, "string", index, 'index')
                print(' '.join(replacedString))
                notPossible = False
                x = 0
                while x < len(builtString) and notPossible == False:
                    possibleWords = encodedDict[encodedString[x]]
                    if len(trimPossibleWords(possibleWords,builtString[x])) == 0:
                        notPossible = True
                    x+=1
                if notPossible == True:
                    return builtString
                if index == len(originalString)-1:
                    print(len(originalString))
                    print("\nFound the sentence:", tmpBuiltString)
                    print("Original Encoded Sentence:", ' '.join(originalString))
                    print("Frequency List", tmpFrequencyList)
                    print(' '.join(tmpBuiltString))
                    exit(0)
                # print(tmpBuiltString,"is a possible string")
                returnedLst = recur(originalString,encodedString,tmpBuiltString,index+1,encodedDict,tmpFrequencyList,dct)
                # print(returnedLst,maxWords,"returned")
        return returnedLst

string = ' '.join(sys.argv[1:]).lower()
# string = "NF JLGSMNBUDKL OGSUKM NK UB DGYK GS KMCZGUVBS QB QDK PKAU NK BCU BH QZDBBX".lower()
string = re.sub(r'[^\w\s]','',string)
print(string)
string = list(string.split())
dct = open("scrabble.txt",'r').read().splitlines()
print("Old Length",len(dct))
dct = trimDct(dct)

dct.append('a')
dct.append('i')
print("Trimmed Length",len(dct))
encodedDict = buildDctFrequency(dct)
encodedString = encodeString(string)
print(encodedString,"Encoded String")
start = time.time()


recur(string,encodedString,string,0,encodedDict,{}, dct)

print(time.time()-start)