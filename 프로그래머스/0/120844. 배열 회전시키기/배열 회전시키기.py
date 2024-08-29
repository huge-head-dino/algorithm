def solution(numbers, direction):
    if direction == 'right':
        a = numbers.pop()
        numbers.insert(0,a)
    elif direction == 'left':
        b = numbers.pop(0)
        numbers.append(b)
    return numbers