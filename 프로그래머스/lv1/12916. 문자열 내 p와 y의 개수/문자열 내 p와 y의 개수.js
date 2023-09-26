function solution(s){
    var answer = true;
//  s에 p의 개수와 y의 개수 비교 같으면 True
    let a = s.toUpperCase()
    let p_num = 0
    let y_num = 0
    
    for(let i=0; i < a.length; i ++){
        if(a[i] == 'P'){
            p_num += 1}
        if(a[i] == 'Y'){
            y_num += 1}
    }
    if(p_num == y_num){
        return true
    }else{
        return false       
    }
}