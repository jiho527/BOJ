# 2667 - 단지번호 붙이기
# 1. 문제 이해 :
# 1은 집이 있음, 0은 없음
# 좌우 위아래로 연결된 집 -> 단지 형성 (대각선은 아님)
# N x N
# 총 단지수 출력, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력

# 2. 풀이 계획 및 검증 : BFS -> O(N^2)

# 3. 구현
from collections import deque

def bfs() :
    cnt = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y = q.popleft()
        # check[nx][ny] = 1
        # cnt += 1 # 여기서 처리하면 중복 값이 생기므로 if 절에서 처리하기

        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n :
                if check[nx][ny] == False and arr[nx][ny] == 1 :
                    q.append((nx, ny))
                    check[nx][ny] = 1
                    cnt += 1

    return cnt


n = int(input())
arr = [list(map(int, list(input()))) for _ in range(n)]
check = [[False] * n for _ in range(n)]
q = deque()
result = []
c = 0

for i in range(n) :
    for j in range(n) :
        if check[i][j] == False and arr[i][j] == 1 :
            q.append((i, j))
            check[i][j] = True
            result.append(bfs())
            c += 1

print(c)
result.sort()
for i in result:
    print(i)

# 4. 검토 및 개선
# visited 체크만 해주면서 단지 수 세기만 하면돼서
# DFS로 구현하면 속도가 더 빠르게 구현할 수 있다.
# 전역변수를 활용하여 메모리 사용도 더 줄였다.

def dfs(x, y) :
    global cnt
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    check[x][y] = True
    cnt += 1

    for i in range(4) :
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n :
            if check[nx][ny] == False and arr[nx][ny] == 1 :
                dfs(nx, ny)


n = int(input())
arr = [list(map(int, list(input()))) for _ in range(n)]
check = [[False] * n for _ in range(n)]

c = 0 # 단지 수
# cnt = 0  # 집 수
result = [] # 집 수 집합


for i in range(n) :
    for j in range(n) :
        if check[i][j] == False and arr[i][j] == 1 :
            cnt = 0
            dfs(i, j)
            result.append(cnt)
            c += 1

print(c)
result.sort()
for i in result :
    print(i)


# 5. 기록
# 결과값이 정답보다 더 크게나와서 하나씩 순서대로 따라가면서 시도해봤더니
# q에 중복된 값들이 들어갈 수 있는데 pop하고 cnt를 증가시키니까
# cnt가 중복으로 증가되었다.
# 따라서 if 절에서 통과될때 cnt를 증가시켜 해결하였다.