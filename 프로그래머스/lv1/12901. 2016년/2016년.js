function solution(a, b) {
    var answer = '';
    let numbers = [31,29,31,30,31,30,31,31,30,31,30,31]
    let day = numbers.slice(0,a-1)
    let day_sum = 0
    day.forEach(num=>day_sum+=num)
    let res = day_sum + b
    console.log(res)
    let rest = res % 7

    if(rest == 1){return 'FRI'}
    if(rest == 2){return 'SAT'}
    if(rest == 3){return 'SUN'}
    if(rest == 4){return 'MON'}
    if(rest == 5){return 'TUE'}
    if(rest == 6){return 'WED'}
    if(rest == 0){return 'THU'}
}