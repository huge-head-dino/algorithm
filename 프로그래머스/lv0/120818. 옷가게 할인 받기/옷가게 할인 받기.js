function solution(price) {
    var answer = 0;
    if(price >= 100000 && price < 300000){
        answer = price - (price/100*5)
    }else if(price >= 300000 && price < 500000){
        answer = price - (price/100*10)
    }else if(price >= 500000){
        answer = price - (price/100*20)
    }else{
        answer = price
    }
    return Math.floor(answer);
}