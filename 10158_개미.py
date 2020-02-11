W, H = map(int, input().split())
c, r = map(int, input().split())
t = int(input())

nc = c+t
nr = r+t
c_q, c_r = divmod(nc, W)
if c_q % 2:
    c_final = W - nc % W
else:
    c_final = nc % W

r_q, r_r = divmod(nr, H)
if r_q % 2:
    r_final = H - nr % H
else:
    r_final = nr % H

print(c_final, r_final)

'''
r_dir = 0
c_dir = 0

for _ in range(t):
    nr = r + 1 + 2 * (-1 * (r_dir%2))
    nc = c + 1 + 2 * (-1 * (c_dir%2))
    if (0 <= nr <= H) and (0 <= nc <= W) :
        r = nr
        c = nc
    else:
        if not (0 <= nr <= H) and not (0 <= nc <= W):
            r_dir += 1
            c_dir += 1
            r = r + 1 + 2 * (-1 ** (r_dir%2))
            c = c + 1 + 2 * (-1 ** (c_dir%2))
        elif not (0 <= nr <= H):
            r_dir += 1
            r = r + 1 * (-1 * r_dir%2)
            c = nc
        elif not (0 <= nc <= W):
            c_dir += 1
            r = nr
            c = c + 1 + 2 * (-1 ** (c_dir%2))

print(c, r)
'''