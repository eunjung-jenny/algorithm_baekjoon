C, R = map(int, input().split())
K = int(input())
board = [[0]*C for _ in range(R)]

# 아래, 오른, 위, 왼
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

guest = 1
r = 0
c = 0
board[r][c] = guest

if K > C * R:
    K = 0

if K != 0:
    while guest != K:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            while 0 <= nr < R and 0 <= nc < C and board[nr][nc] == 0:
                guest += 1
                board[nr][nc] = guest
                r = nr
                c = nc
                nr += dr[i]
                nc += dc[i]
                if guest == K:
                    break
            if guest == K:
                break

    print(c+1, r+1)

else:
    print(K)

#     board[r][c] = guest
#     guest += 1
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         while 0 <= nr < R and 0 <= nc < C and board[nr][nc] == 0:
#             r = nr
#             c = nc
#             board[r][c] = guest
#             if guest == K:
                
#             guest += 1
#             nr = r + dr[i]
#             nc = c + dc[i]
            
#         break

# print(c+1, r+1)


# C, R = map(int, input().split())
# K = int(input())
# board = [[0] * C for _ in range(R)]

# # 아래, 오른, 위, 왼
# dr = [1, 0, -1, 0]
# dc = [0, 1, 0, -1]

# r = 0
# c = 0
# if K > C * R:
#     print('0')
# elif K == 1:
#     print('1 1')
# else:
#     board[0][0] = 1
#     for k in range(2, K+1):
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == 0:
#                 board[nr][nc] = k
#                 r = nr
#                 c = nc
#                 break
#     print(c+1, r+1)


# if K > C * R:
#     K = 0

# if K != 0:

#     cnt = 1
#     tot = 0
#     temp = 0
#     while True:
#         temp = 2 * ((C-1) + (R-1))
#         if K < tot + temp:
#             break
#         tot += temp   
#         cnt += 1
#         C -= 2
#         R -= 2

#     # tot : 전 사각형까지 앉은 사람 수
#     # 바깥에서부터 cnt번째 사각형에 위치
#     x = cnt # 해당 사각형의 시작점의 x
#     y = cnt # 해당 사각형의 시작점의 y

#     cnt = 0
#     tot += 1
#     while tot != K:
#         if cnt < R-1:
#             y += 1
#         elif cnt < R-1 + C-1:
#             x += 1
#         elif cnt < R-1 + C-1 + R-1:
#             y -= 1
#         else:
#             x -= 1
#         cnt += 1
#         tot += 1

#     print(x, y)

# else:
#     print('0')