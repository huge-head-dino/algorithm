function solution(arr)
{
    let right_arr = []
    let real_arr = arr.length
    for (let i = 0 ; i < real_arr; i++){
        if(arr[i]!==arr[i+1]){
            right_arr.push(arr[i])
        }
    }
    return right_arr;
}