n, x = map(int, input().split())

number_list = list(map(int, input().split()))

b= []

for i in range(n):
    if number_list[i] < x: b.append(number_list[i])

for i in b:
    print(i, end=" ")

