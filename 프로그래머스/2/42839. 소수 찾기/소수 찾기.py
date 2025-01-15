import math
import itertools

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    
    for i in range(5, int(math.sqrt(n)) + 1 ,6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True


def solution(numbers):
    answer = []
    cnt = 0
    examples = set()
    for r in range(1,len(numbers) + 1):
        for p in itertools.permutations(numbers,r):
            example = int("".join(p))
            examples.add(example)
    
    for i in examples:
        if is_prime(i) == True:
            answer.append(i)
            cnt += 1
    return cnt