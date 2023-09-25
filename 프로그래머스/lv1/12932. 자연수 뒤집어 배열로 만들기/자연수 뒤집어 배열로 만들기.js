function solution(n) {
    var answer = [];
//     스플릿 걸고 리버스
    let str_n = n.toString()
    let a = str_n.split('')
    let for_answer = a.reverse()
    answer = for_answer.map(Number)
    return answer;
}