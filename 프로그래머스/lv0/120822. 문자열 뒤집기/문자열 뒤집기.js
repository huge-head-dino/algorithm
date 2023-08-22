function solution(my_string) {
    var answer = '';
    a = my_string.split("")
    a.reverse()
    b = a.join('')
    answer = b
    return answer;
}