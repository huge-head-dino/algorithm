import sys
input = sys.stdin.readline

global T
T = int(input())



def f(b):
    count = 1
    for _ in range(100):
        eee= list(str(b).zfill(2))
        munju = int(eee[0])+int(eee[1])
        munju_list = list(str(munju).zfill(2))
        b = int(eee[1] + munju_list[1])
    # for _ in range(100):
        if b != T:
            count += 1
            
        elif b == T:
            print (count)
            break
        else:
            pass
            
    

jb= f(T)