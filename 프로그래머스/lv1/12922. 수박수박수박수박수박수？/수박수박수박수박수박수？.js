function solution(n) {
    var answer = '';
    let wat = '수박'
    if(n % 2 == 0){
        answer = wat.repeat(Math.floor(n/2))
    } else{
        answer = wat.repeat((n-1)/2).concat('수')
    }
    return answer;
}