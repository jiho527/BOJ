# # 내 풀이 (BFS)
# from collections import deque
#
#
# def bfs():
#     dlist = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#     cnt = 1
#
#     while q :
#         x, y = q.popleft()
#
#         for dx, dy in dlist :
#             if 0 <= x+dx < n and 0<= y+dy < n :
#                 if not(check[x+dx][y+dy]) and arr[x+dx][y+dy] == '1':
#                     q.append((x+dx, y+dy))
#                     check[x+dx][y+dy] = True
#                     cnt += 1
#
#     return cnt
#
#
# arr = []
# q = deque()
# result = []
# result_num = 0
#
# n = int(input())
# check = [[False] * n for _ in range(n)]
#
# for _ in range(n) :
#     arr.append(list(input()))
#
# for i in range(n) :
#     for j in range(n) :
#         if arr[i][j] == '1' and check[i][j] == False :
#             q.append((i, j))
#             check[i][j] = True
#             result.append(bfs())
#             result_num +=1
#         else :
#             continue
#
# print(result_num)
# result.sort()
# for i in result :
#     print(i)


# 다른 풀이 (DFS)
from sys import stdin

n = int(input())
matrix = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n) :
    input = stdin.readline().strip() # strip 해주기
    for j, num in enumerate(input) :
            matrix[i][j] = int(num)


def dfs(x, y) :
    global nums
    visited[x][y] = True
    nums += 1

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n :
            if not(visited[nx][ny]) and matrix[nx][ny] == 1 :
                dfs(nx, ny)


nums = 0 # 아파트 수
result = [] # 단지별 아파트 수
cnt = 0 # 단지 수

for i in range(n) :
    for j in range(n) :
        if not(visited[i][j]) and matrix[i][j]  == 1:
            dfs(i, j)
            cnt += 1
            result.append(nums)
            nums = 0

print(cnt)
result.sort()
for num in result :
    print(num)
