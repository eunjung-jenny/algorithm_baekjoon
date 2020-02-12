N = int(input())

pillars = sorted([tuple(map(int, input().split())) for _ in range(N)], key = lambda x: x[0])

highest_h = 0
highest_x = -1
highest_idx = 0
for idx, (x, h) in enumerate(pillars):
    if h > highest_h:
        highest_h = h
        highest_x = x
        highest_idx = idx
        
area = highest_h

previous_highest_x = highest_x
previous_highest_h = highest_h
for i in range(highest_idx-1, -1, -1):
    current_h = pillars[i][1]
    current_x = pillars[i][0]
    for ii in range(i-1, -1, -1):
        if pillars[ii][1] > current_h:
            break
    else:
        area += current_h * (previous_highest_x - current_x)
        previous_highest_x = current_x
        previous_highest_h = current_h

previous_highest_x = highest_x
previous_highest_h = highest_h
for i in range(highest_idx+1, N):
    current_h = pillars[i][1]
    current_x = pillars[i][0]
    for ii in range(i+1, N):
        if pillars[ii][1] > current_h:
            break
    else:
        area += current_h * (current_x - previous_highest_x)
        previous_highest_x = current_x
        previous_highest_h = current_h

print(area)

# pillars = sorted(pillars, key = lambda x: x[0])

# corners = [pillars[0]]

# for i in range(1, len(pillars)):
#     if corners[-1][1] <= pillars[i][1]:
#         corners.append(pillars[i])

# pillars_r = list(reversed(pillars[len(corners):]))

# corners_r = [pillars_r[0]]

# for i in range(1, len(pillars_r)):
#     if corners_r[-1][1] <= pillars_r[i][1]:
#         corners_r.append(pillars_r[i])


# tot = corners[-1][1]
# for i in range(len(corners)-1):
#     h = corners[i][1]
    
#     w = corners[i+1][0] - corners[i][0]
#     tot += h * w

# for i in range(len(corners_r)-1):
#     h = corners_r[i][1]
#     w = (corners_r[i][0]+1) - (corners_r[i+1][0]+1)
#     tot += h * w

# print(tot)
