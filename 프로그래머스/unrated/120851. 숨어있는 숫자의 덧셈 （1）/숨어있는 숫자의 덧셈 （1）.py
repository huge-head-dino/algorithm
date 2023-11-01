import re
import math
def solution(my_string):
    answer = re.findall(r'\d', my_string)
    print(answer)
    answer = [int(i)for i in answer]
    return sum(answer)