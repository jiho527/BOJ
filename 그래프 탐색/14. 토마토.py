# 7596 - 토마토
# 1. 문제 이해 :
# 3차원 배열
# 가로 M * 세로 N * 높이 H (2 <= N, N <= 100, 1 <= H <= 100)
# N개의 줄이 H번 반복 (가장 밑부터 위로가는 순서로)
# 익은 토마토의 위, 아래, 왼쪽, 오른쪽, 앞, 뒤의 토마토가 익는다
# 며칠이 지나면 다 익게 되는지 최소 일수를 구하자 <- 출력
# (모두 익어있으면 0, 모두 못 익으면 -1)
# 1 : 익은 토마토, 0 : 익지 않은 토마토, -1 : 토마토가 없음

# 2. 풀이 계획 및 검증
# 최소 일 수 -> dp
# 탐색 -> dfs
# 3차원 배열 -> (h, n, m)으로 접근

# dx = [1, -1, 0, 0, 0, 0] # 앞, 뒤
# dy = [0, 0, 1, -1, 0, 0] # 위, 아래
# dz = [0, 0, 0, 0, 1, -1] # 좌, 우
#
# def dfs(x, y, z, ans) :
#     global answer
#
#     answer = max(answer, ans)
#
#     for i in range(6) :
#         nx = x + dx[i]
#         ny = y + dy[i]
#         nz = z + dz[i]
#
#         if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m :
#             if arr[nx][ny][nz] == 0 and not(check[nx][ny][nz]) :
#                 arr[nx][ny][nz] = 1
#                 check[nx][ny][nz] = True
#                 dfs(nx, ny, nz, ans + 1)
#
#
# m, n, h = map(int, input().split())
# arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
# check = [[[False] * m for _ in range(n)] for _ in range(h)]
#
# answer = 0
# for i in range(h) :
#     for j in range(n) :
#         for k in range(m) :
#             if arr[i][j][k] == 1 and not(check[i][j][k]): # 중복될 수도 있으므로
#                 check[i][j][k] = True
#                 dfs(i, j, k, 0)
#
# result = True
# for i in range(h) :
#     for j in range(n) :
#         for k in range(m) :
#             if arr[i][j][k] == 0 :
#                 result = False
#                 break
#         if result == False:
#             break
#     if result == False:
#         break
#
# if result :
#     print(answer)
# else :
#     print(-1)

# 위 문제를 dfs로 풀었더니 틀린 것 같음
# dfs -> 동시에 일어나는 일이므로 bfs로 풀어야함

# from collections import deque
#
# dx = [1, -1, 0, 0, 0, 0] # 앞, 뒤
# dy = [0, 0, 1, -1, 0, 0] # 위, 아래
# dz = [0, 0, 0, 0, 1, -1] # 좌, 우
#
# def bfs() :
#     global answer
#
#     while q :
#         x, y, z, ans = q.popleft()
#         answer = max(answer, ans)
#
#         for i in range(6) :
#             nx = x + dx[i]
#             ny = y + dy[i]
#             nz = z + dz[i]
#
#             if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m :
#                 if arr[nx][ny][nz] == 0 and not(check[nx][ny][nz]) :
#                     arr[nx][ny][nz] = 1
#                     check[nx][ny][nz] = True
#                     q.append((nx, ny, nz, ans + 1))
#
#
# m, n, h = map(int, input().split())
# arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
# check = [[[False] * m for _ in range(n)] for _ in range(h)]
#
# q = deque()
# answer = 0
# for i in range(h) :
#     for j in range(n) :
#         for k in range(m) :
#             if arr[i][j][k] == 1 and not(check[i][j][k]): # 중복될 수도 있으므로
#                 check[i][j][k] = True
#                 q.append((i, j, k, 0))
#                 bfs()
#
# result = True
# for i in range(h) :
#     for j in range(n) :
#         for k in range(m) :
#             if arr[i][j][k] == 0 :
#                 result = False
#                 break
#         if result == False:
#             break
#     if result == False:
#         break
#
# if result :
#     print(answer)
# else :
#     print(-1)

# 예제는 맞았지만 채점결과 틀렸다.
# 반례 :
# 5 3 1
# 0 0 0 0 0
# 0 1 0 1 0
# 0 0 0 0 0
# 동시에 토마토가 익어야되는데 동시성을 생각하지 못했다.
# 이는 구슬 탈출에서도 다뤄본 개념

from collections import deque

dx = [1, -1, 0, 0, 0, 0] # 앞, 뒤
dy = [0, 0, 1, -1, 0, 0] # 위, 아래
dz = [0, 0, 0, 0, 1, -1] # 좌, 우

def bfs() :
    global answer

    while q :
        x, y, z, ans = q.popleft()
        answer = max(answer, ans)

        for i in range(6) :
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m :
                if arr[nx][ny][nz] == 0 and not(check[nx][ny][nz]) :
                    arr[nx][ny][nz] = 1
                    check[nx][ny][nz] = True
                    q.append((nx, ny, nz, ans + 1))


m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
check = [[[False] * m for _ in range(n)] for _ in range(h)]

q = deque()
answer = 0
for i in range(h) :
    for j in range(n) :
        for k in range(m) :
            if arr[i][j][k] == 1 :
                check[i][j][k] = True
                q.append((i, j, k, 0))
bfs()

result = True
for i in range(h) :
    for j in range(n) :
        for k in range(m) :
            if arr[i][j][k] == 0 :
                result = False
                break
        if result == False:
            break
    if result == False:
        break

if result :
    print(answer)
else :
    print(-1)

# 드디어 맞음
# 5. 검토 및 개선