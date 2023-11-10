import sys
input = sys.stdin.readline

A = list(input().rstrip())
alpha ={'A':2,'B':2,'C':2,'D':3,'E':3,'F':3,'G':4,'H':4,'I':4,'J':5,'K':5,'L':5,'M':6,'N':6,'O':6,'P':7,'Q':7,'R':7,'S':7,'T':8,'U':8,'V':8,'W':9,'X':9,'Y':9,'Z':9}

# 각 숫자에 대응 하는 알파벳묶음과 숫자를 매칭시킨다
# 주어진 문자열을 하나씩 풀어낸다.
# 알파벳에 대응하는 숫자를 전부 더하고 len(S)를 더한다.
sum = 0
for i in A:
    sum += alpha[i]

print(sum+len(A))

