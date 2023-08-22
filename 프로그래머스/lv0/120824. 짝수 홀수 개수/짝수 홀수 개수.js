function solution(num_list) {
    let odd = 0
    let even = 0
    var answer = [];
    
    for(let i = 0; i < num_list.length ; i++){
        a = num_list[i]
        if (a % 2 === 0){
            even += 1
        } else {
            odd += 1
        }
    }
    
    answer.push(even)
    answer.push(odd)    
    return answer;
}