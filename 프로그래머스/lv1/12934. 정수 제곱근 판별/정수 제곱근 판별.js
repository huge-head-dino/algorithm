function solution(n) {
    var answer = 0;
    let sqrt = Math.sqrt(n);
    if(sqrt % 1 !== 0){
        return -1
    }
    let a = sqrt + 1
    let res = Math.pow(a,2)
    return res
    
    
    
    
    
    return answer;
}