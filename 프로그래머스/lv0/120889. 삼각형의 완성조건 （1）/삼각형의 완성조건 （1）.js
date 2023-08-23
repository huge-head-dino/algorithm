function solution(sides) {
    var answer = 0;
    let new_sides = sides.sort((a,b)=>a-b)
    console.log(new_sides)
    let a = new_sides[2] >= new_sides[1] + new_sides[0] ? 2 : 1
    answer = a
    return answer;
}