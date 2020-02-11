def get_address(i, j):
    if i == 1:
        address = j
    elif i == 2:
        address = C+R+C-j
    elif i == 3:
        address = C+R+C+R-j
    elif i == 4:
        address = C+j
    return address


C, R = map(int, input().split())
N = int(input())

stores = [list(map(int, input().split())) for _ in range(N)]

DK_i, DK_j = list(map(int, input().split()))
DK_address = get_address(DK_i, DK_j)

address = []
for i, j in stores:
    address.append(get_address(i, j))

circumference = 2 * (R + C)

diff = []
for elem in address:
    dist = abs(DK_address - elem)
    dist_2 = circumference - dist
    shorter = min(dist, dist_2)
    diff.append(shorter)

print(sum(diff))

'''
me = list(map(int, input().split()))
circumference = (R+C)*2

dist_lst = []
for i, j in stores:
    dist = 0
    if i == me[0]:
        dist += abs(j - me[1])
    elif i - me[0] % 2:
        option1 = 
        option2 = 
                
    else: # 맞은편
        if i % 2:
            option1 = j + me[1]
            option2 = (R-j) + (R-me[1])
            dist += min(option1, option2) + R
        else:
            option1 = j + me[1]
            option2 = (C-j) + (C-me[1])
            dist += min(option1, option2) + C
'''