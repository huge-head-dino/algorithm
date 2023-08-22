function solution(slice, n) {
    var answer = 0;
    let defaults = Math.floor(n / slice)
    if(n % slice > 0){
        defaults += 1
    }
    answer = defaults
    return answer;
}