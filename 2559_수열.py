N, K = map(int, input().split())
temps = list(map(int, input().split()))

max_sum = None

for i in range(len(temps)-K+1):
    sum_temp = sum(temps[i:i+K])
    if max_sum:
        if sum_temp > max_sum:
            max_sum = sum_temp    
    else:
        max_sum = sum_temp

print(max_sum)