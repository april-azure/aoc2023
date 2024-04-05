def q1():
    lines = []
    with open('input.txt') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]

    times = get_ints(lines[0])
    distance = get_ints(lines[1])

    res = 1
    for time, dist in zip(times, distance):
        x = get_race(time, dist)
        res = x * res
    print(res)

def get_race(time, distance):
    cnt = 0
    for i in range(time):
        speed = i
        r = time - i
        if speed * r > distance:
            cnt += 1
    return cnt

def get_ints(line):
    t: str = line.split(':')[1]
    parts = t.strip().split(' ')
    return [int(x) for x in parts if x]

def q2():
    lines = []
    with open('input.txt') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    lines = [line.replace(" ","") for line in lines]
    time = int(lines[0].split(':')[1])
    distance = int(lines[1].split(':')[1])
    low = race_min(time, distance)
    high = race_max(time, distance)
    print(low, high)

    print(high-low+1)

def race_min(time, dis):
    lo=0
    high=time
    while True:
        mid = (lo+high) // 2 + 1
        print(lo, high, mid)
        if not can_reach(time,dis,mid-1) and can_reach(time,dis,mid):
            return mid
        # breakpoint()
        if not can_reach(time, dis, mid):
            lo=mid+1
        else:
            high=mid

def can_reach(time, dis, speed):
    return speed * (time - speed) >= dis


def race_max(time, dis):
    lo=0
    high=time
    while True:
        mid = (lo+high) // 2        
        print(lo, high, mid)
        
        if can_reach(time,dis,mid) and not can_reach(time,dis,mid + 1):
            return mid
        if can_reach(time, dis, mid):
            lo=mid+1
        else:
            high=mid-1

q2()