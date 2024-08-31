def solution(a, b, c):
    answer = 0
    if (a == b or a == c or b == c) and (a != c or a!= b or b!=c):
        answer = (a+b+c) * (a**2 + b**2 + c**2)
        print(a**2)
    elif a != b and b != c and a != c:
        answer = (a + b + c) 
    elif a == b and a == c and b == c:
        answer = (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
        print(a**2)
    return answer