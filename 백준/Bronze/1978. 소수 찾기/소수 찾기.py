T = int(input())

number_list = list(map(int, input().split()))

result = 0

def prime_num(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
        
    return True

for i in number_list:
    a = prime_num(i)
    if a == True:
        result += 1
    else:
        pass

print(result)






