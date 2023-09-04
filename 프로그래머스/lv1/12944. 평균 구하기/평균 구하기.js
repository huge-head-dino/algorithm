function solution(arr) {
    var answer = 0;
    let res = 0;
    for (let i = 0; i < arr.length; i++){
        res += arr[i]
    }
    answer = res / arr.length
    return answer;
}