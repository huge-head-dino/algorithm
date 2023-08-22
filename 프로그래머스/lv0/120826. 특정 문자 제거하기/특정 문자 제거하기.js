function solution(my_string, letter) {
    var answer = '';
    b = my_string.split('')
    
    let FN = b.filter(function(item){
        return item != letter
    })
    
    c = FN.join('')
    answer = c
    return answer;
}