function solution(n, k) {
    var answer = 0;
    let yang = 12000 * n
    let bev = 2000 * k
    if(Math.floor(n/10) != 0){
        serv = Math.floor(n/10)
        bev = bev - (2000*serv)
    }
    answer = yang + bev
    return answer;
}