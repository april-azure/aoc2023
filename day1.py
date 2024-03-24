from typing import List, Optional


def get_digit(line: str, order: int):
    for i in line[::order]:
        if i.isdigit():
            return int(i)

def q1() -> None:
    lines = []
    with open('input.txt') as file:
        lines = file.readlines()
    
    sum = 0
    for line in lines:
        f = get_digit(line, 1)
        l = get_digit(line, -1)

        sum += (f * 10 + l)
    print(sum)



MAP = {
    'one' : 1,
    'two' : 2,
    'three' : 3,
    'four' : 4, 
    'five' : 5,
    'six' : 6,
    'seven' : 7, 
    'eight' : 8, 
    'nine' : 9,
}
def get_number(line: str, index: int) -> Optional[int]:
    # check if line[index] is a number or not
    if line[index].isdigit():
        return int(line[index])
    
    for i in range(index+1, len(line)):
        if line[index: i+1] in MAP: 
            return MAP[line[index: i+1]]

    return None


def q2() -> None:
    lines = []
    with open('input.txt') as file:
        lines = file.readlines()
    numbers = []
    for line in lines:
        cur_numbers = []
        for i in range(len(line)):
            v = get_number(line, i)
            if v is not None:
                cur_numbers.append(v)
        numbers.append(cur_numbers)
    
    sum = 0
    for nums in numbers: 
        f = nums[0]
        l = nums[-1]
        sum += (f * 10 + l)
    
    print(sum)

# q1()
q2()