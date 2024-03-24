
def q1() -> None:
    lines = []
    with open('input.txt') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    
    sum = 0
    for line in lines:
        p = line.split(':')[1].strip()
        parts = p.split('|')
        targets = get_nums(parts[0])
        currents = get_nums(parts[1])
        cnt = find_match_cnt(targets, currents)
        if cnt != 0:
            sum += (2 ** (cnt-1))
    print(sum)

def get_nums(val):
    vals = val.strip().split(' ')
    return [int(x) for x in vals if x]

def find_match_cnt(targets, currents):
    cnt = 0
    for x in currents:
        if x in targets:
            cnt += 1
    return cnt

def q2():
    lines = []
    with open('input.txt') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    
    cnts = [0] * len(lines)
    for i in range(len(lines)):
        line = lines[i]
        p = line.split(':')[1].strip()
        parts = p.split('|')
        targets = get_nums(parts[0])
        currents = get_nums(parts[1])
        cnt = find_match_cnt(targets, currents)
        # print("row",i, cnt)
        copy = cnts[i]
        if cnt == 0:
            continue
        for next_i in range(i+1, min(len(lines)+1,i+1+cnt)):
            cnts[next_i] += (copy+1)
    # print(cnts)
    print(sum(cnts) + len(lines))
q2()
