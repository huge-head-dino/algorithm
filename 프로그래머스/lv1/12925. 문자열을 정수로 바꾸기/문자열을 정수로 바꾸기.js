function solution(s) {
    var answer = 0;
//     S는 문자열이니까 맨 앞에 부호를 분리해내고
//     -가 붙어있다면, map -> Number 2연타
//     +가 붙어있다면, 그냥 +를 떼고 출력
    let s_list = s.split('')
    if(s_list[0] == '-'){
        let just = Number(s)
        // return just
    }
    if(s_list[0] == '+'){
        s_list.shift()
        let doit = s_list.join('')
        console.log(doit)
        // return doit
    }
    let res = Number(s)
    return res;
}