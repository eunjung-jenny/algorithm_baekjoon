N = int(input())

pillars = []
for _ in range(N):
    L, H = map(int, input().split())
    pillars.append((L, H))

pillars = sorted(pillars, key = lambda x: x[0])

corners = [pillars[0]]

for i in range(1, len(pillars)):
    if corners[-1][1] <= pillars[i][1]:
        corners.append(pillars[i])

pillars_r = list(reversed(pillars[len(corners):]))

corners_r = [pillars_r[0]]

for i in range(1, len(pillars_r)):
    if corners_r[-1][1] <= pillars_r[i][1]:
        corners_r.append(pillars_r[i])


tot = corners[-1][1]
for i in range(len(corners)-1):
    h = corners[i][1]
    
    w = corners[i+1][0] - corners[i][0]
    tot += h * w

for i in range(len(corners_r)-1):
    h = corners_r[i][1]
    w = (corners_r[i][0]+1) - (corners_r[i+1][0]+1)
    tot += h * w

print(tot)
