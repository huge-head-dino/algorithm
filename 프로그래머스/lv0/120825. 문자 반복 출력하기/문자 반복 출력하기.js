function solution(my_string, n) {
    var answer = '';
    let arr = []
    for(let i = 0; i< my_string.length; i++){
        a = my_string[i].repeat(n)
        arr.push(a)
    }
    answer = arr.join('')
    return answer;
}