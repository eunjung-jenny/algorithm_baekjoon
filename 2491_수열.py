# 0에서부터 9까지의 숫자로 이루어진 N개의 숫자가 나열된 수열이 있다. 그 수열 안에서 연속해서 커지거나(같은 것 포함), 혹은 연속해서 작아지는(같은 것 포함) 수열 중 가장 길이가 긴 것을 찾아내어 그 길이를 출력하는 프로그램을 작성하라. 
# 예를 들어 수열 1 2 2 4 4 5 7 7 2 의 경우에는  1≤2≤2≤4≤4≤5≤7≤7 이 가장 긴 구간이 되므로 그 길이 8을 출력한다. 수열 4 1 3 3 2 2 9 2 3 의 경우에는 3≥3≥2≥2 가 가장 긴 구간이 되므로 그 길이 4를 출력한다. 또 1 5 3 6 4 7 1 3 2 9 5 의 경우에는 연속해서 커지거나 작아지는 수열의 길이가 3 이상인 경우가 없으므로 2를 출력하여야 한다.

# 입력
# 첫째 줄에는 수열의 길이 N이 주어지고, 둘째 줄에는 N개의 숫자가 빈칸을 사이에 두고 주어진다. N은 1 이상 100,000 이하의 정수이다.

# 출력
# 첫째 줄에 가장 긴 길이를 출력한다.

N = int(input())
nums = list(map(int, input().split()))

previous_n = nums[0]
# increasing = False
# decreasing = False
len_inc = 1
len_dec = 1

max_len = 1
for num in nums[1:]:
    if num == previous_n:
        # increasing = True
        # decreasing = True
        len_inc += 1
        len_dec += 1
    elif num > previous_n:
        # increasing = True
        # decreasing = False
        len_inc += 1
        len_dec = 1
    elif num < previous_n:
        # increasing = False
        # decreasing = True
        len_inc = 1
        len_dec += 1
    previous_n = num
    longer = max(len_inc, len_dec)
    if longer > max_len:
        max_len = longer
    
print(max_len)

'''
# 증가 검사
max_len = 0

for i in range(N):
    temp = 1
    if i + 1 < N:
        for ii in range(i+1, N):
            if nums[ii] >= nums[ii-1]:
                temp += 1
            else:
                break
    if temp > max_len:
        max_len = temp         

# 감소 검사
for i in range(N):
    temp = 1
    if i + 1 < N:
        for ii in range(i+1, N):
            if nums[ii] <= nums[ii-1]:
                temp += 1
            else:
                break
    if temp > max_len:
        max_len = temp

print(max_len)
'''