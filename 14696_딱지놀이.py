# 별 4
# 동그라미 3
# 네모 2
# 세모 1

# 승자 이름
# 무승부 D

from collections import Counter

N = int(input())

for _ in range(N):
    a = dict(Counter(map(int, input().split()[1:])))
    b = dict(Counter(map(int, input().split()[1:])))
    
    for i in range(4, 0, -1):
        if i not in a.keys() and i not in b.keys():
            continue
        elif i not in b.keys():
            print('A')
            break
        elif i not in a.keys():
            print('B')
            break            
        else:
            if a[i] > b[i]:
                print('A')
                break
            elif a[i] < b[i]:
                print('B')
                break
        
    else:
        print('D')

'''
    if a.count(4) > b.count(4):
        print('A')
    elif a.count(4) < b.count(4):
        print('B')
    else:
        if a.count(3) > b.count(3):
            print('A')
        elif a.count(3) < b.count(3):
            print('B')
        else:
            if a.count(2) > b.count(2):
                print('A')
            elif a.count(2) < b.count(2):
                print('B')
            else:
                if a.count(1) > b.count(1):
                    print('A')
                elif a.count(1) < b.count(1):
                    print('B')
                else:
                    print('D')
'''