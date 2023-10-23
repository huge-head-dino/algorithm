def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            kim = numbers[i] + numbers[j]
            answer.append(kim)
    temp = list(set(answer))
    temp.sort()
    answer = temp
    return answer