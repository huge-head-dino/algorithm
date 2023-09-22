function solution(t, p) {
    var answer = 0;
    const P_number = Number(p)
    let re = t.length - (p.length-1)
    
    for(let i = 0; i< re; i++){
        let a = t.substr(i,p.length)
        let T_number = Number(a)
        
        if(T_number <= P_number){
            answer += 1
        }
    }
   
    return answer;
}