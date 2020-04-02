import sys

probNum = int(''.join(sys.argv[1]))
if probNum == 31:
    str = r"/^100\b|^101\b|^0\b/"
if probNum == 32:
    str = "/^[0-1]+$"
if probNum == 33:
    str = "/\w*0$/"
if probNum == 34:
    str = "/.*[aeiou].*[aeiou].*/i"
if probNum == 35:
    str = "/\w*0$/"
if probNum == 36:
    str = "/.*110*./"
if probNum == 37:
    str = r"/^\w{2,4}\b/"
if probNum == 38:
    str = "/\s*\-?[0-9]\s*\-?[0-9]\s*\-?[0-9]\s*\-?\s*\-?[0-9]\s*\-?\s*\-?[0-9]\s*\-?[0-9]\s*\-?[0-9]\s*\-?\s*\-?[0-9]\s*\-?\s*\-?[0-9]\s*\-?/"
if probNum == 39:
    str = "/\^d\w*/i"
if probNum == 40:
    str = r"\b0[01]*0\b|\b1[01]*1\b"
print(str)
