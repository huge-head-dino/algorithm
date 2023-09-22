function solution(sizes) {
    var answer = 0;
    let sero = []
    let garo = []
    for(let i = 0 ; i < sizes.length; i++){
        let a = sizes[i][0]
        let b = sizes[i][1]
        if(a > b){
            sero.push(a)
            garo.push(b)
        }else{
            sero.push(b)
            garo.push(a)
        }
    }
    console.log(sero)
    console.log(garo)
    let H = Math.max(...sero)
    let W = Math.max(...garo)
    let res = H * W
    return res;
}