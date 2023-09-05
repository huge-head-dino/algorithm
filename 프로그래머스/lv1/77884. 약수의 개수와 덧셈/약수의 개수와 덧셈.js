function solution(left, right) {
    var answer = 0;
    let yaknum = 0
    for(let i = left; i<=right; i++){
        for(let j= 1; j<=(i/2); j++){
            if(i % j== 0){
                yaknum += 1
            }
        }
          yaknum += 1
            if(yaknum % 2 == 0){
                answer += i
            }else{
                answer -= i
            }
        yaknum = 0
    }
    return answer;
}