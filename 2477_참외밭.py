N = int(input())

elem = [list(map(int, input().split())) for _ in range(6)]
w = [l for d, l in elem if d == 2 or d == 1]
h = [l for d, l in elem if d == 3 or d == 4]
elem_len = [l for d, l in elem]

max_w = max(w)
max_h = max(h)
tot_area = max_w * max_h

max_w_idx = elem_len.index(max_w)
max_h_idx = elem_len.index(max_h)

cut_idx1 = max(max_w_idx, max_h_idx) + 2
cut_idx2 = max(max_w_idx, max_h_idx) + 3

if cut_idx1 >= 6:
    cut_idx1 %= 6
if cut_idx2 >= 6:
    cut_idx2 %= 6

cut_area = elem_len[cut_idx1] * elem_len[cut_idx2]

result = N * (tot_area - cut_area)
print(result)