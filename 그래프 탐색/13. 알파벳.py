#1987 - 알파벳
# 1. 문제 이해 :
# 세로 R, 가로 C 보드
# 보드의 각 칸에 대문자 알파벳 적혀있음
# (0, 0)에 말이 있음, 말은 상하좌우로 이동 가능
# 같은 알파벳을 두번 지날 수 없음
# (0,0)에서 시작해서(포함) 최대 몇칸을 지날 수 있는지 구하기
# 입력 : R C (1 <= R, C <= 20)
# R개의 줄에 걸쳐 C개의 대문자 알파벳 주어짐
# 출력 : 말이 지날 수 있는 최대 칸 수 출력

# 2. 풀이 계획 및 검증 :
# visited에 지나온 알파벳 추가
# 다음 알파벳이 visited에 있는지 검사
# bfs/dfs로 구할 수 있음

# 3. 구현
# def dfs(x, y) :
#     global cnt
#
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]
#
#     for i in range(4) :
#         nx, ny = x + dx[i], y + dy[i]
#         if 0 <= nx < r and 0 <= ny < c :
#             if arr[nx][ny] not in visited :
#                 visited.append(arr[nx][ny])
#                 cnt += 1
#                 dfs(nx, ny)
#
#
# r, c = map(int, input().split())
# arr = []
# visited = []
# for _ in range(r) :
#     arr.append(list(input()))
#
# visited.append(arr[0][0])
# cnt = 1
# dfs(0, 0)
#
# print(cnt)

#4. 검토 및 개선 :
# 예제 하나는 맞앗지만 '틀렸습니다'
# 찾아보니 백트래킹을 사용해서 푸는 문제였다.
# BFS와 DFS는 모든 칸들을 지나가게 되는데,
# 이 문제에서 중복되는 알파벳들을 피해야하는 조건이 있으므로
# BFS나 DFS로 한칸 한칸 지나면서 조건을 만족하지않으면
# 백트래킹을 해야한다.

# 여기서 말은 인접한 네 칸 중의 '한 칸'으로 이동할 수 있으므로
# 전체를 BFS/DFS로 탐색한다고 최대 칸 수가 나오지 않는다.
# 따라서, 매번 말을 이동할 때마다, max 값을 비교해야한다.

# visited에 지나온 알파벳 추가
# 다음 알파벳이 visited에 있는지 검사
# bfs/dfs로 구할 수 있음

# import sys
#
# def dfs(x, y, cnt) :
#     global answer
#
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]
#
#     answer = max(cnt, answer)
#
#     for i in range(4) :
#         nx, ny = x + dx[i], y + dy[i]
#         if 0 <= nx < r and 0 <= ny < c :
#             if arr[nx][ny] not in visited :
#                 visited.append(arr[nx][ny])
#                 dfs(nx, ny, cnt + 1)
#                 visited.pop() # 다음 경로와 비교하려면 pop 해줘야함
#
#
# #r, c = map(int, input().split())
# r, c = map(int, sys.stdin.readline().split())
# arr = [list(sys.stdin.readline().strip()) for _ in range(r)]
# visited = []
#
# answer = 1
# visited.append(arr[0][0])
# dfs(0, 0, answer)
#
# print(answer)

# 시간 초과

# dfs로 돌 수 있는 경우의 수가 많다.
# 알파벳이 26개라서 25번 움직일 수 있고,
# 방향은 왔던 방향 빼고 3가지이므로 최대 3^26이다.
# 물론 지나온 알파벳을 갈 수 없는 조건을 걸어도 경우의 수가 많다.
# + not in 을 사용하면 배열의 원소 하나하나를 체크하는 것이므로
# 알파벳이 26가지이므로 크기가 26인 배열을 만들어서
# 방문 여부를 체크하는 것이 더 빠를 수 있다.

# 1. 알파벳 -> 배열
r, c = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]
check, ans = [False] * 26, 0

def dfs (x, y, z) :
    global ans
    ans = max(ans, z)

    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1) :
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c :
            n = ord(arr[nx][ny]) - ord('A')
            if not(check[n]) :
                check[n] = True
                dfs(nx, ny, z + 1)
                check[n] = False

check[ord(arr[0][0]) - ord('A')] = True # ord : 아스키 코드값으로 변환
dfs(0, 0, 1)
print(ans)


# 2. BFS
import sys

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y) :
    global answer
    q = set([(x, y, arr[x][y])])

    while q :
        x, y, visited = q.pop()

        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < r and 0 <= ny < c :
                if arr[nx][ny] not in visited :
                    q.add((nx, ny, visited + arr[nx][ny]))
                    answer = max(answer, len(visited) + 1) # dp 구현


r, c = map(int, input().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(r)]

answer = 1
bfs(0, 0)
print(answer)

# bfs, dfs 둘다 dp 개념 + 백트래킹 섞어서 풀어야한다.
# 재귀 dfs의 경우, 매개변수를 넘겨줌으로써 이전의 값을 전달하고,
# 경로 한번 돌 때마다 answer값을 최대값으로 초기화시키고
# 전에 방문한 흔적도 초기화시킨다.

# bfs의 경우, 경로를 하나씩 도는 것이 아니므로
# 큐에서 하나씩 뺄때마다 answer 값을 최대값으로 초기화시키고
# visited를 통해 이전의 값을 전달한다.

# 공통점은 둘다 이전의 값을 저장하고
# 이것을 전달하여 다음값을 만들고 저장 -> DP

# 다시 풀기 (dfs)
def dfs(x, y, cnt) :
    global answer

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    answer = max(answer, cnt) # 다음 값 저장

    for i in range(4) :
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c :
            n = ord(arr[nx][ny]) - ord('A')
            if not(visited[n]) :
                visited[n] = True # 까먹지마
                dfs(nx, ny, cnt + 1) # 이전 값 넘겨주기
                visited[n] = False # 이전 경로 초기화


r, c = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]
visited = [False] * 26

answer = 1
visited[ord(arr[0][0]) - ord('A')] = True
dfs(0, 0, 1)

print(answer)