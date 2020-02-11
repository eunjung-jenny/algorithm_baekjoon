C, R = map(int, input().split())
N = int(input())

hor = [0, R]
ver = [0, C]

for _ in range(N):
    direction, line = map(int, input().split())
    
    if direction == 0:
        hor.append(line)
    elif direction == 1:
        ver.append(line)

hor = sorted(hor)
ver = sorted(ver)

max_w = 0
for i in range(len(hor)-1):
    w = hor[i+1] - hor[i]
    if w > max_w:
        max_w = w

max_h = 0
for i in range(len(ver)-1):
    h = ver[i+1] - ver[i]
    if h > max_h:
        max_h = h

print(max_w * max_h)