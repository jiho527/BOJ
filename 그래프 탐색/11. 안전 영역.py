# 2468 - 안전영역
# 1. 문제 이해 :
# N * N
# 지역에 비가 많이 내렸을 때 물에 잠기지 않는 안전영역 최대 개수 조사
# 비의 양에따라 일정한 높이 이하의 모든 지점은 물에 잠긴다.
# 주의*  비의 양에따라 안전한 영역의 개수는 다르므로 모두 비교해줘야함 !!
# 안전 영역은 물에 잠기지 않는 지점들이 위, 아래, 오른쪽, 왼쪽에 인접하며
# 그 크기가 최대인 영역을 뜻한다.
# 입력 : 2 <= N <= 100
# N개의 행 높이 정보 입력 / 1 <= 높이 <= 100
# 출력 : 장마철에 물에 잠기지않는 안전한 영역의 최대 개수

# 2. 풀이 계획 및 검증 :
# 예제 입력 1에서 2이하, 3이하, ..., 9이하 까지
# 배열내의 가장 작은 수부터 가장 큰수까지 비교했을 때
# 안전영역의 개수가 최대일때의 개수를 출력해야한다.
# 따라서 배열내에서 최소값, 최대값을 찾고,
# 최소값부터 최대값까지 bfs로 안전영역 개수를 조사한 다음, (visited 업데이트)
# 매번 최대 안전영역 개수와 비교하여 안전영역 개수를 업데이트 시켜야한다.

# 3. 구현
from collections import deque

def bfs() :
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    while q :
        x, y = q.popleft()

        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n :
                if arr[nx][ny] >= rain and not(visited[nx][ny]) :
                    visited[nx][ny] = True
                    q.append((nx, ny))


n = int(input())
arr = []
for _ in range(n) :
    arr.append(list(map(int, input().split())))

max_val = 1
min_val = 100
for i in range(n) :
    for j in range(n) :
        max_val = max(max_val, arr[i][j])
        min_val = min(min_val, arr[i][j])

q = deque()
safe_area = 0
for rain in range(min_val, max_val + 1) :
    cnt = 0 # cnt 초기화 시켜줘야함
    visited = [[False] * n for _ in range(n)]

    for i in range(n) :
        for j in range(n) :
            if arr[i][j] >= rain and not(visited[i][j]) : # 물에 안잠김
                visited[i][j] = True
                q.append((i, j))
                bfs()
                cnt += 1

    safe_area = max(safe_area, cnt)

print(safe_area)

# 4. 검토 및 개선
# max(arr)는 이차원배열 arr중 가장 큰 수를 가진 배열을 반환한다.
# 따라서 이차원배열 arr에서 최대값은 max(max(arr))로 표현할 수 있다.

# 5. 기록 :
# 예제 입력에서는 맞았는데 틀렸다고 떠서 원인을 찾아봤는데
# rain의 최소값을 2, 최대값이 9라고 할 때
# 2보다 높이가 작은 것이 침수될때와, 9보다 높이가 작은 것이 침수될 때도
# 구해야했는데 부등호를 빼먹었다.
# 이것을 '아무 지역도 물에 잠기지 않을 수도 있다.'라는 노트를 보고
# 힌트를 얻게되었다.
# 어차피 9 이하가 침수되면 안전영역은 0개이므로 계산할 필요가 없으므로
# rain이 1이하부터 8이하까지만 계산하면 된다.

# dfs로 풀었더니 컴파일 에러뜸
# 틀렸지만 참고로 올린다.
# import sys
# sys.setrecursionlimit(100000)
#
# def dfs(x, y, z) :
#     check[x][y] = True
#     for dx, dy in (-1, 0) (1, 0), (0, -1), (0, 1) :
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < n and 0 <= ny < n :
#             if not(check[nx][ny]) and arr[nx][ny] > z :
#                 dfs(nx, ny, z)
#
#
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# safe = 0
# for k in range(max(max(arr))) :
#     check = [[False] * n for _ in range(n)]
#     cnt = 0
#
#     for i in range(n) :
#         for j in range(n) :
#             if not(check[i][j]) and arr[i][j] > k : # 높이는 1부터이므로
#                 dfs(i, j, k)
#                 cnt += 1
#     safe = max(safe, cnt)
# print(safe)