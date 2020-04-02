import sys

probNum = int("".join(sys.argv[1]))

str = ""
if probNum == 41:
    str = r"[PCKpck](\w+)"
if probNum == 42:
    str = "^.(..)*$"
if probNum == 43:
    str = "0((0|1)(0|1))*|1(0|1)((0|1)(0|1))*"
if probNum == 44:
    str = "^((?!110).)*$"
if probNum == 45:
    str = r"^((0|1|x|o|X|o|.)(0|1|x|o|X|o|.)(0|1|x|o|X|o|.)(0|1|x|o|X|o|.)(0|1|x|o|X|o|.)(0|1|x|o|X|o|.)(0|1|x|o|X|o|.)(0|1|x|o|X|o|.)(0|1|x|o|X|o|.)(0|1|x|o|X|o|.)(0|1|x|o|X|o|.))$"
if probNum == 46:
    str = r"[XOxo]*\.[XOxo]*"
if probNum == 47:
    str = ""
if probNum == 48:
    str = r"\b[bc]*a[bc]*\b"
if probNum == 49: #prob not right
    str = r"\b[bc]*a[bc]*a[bc]*\b"
if probNum == 50:
    str = ""
print(str)