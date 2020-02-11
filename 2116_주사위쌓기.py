N = int(input())

dices = [list(map(int, input().split())) for _ in range(N)]

max_tot = 0
for i in range(3):
    temp_tot = 0
    for j in range(N):
        

    if temp_tot > max_tot:
        max_tot = temp_tot