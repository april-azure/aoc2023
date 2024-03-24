def q1() -> None: 
    lines = []
    with open('input.txt') as file:
        lines = file.readlines()

    MAX = {
        'red' : 12,
        'green': 13,
        'blue': 14,
    }
    sum = 0
    for line in lines:
        line = line.strip()
        game_id = int(line.split(': ')[0].split(' ')[1])
        
        l = line.split(': ')[1]
        parts = l.split('; ')
        possible = True
        for part in parts:
            for c in part.split(', '):
                cnt, color = c.split(' ')
                if int(cnt) > MAX[color]:
                    possible = False
                    break
        if possible:
            print(game_id)
            sum += game_id
    
    print(sum)

# q1()

def q2() -> None:

    lines = []
    with open('input.txt') as file:
        lines = file.readlines()

    sum = 0
    
    for line in lines:
        mins = {
            'green': 0,
            'red': 0,
            'blue': 0,
        }
        line = line.strip()
        
        l = line.split(': ')[1]
        parts = l.split('; ')

        for part in parts:
            for c in part.split(', '):
                cnt, color = c.split(' ')
                mins[color] = max(mins[color], int(cnt))
                
        power = mins['blue'] * mins['green'] * mins['red']
        # print(mins['blue'], mins['green'], mins['red'])
        sum += power
    print(sum)
    
q2()