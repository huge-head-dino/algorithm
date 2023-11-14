def solution(myString):
    answer = ''
    myString = list(myString)
    alpha =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for idx, val in enumerate(myString):
        if alpha.index(val) < alpha.index('l'):
            myString[idx] = 'l'
    answer = myString
    answer = ''.join(answer)
    return answer