function solution(numbers) {
    var answer = 0;
    b = numbers.sort((a,b) => a-b)
    arg1 = b.pop()
    arg2 = b.pop()
    answer = arg1 * arg2
    return answer;
}