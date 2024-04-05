from typing import List, Tuple


def q1() -> None:
    lines = []
    with open('input.txt') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]

    # get seeds 
    seeds = [int(i) for i in lines[0].split(':')[1].strip().split(' ')]
    map = []
    indexes = [ i for i in range(1, len(lines)) if not lines[i]] + [len(lines)]
    # print(indexes)
    for i in range(len(indexes)-1):
        cur = lines[indexes[i]+1:indexes[i+1]]
        # print(cur)
        temp = get_map(cur)
        source, dest, sdmap = temp
        map.append(sdmap)
    dests = []
    for seed in seeds:
        source = seed
        for sdmap in map:
            source = get_dest(sdmap, source)
        dests.append(source)
    print(min(dests))

def get_map(lines: List[str]) -> Tuple[str, str, List[Tuple[int, int, int]]]:
    first_line = lines[0]
    parts = first_line.split(' ')[0].split('-')
    source = parts[0]
    dest = parts[2]
    map = []
    for line in lines[1:]:
        parts = line.split(' ')
        dest_range = int(parts[0])
        source_range = int(parts[1])
        r = int(parts[2])
        map.append((dest_range, source_range, r))
    map.sort(key=lambda x: x[0])
    return (source, dest, map)

def get_dest(map: List[Tuple[int, int, int]], source: int) -> int:
    for line in map: 
        dest_start, source_start, r = line
        if source >= source_start and source < source_start + r:
            return dest_start + (source - source_start)
    return source

# q1()


def get_map2(lines: List[str]) -> Tuple[str, str, List[Tuple[int, int, int]]]:
    first_line = lines[0]
    parts = first_line.split(' ')[0].split('-')
    source = parts[0]
    dest = parts[2]
    map = []
    for line in lines[1:]:
        parts = line.split(' ')
        dest_range = int(parts[0])
        source_range = int(parts[1])
        r = int(parts[2])
        map.append((source_range, dest_range, r))
    map.sort(key=lambda x: x[0])
    return (source, dest, map)

def q2():
    lines = []
    with open('input.txt') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]

    # get seeds 
    seeds = [int(i) for i in lines[0].split(':')[1].strip().split(' ')]
    map = []
    indexes = [ i for i in range(1, len(lines)) if not lines[i]] + [len(lines)]
    # print(indexes)
    for i in range(len(indexes)-1):
        cur = lines[indexes[i]+1:indexes[i+1]]
        # print(cur)
        temp = get_map(cur)
        source, dest, sdmap = temp
        map.append(sdmap)
    dests = []
    i = 0
    while i < len(seeds):
        for seed in range(seeds[i], seeds[i]+seeds[i+1]):
            ...
        i+=2
    print(min(dests))


q2()