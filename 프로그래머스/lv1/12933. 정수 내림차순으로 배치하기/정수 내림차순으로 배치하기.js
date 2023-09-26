function solution(n) {
    var answer = 0;
    let m = n.toString()
    let array = m.split('')
    let new_array = array.sort((a,b) => (b-a))
    
    answer = Number(new_array.join(''))
    return answer;
}