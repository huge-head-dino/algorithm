function solution(s1, s2) {
    var answer = 0;
    let long = 0
    if(s1.length > s2.length){
        long = 1
    }else{
        long = 2
    }
    if(long === 1){
        for(let i = 0 ; i < s1.length; i++){
            if(s2.includes(s1[i])){
                answer += 1
            }
        }
    }else if(long ===2){
        for(let j = 0; j < s2.length; j++){
            if(s1.includes(s2[j])){
                answer += 1
            }
        }
    }   
    return answer;
}