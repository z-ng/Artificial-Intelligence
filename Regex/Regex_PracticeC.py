import sys

probNum = int("".join(sys.argv[1]))
str = ""

if probNum == 31:
    str = r"/^100\b|^101\b|^0\b/"
if probNum == 32:
    str = "/^[0-1]+$/"
if probNum == 33:
    str = "/\w*0$/"
if probNum == 34:
    str = "/.*[aeiou].*[aeiou].*/i"
if probNum == 35:
    str = "/\w*0$/"
if probNum == 36:
    str = "/.*110.*/"
if probNum == 37:
    str = r"/^\w{2,4}\b/"
if probNum == 38:
    str = "/(.*\s*-?\s*[0-9]){9}/"
if probNum == 39: #might want to double check this
    str = "/^d\w*/i"
if probNum == 40:
    str = r"/\b0[01]*0\b|\b1[01]*1\b/"
if probNum == 41:
    str = r"/[PCKpck](\w+)/"
if probNum == 42:
    str = "/^.(..)*$/"
if probNum == 43:
    str = r"/\b(0([01][01])*)\b|\b(1)\b|\b(1)([01][01])*\b/"
if probNum == 44:
    str = "/^((?!110).)*$/"
if probNum == 45:
    str = r"/\b((0|1|x|o|X|o|.)(0|1|x|o|X|o|.)(0|1|x|o|X|o|.)(0|1|x|o|X|o|.)(0|1|x|o|X|o|.)(0|1|x|o|X|o|.)(0|1|x|o|X|o|.)(0|1|x|o|X|o|.)(0|1|x|o|X|o|.)(0|1|x|o|X|o|.)(0|1|x|o|X|o|.))\b/"
if probNum == 46:
    str = r"/\b[XOxo]*\.[XOxo]*\b/"
if probNum == 47:
    str = r"/\b[Xx]*\.\b|\b[Xx]*\.[Xx]*\b|\b[Xx][Oo]*\.\b|\b[XxOo]*\.[Oo]*[Xx]\b/"
if probNum == 48:
    str = r"/\b[abc]+\b/"
if probNum == 49:
    str = r"/\b([bc]*a[bc]*a[bc]*)+\b/"
if probNum == 50:
    str = r"/\b[02]*1[02]*1[02]*\b/"

if probNum == 51:
    str = r"/(.)\1{10}/"
if probNum == 52:
    str = r"/.*(.).*\1.*/"
if probNum == 53:
    str = r"/\b.*(.)\1{1}.*\b/"
if probNum == 54:
    str = r"/\b.*(.).*\1.*\b/"
if probNum == 55:
    str = r"/\b(.).*1.*\1\b|\b(1).*\2\b/"
print(str)