import sys
input = sys.stdin.readline

XE = input()
X = list(XE.rstrip())

if X[0] == '0':

    if X[1] == 'x':
        hex = int(XE,16)
        print(hex) 
    else:
        oct = int(XE,8)
        print(oct)

else:
    print(XE)

