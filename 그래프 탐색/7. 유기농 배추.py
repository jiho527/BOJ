# 1012 - 유기농 배추
# 1. 문제 이해 :
# 흰 지렁이는 인접한 다른 배추로 이동 가능 (좌 우 위 아래)
# 배추들이 모여있는 곳에는 배추 흰지렁이가 한 마리만 있으면 됨
# 입력 : 테스트 케이스 개수 T, M x N 가로 세로, 배추의 개수 k,배추의 위치 x,y
# 출력 : 각 테스트 케이스에 대해 필요한 최소의 배추 흰지렁이 마리 수 출력

# 2. 풀이 계획 및 검증: BFS or DFS -> O(T*M*N)

# 3. 구현
from _collections import deque

def bfs() :
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


t = int(input()) # 테스트 케이스

for _ in range(t) :
    q = deque() # 테스트 케이스마다 초기화
    c = 0  # bfs 호출한 횟수 = 배추 흰지렁이 마리 수/ 테스트 케이스마다 초기화

    m, n, k = map(int, input().split()) # 가로 세로 개수
    arr = [[0] * m for _ in range(n)] # 배추 밭
    check = [[False] * m for _ in range(n)] # 방문 확인

    for _ in range(k) : # 배추 입력
       x, y = map(int, input().split()) # 가로 세로 주의
       arr[y][x] = 1

    for i in range(n) :
        for j in range(m) :
            if arr[i][j] == 1 and not(check[i][j]) :
                q.append((i, j))
                check[i][j] = True
                bfs()
                c += 1
    print(c)

# 4. 검토 및 개선 :
# x와 y를 받을 때, 뭐가 가로고 뭐가 세로인지 알아야한다. (범위보고 구분했음)
# 테스트 케이스마다 큐와 배추 지렁이 수를 세는 c를 초기화 해줘야했다.
# dfs로도 풀 수 있어야한다.

# def dfs(i, j) : # 세로 가로
#     visited[i][j] = True
#
#     for k in range(4) :
#         nx, ny = i + dx[k], j + dy[k]
#
#         if 0 <= nx < n and 0 <= ny < m :
#             if not(visited[nx][ny]) and arr[nx][ny] == 1 :
#                 dfs(nx, ny)
#
#
# t = int(input())
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
# for _ in range(t) :
#     cnt = 0
#     m, n, k = map(int, input().split())
#     arr = [[0] * m for _ in range(n)]
#     visited = [[False] * m for _ in range(n)]
#
#     for _ in range(k) :
#         i, j = map(int, input().split()) # 가로 세로
#         arr[j][i] = 1
#
#     for i in range(n) : # 세로
#         for j in range(m) : # 가로
#             if not(visited[i][j]) and arr[i][j] == 1 :
#             # 방문한 곳을 안가기위해서 visited가 False인지 꼭 확인해야함
#                 dfs(i, j)
#                 cnt += 1
#
#     print(cnt)

# 위의 dfs로 푼 코드는 답은 나오지만 런타임 에러가 뜸
# recursion depth 문제로 추측
# 배추로 가득한 50 * 50 밭일 경우, 재귀 깊이가 2500이 될텐데,
# 파이썬은 재귀가 대충 1000을 넘어가면 런타임 에러가 남.

# import sys
# sys.setrecursionlimit(n)으로 깊이를 재설정하여
# n에 2500보다 같거나 큰 숫자를 넣으면 정답 처리가 되지만,
# 이런 한계 때문에 웬만하면 재귀를 쓰지 않는게 좋다.