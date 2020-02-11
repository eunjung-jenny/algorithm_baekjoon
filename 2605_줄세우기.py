N = int(input())
nums = list(map(int, input().split()))

line = [1]

for student in range(2, N+1):
    choice = nums[student-1]
    if choice == 0:
        line.append(student)
    else:
        line.insert(-choice, student)

for student in line:
    print(student, end = ' ')
