# 2206 - 벽 부수고 이동하기
# 1. 문제 이해 :
# N x M 맵 (세로x가로)
# 0 : 이동할 수 있는 곳, 1 : 이동할 수 없는 벽
# (1, 1)에서 (N, M)까지 최단 경로로 이동 (최단 경로는 시작과 끝 포함)
# 이동 중에 한개의 벽을 부수고 이동하는게 경로가 더 짧다면
# 한개까지 부숴도 된다. 최단 경로를 구하시오
# 입력 : 1 <= N , M <= 1000
# (1,1)과 (N,M)은 항상 0 이라고 가정
# 출력 : 최단거리 출력, 불가능할 때는 -1 출력

# 2. 풀이 계획 :
# min(벽 안부수고 bfs, 차례대로 벽 부수고 bfs)

# 3. 구현 :
# from collections import deque
#
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
#
# def bfs() :
#     while q :
#         x, y = q.popleft()
#         if x == n-1 and y == m-1 :
#             return dp[n-1][m-1]
#
#         for i in range(4) :
#             nx, ny = x + dx[i], y + dy[i]
#
#             if 0 <= nx < n and 0 <= ny < m :
#                 if arr[nx][ny] == 0 and not(dp[nx][ny]) :
#                     q.append((nx ,ny))
#                     dp[nx][ny] = dp[x][y] + 1
#
#     if x != n-1 and y != m-1 :
#         return -1
#
#
# n, m = map(int, input().split()) # n : 세로
# arr = [list(map(int, input().strip())) for _ in range(n)]
# dp = [[0] * m for _ in range(n)]
# wall = []
#
# q = deque([(0, 0)])
# dp[0][0] = 1
# cnt = bfs()
#
# result = []
# for i in range(n) :
#     for j in range(m) :
#         if arr[i][j] == 1 :
#             dp2 = [[0] * m for _ in range(n)]
#             arr[i][j] = 0
#             q = deque([(0, 0)])
#             cnt2 = bfs()
#             if cnt2 != -1 :
#                 result.append(cnt2)
#             arr[i][j] = 1
#
# if cnt == -1 and len(result) == 0 :
#     print(-1)
# elif cnt > 0 and len(result) == 0 :
#     print(cnt)
# elif cnt == -1 and len(result) :
#     print(min(result))
# elif cnt > 0 and len(result) :
#     print(min(cnt, min(result)))

# 시간 초과 ㅠㅠ
# 4. 검토 및 개선 :
# 벽을 하나씩 부수고 매 경우마다 bfs를 수행하면 시간초과가 뜬다.

# 출처 : https://www.acmicpc.net/board/view/27386
# -가중치가 없는 최단 경로는 무조건 BFS
# DFS는 특정 칸에 처음 도달했을 때까지의 경로의 길이가 다른 경로를 통해
# 도달한 길이보다 짧다는 보장이 없기때문이다.
# -모든 칸을 전부 0으로 하나씩 바꾸고 BFS를 돌리면 통과하지 못함
# 벽이 최대 O(NM)개 있는 맵에서 벽을 하나 부술때마다 O(NM)개의 칸을
# 탐색해야하므로 O((NM)^2) = 1조
# - 칸마다 방문 체크 하나씩만 하는 방법으로는 통과할 수 없다.
# 그 지점까지 최단으로 갔다고 해서 그 이후의 여정도 최적으로 만들 수 있는것은
# 아니기 때문이다.
# 따라서 현재상태(여기까지 오면서 벽을 부순 적이 있는가) 자체를
# 큐에 넣어서 문제를 풀어야한다.
# visited[x][y][벽을 부순적이 있는가?)가 되어야한다.

# from _collections import deque
# dr = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#
#
# def bfs(y, x, k) :
#     global n, m
#     queue = deque()
#     queue.append((y, x, k))
#     dist[y][x][k] = 1
#
#     while queue :
#         curr_y, curr_x, status = queue.popleft()
#         for d in dr :
#             next_y, next_x = curr_y + d[0], curr_x + d[1]
#             if 0 <= next_y < n and 0 <= next_x < m :
#                 # 방문할 수 있고, 방문 안한 경우
#                 if map[next_y][next_x] == 0 and dist[next_y][next_x][status] == 0 :
#                     dist[next_y][next_x][status] = dist[curr_y][curr_x][status] + 1
#                     queue.append((next_y, next_x, status))
#
#                 if status == 0 : # 벽이 안부숴진 경우
#                     # 벽 부숴버리기
#                     if map[next_y][next_x] == 1 and dist[next_y][next_x][status + 1] == 0 :
#                         dist[next_y][next_x][status+1] = dist[curr_y][curr_x][status] + 1
#                         queue.append((next_y, next_x, status+1))
#
# n, m = map(int, input().split())
# map = [list(map(int, input().strip())) for _ in range(n)]
# dist = [[[0] * 2 for _ in range(m)] for _ in range(n)]
# # dist[i][i][0] : 벽이 부숴진 것 없이 (i, i)에 도달하는 최단경로
# # dist[i][i][1] : 벽이 부숴진 후 자기 (i, i)에 도달하는 최단경로
#
# bfs(0,0,0)
#
# # 부숴지지 않아도 도달할 수 있고, 부숴져도 도달하는 경우 -> 작은 것을 출력
# if dist[n-1][m-1][0] != 0 and dist[n-1][m-1][1] != 0 :
#     print(min(dist[n-1][m-1]))
# elif dist[n-1][m-1][0] != 0 : # 부숴지기 전 값만 있다면
#     print(dist[n-1][m-1][0])
# elif dist[n-1][m-1][1] != 0 : # 부숴진 후 값만 있다면
#     print(dist[n-1][m-1][1])
# else : # 둘다 값이 없다면
#     print(-1)


# 다시 풀기
from _collections import deque

dr = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(y, x, z) :
    global n, m
    q = deque([(y, x, z)])
    dist[y][x][z] = 1 # 빼먹음 (시작 포함해줘야함)

    while q :
        curr_y, curr_x, status = q.popleft()

        for d in dr :
            next_y, next_x = curr_y + d[0], curr_x + d[1]
            if 0 <= next_y < n and 0 <= next_x < m :
                if arr[next_y][next_x] == 0 and dist[next_y][next_x][status] == 0 :
                    dist[next_y][next_x][status] = dist[curr_y][curr_x][status] + 1
                    q.append((next_y, next_x, status))

                if status == 0 :
                    # 벽이 있는 경우 주의 !
                    if arr[next_y][next_x] == 1 and dist[next_y][next_x][status+1] == 0 :
                        dist[next_y][next_x][status+1] = dist[curr_y][curr_x][status] + 1
                        q.append((next_y, next_x, status+1))


n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
dist = [[[0] * 2 for _ in range(m)] for _ in range(n)]

bfs(0, 0, 0)

if dist[n-1][m-1][0] != 0 and dist[n-1][m-1][1] != 0 :
    print(min(dist[n-1][m-1]))
elif dist[n-1][m-1][0] != 0 :
    print(dist[n-1][m-1][0])
elif dist[n-1][m-1][1] != 0 :
    print(dist[n-1][m-1][1])
else :
    print(-1)

# 5. 기록
# bfs로 완탐하면 시간이 너무 오래걸림
# 큐에서 뺄 때 한번에 벽 부쉈을때와 안부쉈을때의 최단경로를 dp로 저장하여
# 시간을 줄인다.
# 오타 하나때문에 몇십분을 잡아먹었다. 오타 주의하자.
