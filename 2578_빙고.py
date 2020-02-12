board = [list(map(int, input().split())) for _ in range(5)]
calls = []
# calls = [11, 12, 2, 24, 10, 25, 17, 9, 18, 13, 5, 19, 4, 14, 7, 8, 16, 1, 3, 6, 20, 21, 22, 15, 23]
# calls = [11, 1, 14, 18, 10, 3, 4, 22, 2, 13, 8, 7, 5, 12, 24, 16, 25, 6, 20, 21, 17, 19, 9, 15, 23]

for _ in range(5):
    calls += list(map(int, input().split()))

dr = []
dc = []
# bingo_line_hor = []
# bingo_line_ver = []
# bingo_line_dia = [] # 1: 우하향, 2: 우상향

cnt = 0
bingo_line = 0
for call in calls:
    if bingo_line >= 3:
        break
    else:
        cnt += 1
    for i in range(25):
        r, c = divmod(i, 5)
        if board[r][c] == call:
            board[r][c] = 0
            break
    
    for i in range(5):
        # if r in bingo_line_hor:
        #     break
        if board[r][i] != 0:
            break
    else:
        bingo_line += 1
        # bingo_line_hor.append(r)

    for i in range(5):
        # if c in bingo_line_hor:
        #     break
        if board[i][c] != 0:
            break
    else:
        bingo_line += 1
        # bingo_line_ver.append(r)

    if r == c:
    # if r == c and 1 not in bingo_line_dia:            
        for i in range(5):
            if board[i][i] != 0:
                break
        else:
            bingo_line += 1
            # bingo_line_dia.append(1)
        
    if r == 4-c:
    # if r == 4-c and 2 not in bingo_line_dia:
        for i in range(5):
            if board[i][4-i] != 0:
                break
        else:
            bingo_line += 1
            # bingo_line_dia.append(2)

print(calls.index(call))
    