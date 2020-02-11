heights = [int(input()) for _ in range(9)]

tot = sum(heights)

for i in range(1, 9):
    if len(heights) == 7:
        break
    for j in range(i+1, 10):
        if tot - heights[i-1] - heights[j-1] == 100:
            heights.pop(j-1)
            heights.pop(i-1)
            break
    
heights = sorted(heights)

for height in heights:
    print(height, end=' ')