function solution(d, budget) {
    var answer = 0;
    let res = 0 
    d.sort((a,b)=> a - b)
    for(let i = 0; i < d.length; i++){
        res += d[i]
        if(res <= budget){
            answer += 1
        } else {
            break
        }
    }
    return answer;
}