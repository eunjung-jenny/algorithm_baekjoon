N = int(input())
board = [[0]*101 for _ in range(101)]

for i in range(1, N+1):
    c1, r1, dc, dr = map(int, input().split())
    for r in range(r1, r1+dr):
        for c in range(c1, c1+dc): 
           board[r][c] = i

for i in range(1, N+1):
    cnt_i = 0
    for row in board:
        cnt_i += row.count(i)
    print(cnt_i)


            