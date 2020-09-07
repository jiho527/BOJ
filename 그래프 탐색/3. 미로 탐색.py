# 2178 - 미로 탐색
# 1. 문제 이해:
# 1은 이동 가능, 0은 이동 x
# (1,1)에서 (N,M)의 위치로 이동할 때 지나야하는 최소의 칸 수 구하기
# 다른칸으로 이동시, 서로 인접한 칸으로만 이동 가능
# 칸 수에 시작과 도착 위치도 포함
# N, M  -> NxM 크기의 배열
# N개 줄 만큼 M개의 정수로 미로 주어짐 (도착위치로 이동할 수 있는 경우만)

# 2. 풀이 계획 (자료구조, 알고리즘) : matrix 배열, visited 배열, BFS
# 3. 검증 : O(NM)

# 4. 구현
# from _collections import deque
#
# def bfs() :
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, 1, -1]
#     cnt = 0
#
#     while q :
#         x, y = q.popleft()
#         if not(check[x][y]) and matrix[x][y] == '1':
#             check[x][y] = True
#             cnt += 1
#
#             for i in range(4) :
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#
#                 if 0 <= nx <= 3 and 0 <= ny <= 5 :
#                     if not(check[nx][ny]) and matrix[nx][ny] == '1':
#                         q.append((nx,ny))
#
#     return cnt
#
#
# n, m = map(int, input().strip().split())
# matrix = [[] * m for _ in range(n)]
# check = [[False] * m for _ in range(n)]
#
# for _ in range(n) :
#     matrix[_].extend(list(input()))
#
# q = deque()
# q.append((0,0))
# c = bfs()
#
# print(c)
# 틀림
# 1이면 다 방문함 -> 15 나와야하는데 17나옴

# 하지만 최소값을 구해야함
# 어떻게 1만 방문하면서 최소 칸 수를 구할 수 있을까

# 4. 검토 및 개선
# from collections import deque
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
#
# n, m = map(int, input().split())
# a = [list(map(int, list(input()))) for _ in range(n)]
# # map함수는 Iterator를 반환하므로 list로 변환해줘야함
# q = deque()
# check = [[False]*m for _ in range(n)]
# dist = [[0]*m for _ in range(n)]
#
# q.append((0, 0))
# check[0][0] = True
# dist[0][0] = 1 # 최소 칸 수 찾기 위한 이차원 배열
#
# while q :
#     x, y = q.popleft()
#     for k in range(4) :
#         nx, ny = x + dx[k], y + dy[k]
#         if 0 <= nx < n and 0 <= ny < m :
#             if check[nx][ny] == False and a[nx][ny] == 1 :
#                 q.append((nx, ny))
#                 dist[nx][ny] = dist[x][y] + 1
#                 check[nx][ny] = True
#
# print(dist[n-1][m-1])

# 경험 및 기록 :
# BFS다 방식을 사용하여 최단 경로를 탐색한다.
# 값이 1이고 방문하지 않은 정점을 다 방문 하되,
# 인접한 정점을 방문할 때마다 횟수를 증가시키는게 아니라
# 해당 칸까지의 최단 거리를 저장하는 배열을 따로 만들어서
# 조건이 맞으면 (방문x, 1) 인접한 다음 칸에 1 증가한 수를 저장

# 다시 풀기:
from collections import deque

n, m = map(int, input().split())
arr = []
check = [[False] * m for _ in range(n)]
cnt = [[0] * m for _ in range(n)] # 칸까지의 최단거리
cnt[0][0] = 1
q = deque()

for _ in range(n) :
    arr.append(list(map(int, list(input()))))

q.append((0,0))
check[0][0] = True

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q :
    x, y = q.popleft()
    for i in range(4) :
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m :
            if check[nx][ny] == False and arr[nx][ny] == 1 :
                q.append((nx, ny))
                check[nx][ny] = True
                cnt[nx][ny] = cnt[x][y] + 1

print(cnt[n-1][m-1])