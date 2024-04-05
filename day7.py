from collections import Counter
from functools import cmp_to_key

def q1():
    lines = []
    with open('input.txt') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]

    lines = sorted(lines, key=cmp_to_key(compare))

    # print(lines)
    score = 0
    for i, line in enumerate(lines):
        s = int(line.split(' ')[1])
        # print(s)
        score += (i+1) * s
    print(score)


def compare(l, r):
    card_l = l.split(' ')[0]
    card_r = r.split(' ')[0]
    return compare_card(card_l, card_r)

def get_rank(r):
    if isinstance(r, int): return r
    m = {
        'five': 9,
        'four': 8,
        'full house': 7, 
        'three': 6,
        'two pair': 5,
        'one pair': 4, 
        'high card': 3,
    }
    return m[r]

def compare_rank(l, r):
    rl = get_rank(l)
    rr = get_rank(r)
    return rl - rr

def get_card_score(c:str):
    if c.isnumeric():
        return int(c)-0
    m = {
        'T': 10,
        'J': -1,
        'Q': 12,
        'K': 13, 
        'A': 14
    }
    return m[c]


def compare_card(l, r):
    tl = get_type2(l)
    tr = get_type2(r)

    if compare_rank(tl, tr) != 0:
        return compare_rank(tl, tr)

    socres = [
        get_card_score(x) - get_card_score(y)
        for x,y in zip(l, r)
    ]
    socres=list(filter(lambda x: x!=0, socres))
    return socres[0]
    

def get_type(cards: str):
    c = Counter(cards)
    if len(c) == 1:
        return 'five'
    if (len(c)) == 2:
        a,b=c.most_common()
        if a[1] == 4:
            return 'four'
        else:
            return 'full house'
    if len(c) == 3:
        x,y,z,=c.most_common()
        if x[1] == 3:
            # three of a kind
            return 'three'
        # two pair
        return 'two pair'
    if len(c) == 4:
        # one pair
        m,x,y,z=c.most_common()
        s = sorted([x[0],y[0],z[0]], reverse=True)
        return 'one pair'
    # high card
    e = list(c.elements())
    return 'high card'

def get_type2(cards: str):
    c = Counter(cards)
    j_count = c['J']
    if len(c) == 1:
        return 'five'
    elif (len(c)) == 2:
        a,b=c.most_common()
        if j_count > 0:
            return 'five'
        if a[1] == 4: # 4,1
            return 'four'
        else: # 3,2
            return 'full house'
    elif len(c) == 3:
        x,y,z,=c.most_common()
        if x[1] == 3:
            # three of a kind, 3,1,1
            if j_count > 0:
                return 'four'
            return 'three'
        else: 
            # two pair, 2,2,1
            if j_count == 2:
                return 'four'
            if j_count == 1:
                return 'full house'
            return 'two pair'
    elif len(c) == 4:
        # one pair
        if j_count != 0:
            return 'three'
        return 'one pair'
    # high card
    else:
        if j_count !=0:
            return 'one pair'
        return 'high card'



q1()