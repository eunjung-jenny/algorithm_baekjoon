from collections import Counter
from math import ceil

N, K = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(N)]
# (s, y)
# s: 0 여자 1 남자

female = [y for s, y in students if s == 0]
male = [y for s, y in students if s == 1]

female_dict = dict(Counter(female))
male_dict = dict(Counter(male))

tot = 0
for value in female_dict.values():
    tot += ceil(value/K)

for value in male_dict.values():
    tot += ceil(value/K)

print(tot)