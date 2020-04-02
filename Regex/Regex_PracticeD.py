import sys

probNum = int(''.join(sys.argv[1]))
str = ""

if probNum == 31:
    str = r"/^100$|^101$|^0$/"
if probNum == 32:
    str = "/^[0-1]*$/"
if probNum == 33:
    str = "/\w*0$/"
if probNum == 34:
    str = "/\S*[aeiou]\S*[aeiou]\S*/i"
if probNum == 35:
    str = "/^1[0-1]*0$|^0$/"
if probNum == 36:
    str = "/^[0-1]*110[0-1]*$/g"
if probNum == 37:
    str = r"/^.{2,4}$/s"
if probNum == 38:
    str = r"/^[0-9]\s*[0-9]\s*[0-9]\s*-?\s*[0-9]\s*[0-9]\s*-?\s*[0-9]\s*[0-9]\s*[0-9]\s*[0-9]\s*$/"
if probNum == 39:
    str = "/^.*?d/im"
if probNum == 40:
    str = r"/\b0[01]*0\b|\b1[01]*1\b|\b1\b|\b0\b/"
if probNum == 41:
    str = r"/\b[PCKpck]\S*\b/gm"
if probNum == 42:
    str = "/^.(..)*$/s"
if probNum == 43:
    str = r"/^0(..)*$|^1(.)$|^1(.)(..)*$/"
if probNum == 44:
    str = r"/^(0*10+)*0*1*$/"
if probNum == 45:
    str = r"/^[XO.]{64}$/i"
if probNum == 46:
    str = r"/^[xo]*\.[xo]*$/i"
if probNum == 47:
    str = r"/^[x]*\.$|^[x]*\.[x]+$|^[x]+[o]*\.[xo.]*$|^[xo.]*\.[o]*[x]+$|^\..*$|^.*\.$/i"
if probNum == 48:
    str = r"/^[bc]+a?[bc]*$|^[bc]*a?[bc]+$|^a$/"
if probNum == 49:
    str = r"/^([bc]*a[bc]*a[bc]*)+$|^[bc]+$/"
if probNum == 50:
    str = r"/^(2|20*)+(1[02]*1[02]*)+[02]$|^(2|20*)*(1[02]*1[02]*)+[02]*$|^(2|20*)+(1[02]*1[02]*)*[02]*$|^(2|20*)*(1[02]*1[02]*)*[02]+$/"

if probNum == 51:
    str = r"/^.*(.)\1{9}.*$/si"
if probNum == 52:
    str = r"/(\w)\w*\1/i"
if probNum == 53:
    str = r"/\w*(\w)\1{1}\w*/"
if probNum == 54:
    str = r"/\w*(\w)\w*\1\w*/i"
if probNum == 55:
    str = r"/^(.)[01]*\1$|^0$|^1$/"

if probNum == 56:
    str = r"/cat\w{3}|\wcat\w{2}|\w{2}cat\w|\w{3}cat/i"
if probNum == 57:
    str = r"/(?<=^(.)).*\1$|^0$|^1$/"
if probNum == 58:
    #str = r"/\b([01])(([01])*)(?<=\1)\b/"
     str = r"/(?=^([10]).*\1$)|^0$|^1$/"
if probNum == 59:
    str = r"/\ba\w*[eiou]\b|\be\w*[aiou]\b|\bi\w*[aeou]\b|\bo\w*[aeiu]\b|\bu\w*[aeio]\b/i"
if probNum == 60:
    str = r"/^((?!011).)*$/"

print(str)