# 10026 - 적록색약
# 1. 문제 이해 :
# N x N 그리드 칸
# R 빨, G초, B파
# 같은 색이 상하좌우로 인접해있는 경우 같은 구역
# 적록색약은 빨간색과 초록색을 구별 하지 못함
# 입력 : 1 <= N <= 100
# 출력 : 적록색약이 아닌 사람이 본 구역의 개수 적록색약 구역의 개수

# 2. 풀이 계획 및 검증 :
# dfs -> O(V + E) = O(10000 + 40000)

# 3. 구현
# import sys
# sys.setrecursionlimit(100000)
#
# n = int(input())
# arr = [list(input().strip()) for _ in range(n)]
# visited = [[False] * n for _ in range(n)]
#
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
#
# def dfs (x, y, value) :
#     for i in range(4) :
#         nx, ny = x + dx[i], y + dy[i]
#
#         if 0 <= nx < n and 0 <= ny < n :
#             if not(visited[nx][ny]) and arr[nx][ny] == value:
#                 visited[nx][ny] = True
#                 dfs(nx, ny, value)
#
#
# def dfs2 (x, y, value) :
#     for i in range(4) :
#         nx, ny = x + dx[i], y + dy[i]
#
#         if value == 'B':
#             if 0 <= nx < n and 0 <= ny < n :
#                 if not(visited[nx][ny]) and arr[nx][ny] == value:
#                     visited[nx][ny] = True
#                     dfs(nx, ny, value)
#         else:
#             if 0 <= nx < n and 0 <= ny < n:
#                 if not(visited[nx][ny]) :
#                     if arr[nx][ny] == 'R' or arr[nx][ny] == 'G':
#                         visited[nx][ny] = True
#                         dfs2(nx, ny, arr[nx][ny])
#
#
# # 적록색약 아님
# cnt = 0
# for i in range(n) :
#     for j in range(n) :
#         if not(visited[i][j]) :
#             visited[i][j] = True
#             dfs(i, j, arr[i][j])
#             cnt += 1
# print(cnt, end=' ')
#
# visited = [[False] * n for _ in range(n)]
# cnt = 0
# for i in range(n) :
#     for j in range(n) :
#         if not(visited[i][j]) :
#             visited[i][j] = True
#             dfs2(i, j, arr[i][j])
#             cnt += 1
# print(cnt)

# 개선 및 검토 :
# BFS를 기본인 상태에서 한 번,
# G를 R로 바꾼 상태에서 한 번 실행시켜주면 된다.
# DFS와 BFS는 재귀로도 풀 수 있지만, 재귀를 사용하면
# 스택 오버플로우로 인해 런타임 에러가 발생할 가능성이 크다.
# 재귀로 풀 수 있는 모든 코드는 반복문을 사용해서도 해결할 수 있다.
from _collections import deque

n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
q = deque()

dx = [1, -1, 0, 0]
dy= [0, 0, 1, -1]

def bfs() :
    while q :
        x, y = q.popleft()

        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n :
                if not(visited[nx][ny]) and arr[nx][ny] == arr[x][y] :
                    visited[nx][ny] = True
                    q.append((nx, ny))


cnt1 = 0
for i in range(n) :
    for j in range(n) :
        if not(visited[i][j]) :
            visited[i][j] = True
            q.append((i, j))
            bfs()
            cnt1 += 1

for i in range(n) :
    for j in range(n) :
        if arr[i][j] == 'G' :
            arr[i][j] = 'R'

cnt2 = 0
visited = [[False] * n for _ in range(n)]
for i in range(n) :
    for j in range(n) :
        if not(visited[i][j]) :
            visited[i][j] = True
            q.append((i, j))
            bfs()
            cnt2 += 1

print(cnt1, cnt2)