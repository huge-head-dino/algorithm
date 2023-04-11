import math
A, B, V = map(int,input().split())

def calculate_i(A,B,V):

    return math.ceil((V-B)/(A-B))

i= calculate_i(A,B,V)
print(i)