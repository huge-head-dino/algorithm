function solution(arr, divisor) {
    var answer = [];
    for(let i = 0; i < arr.length; i++){
        if(arr[i] % divisor == 0){
            answer.push(arr[i])
        }
    }
    if(answer[0] == undefined){
        return [-1]
    }
    answer.sort((a,b)=>a-b)
    return answer;
}