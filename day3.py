def is_valid_at(lines, r, c, i, j) -> bool:
    if i < 0 or i >= r or j < 0 or j >= c:
        return False
    if lines[i][j].isdigit() or lines[i][j] == '.':
        return False
    return True

def is_valid(lines, r, c, row, i, j) -> bool:
    if is_valid_at(lines,r,c,row,i-1):
        return True
    if is_valid_at(lines,r,c,row,j+1):
        return True
    for x in range(i-1, j+2):
        if is_valid_at(lines,r,c,row-1,x):
            return True
        if is_valid_at(lines,r,c,row+1,x):
            return True
    return False

def q1() -> None:
    lines = []
    with open('input.txt') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    
    rows = len(lines)
    cols = len(lines[0])
    
    sum = 0
    for r in range(rows):
        i = 0
        while i < cols:
            if not lines[r][i].isdigit(): 
                i += 1
                continue
        
            j = i
            while j < cols and lines[r][j].isdigit():
                j += 1

            if is_valid(lines, rows, cols, r, i, j-1):
                print(lines[r][i:j])
                sum  += int(lines[r][i:j])

            i = j+1
    print(sum)


# i, j inclusive
def mark_sym(syms, lines, i, j, val):
    rows = len(lines)
    cols = len(lines[0])
    if i < 0 or j < 0 or i >= rows or j >= cols:
        return 
    if lines[i][j] == '*':
        syms[i][j].append(val)

def mark_syms(syms, lines, r, i, j):
    val = int(''.join(lines[r][i:j+1]))
    for c in range(i-1,j+2):
        mark_sym(syms, lines, r-1,c,val)
        mark_sym(syms, lines, r+1,c,val)
    mark_sym(syms,lines,r,i-1,val)
    mark_sym(syms,lines,r,j+1,val)

def q2() -> None:
    lines = []
    with open('input.txt') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    
    rows = len(lines)
    cols = len(lines[0])
    
    sum = 0
    syms = [[[] for c in range(cols)] for r in range(rows)]
    
    for r in range(rows):
        i = 0
        while i < cols:
            if not lines[r][i].isdigit(): 
                i += 1
                continue
        
            j = i
            while j < cols and lines[r][j].isdigit():
                j += 1

            # count the syms around lines[r][i:j]
            mark_syms(syms, lines,r,i,j-1)
            
            i = j+1
    
    for i in range(rows):
        for j in range(cols):
            if len(syms[i][j]) == 2:
                sum += (syms[i][j][0] * syms[i][j][1])
    print(sum)

q2()