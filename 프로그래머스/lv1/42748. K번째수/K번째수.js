function solution(array, commands) {
    // i부터 j까지 자르고, 
    // 정렬
    // k번째에 있는 수를 도출
    var answer = [];
    for(let a = 0; a < commands.length; a++){
        let i = commands[a][0] 
        let j = commands[a][1]
        let k = commands[a][2]
        let new_arr = array.slice(i-1,j)
        new_arr.sort((a,b)=>a-b)
        let res = new_arr[k-1]
        answer.push(res)
    }
    return answer;
}