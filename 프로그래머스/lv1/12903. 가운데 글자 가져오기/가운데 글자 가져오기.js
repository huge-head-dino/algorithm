function solution(s) {
    var answer = '';
    let long = s.length
    if(long % 2 != 0){
        answer = s[Math.floor(long/2)]
    } else {
        console.log(long)
        answer = s.substr((long/2)-1,2)
    }
    return answer;
}