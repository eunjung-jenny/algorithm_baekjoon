N = int(input())
pieces = [list(map(int, input().split())) for _ in range(N)]
board = [[0]*100 for _ in range(100)]

pieces_coord = []
for piece in pieces:
    r1, c1, r2, c2 = piece[1], piece[0], piece[1]+10, piece[0]+10 
    pieces_coord.append((r1, c1, r2, c2))

for r1, c1, r2, c2 in pieces_coord:
    for r in range(r1, r2):
        for c in range(c1, c2):
            board[r][c] = 1

tot = 0
for row in board:
    tot += sum(row)

print(tot)

