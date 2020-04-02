import sys

probNum = int(''.join(sys.argv[1]))
if probNum == 1:
    str = r""
if probNum == 2:
    str = r"^(.)(.).*\2\1$"
if probNum == 3:
    str = r"\b(.).*\1.*\1.*\1.*\b"
if probNum == 4:
    str = ""
if probNum == 5:
    str = ""
if probNum == 6:
    str = ""
print(str)
