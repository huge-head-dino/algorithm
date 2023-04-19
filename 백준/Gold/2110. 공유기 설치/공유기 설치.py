import sys
input = sys.stdin.readline


N,C = map(int, input().split()) # N = 집의 갯수, C= 설치해야할 공유기 수

house = [None]*N    # 입력받은 집의 위치들이 모여있는 list

for i in range(N):    # house라는 빈 리스트에 입력받은 값 담기
    a =int(input())
    house[i]= a
house.sort()


def f(house,start,end):
    while start <= end:
        mid = (start+end) //2
        now = house[0]
        count = 1

        for i in range(1,len(house)):
            if house[i] >= now + mid:
                count += 1
                now = house[i]

        if count >= C:
            global result
            start = mid + 1
            result = mid
        else:
            end = mid -1
           
start = 1
end = house[-1]-house[0]
result = 0
f(house,start,end)
print(result)


