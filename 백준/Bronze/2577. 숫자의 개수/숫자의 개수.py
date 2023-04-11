a = int(input())
b = int(input())
c = int(input())

d = a * b * c
num_str = str(d)

count_list = [0] * 10

for c in num_str:
    num = int(c)
    count_list[num] += 1

zero_count = count_list[0]  # 0이 나온 횟수 구하기
print(zero_count)

for i in range(1, 10):
    print(count_list[i])
