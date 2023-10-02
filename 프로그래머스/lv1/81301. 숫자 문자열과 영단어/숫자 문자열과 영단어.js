function solution(s) {
    let numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
    // 그냥 숫자가 들어왔을 때를 생각해야함
    let answer = s
    for(let i=0; i < numbers.length; i++){
        let array = answer.split(numbers[i])
        answer = array.join(i)
    }
     
    return Number(answer);
}