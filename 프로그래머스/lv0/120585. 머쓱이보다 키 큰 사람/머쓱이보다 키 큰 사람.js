function solution(array, height) {
    var answer = 0;
    let arr = []
    for(let i = 0; i<array.length; i++){
        a = array[i]
        if(a > height){
            arr.push(a)
        }
    }
    answer = arr.length
    
    return answer;
}