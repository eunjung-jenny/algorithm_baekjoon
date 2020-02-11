C, R = map(int, input().split())
K = int(input())



cnt = 1
tot = 0
temp = 0
while True:
    temp = 2 * ((C-1) + (R-1))
    if K < tot + temp:
        break
    tot += temp   
    cnt += 1
    C -= 2
    R -= 2
    

# tot : 전 사각형까지 앉은 사람 수
# 바깥에서부터 cnt번째 사각형에 위치
x = cnt # 해당 사각형의 시작점의 x
y = cnt # 해당 사각형의 시작점의 y

cnt = 0
tot += 1
while tot != K:
    if cnt < R-1:
        y += 1
    elif cnt < R-1 + C-1:
        x += 1
    elif cnt < R-1 + C-1 + R-1:
        y -= 1
    else:
        x -= 1
    cnt += 1
    tot += 1

print(x, y)