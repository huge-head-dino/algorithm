function solution(n)
{
    var answer = 0;
    let res = n.toString()
    let a = res.length
    for (let i = a; i >= 1 ; i--)
    {
        let b = 10 ** (i-1)
        let sorc = Math.floor(n / b)
        console.log(sorc)
        answer += sorc
        n = n - (b*sorc)
    }

    return answer;
}