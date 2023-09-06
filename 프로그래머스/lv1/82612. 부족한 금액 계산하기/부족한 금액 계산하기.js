function solution(price, money, count) {
    var answer = 0;
    let res = 0
    for(let i = 1; i <= count; i++){
        let a = price * i
        res += a
    }
    if(res > money){
        answer = res - money
    } else {
        answer = 0
    }
    return answer;
}