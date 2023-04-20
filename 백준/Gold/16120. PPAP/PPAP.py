import sys
input = sys.stdin.readline

P = input().strip()

if P=='P' or P=='PPAP':
    print("PPAP")
else:
    stack = []
    ppap = ['P','P','A','P']
    for i in P:
        stack.append(i)
        if stack[-4:] == ppap:
                stack.pop()
                stack.pop()
                stack.pop()

    if stack == ppap or stack == ["P"]:
        print("PPAP")
    else:
        print("NP")
