# 7576 - 토마토
# 1. 문제 이해 :
# 익은 토마토에 인접(왼오 위아래)한 토마토들만 익음
# 1은 익은 토마토, 0은 익지않은 토마토, -1은 토마토가 들어있지 않은 칸
# 입력 : M x N (M이 가로)
# 토마토들이 며칠이 지나면 다 익게되는지 최소 일수 출력
# 토마토가 모두 익지 못하는 상황 : -1출력
# 이미 모든 토마토가 익어있는 상태이면 0 출력

# 2. 풀이 계획 및 검증: BFS -> O(MxN) -> 백만

# 3. 구현 :
# from _collections import deque
#
# def bfs() :
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]
#     while q :
#         x, y = q.popleft()
#
#         for i in range(4) :
#             nx, ny = x + dx[i], y + dy[i]
#
#             if 0 <= nx < n and 0 <= ny < m :
#                 if not(check[nx][ny]) and box[nx][ny] == 0 :
#                     q.append((nx, ny))
#                     check[nx][ny] = True
#                     box[nx][ny] = 1
#                     storage[nx][ny] = storage[x][y] + 1
#
#
# m, n = map(int, input().split()) # 가로 세로
# box = [list(map(int, list(input().split()))) for _ in range(n)] # 공백 제거해줘야함
# check = [[False] * m for _ in range(n)]
# q = deque()
# storage = [[0] * m for _ in range(n)] # 최소 횟수 저장소
# result = 0 #
#
# for i in range(n) :
#     for j in range(m) :
#         if not(check[i][j]) and box[i][j] == 1 :
#             q.append((i, j))
#             check[i][j] = True
#             storage[i][j] = 0
#             bfs()
#
# for i in range(n) :
#     for j in range(m) :
#         if box[i][j] == 0 : # 토마토가 다 익지않았으면 -1 출력
#             result = -1
#             break
#
# if result == -1 :
#     print(-1)
# else :
#     max_value = 0 # 토마토가 다 익은 경우 storage 에서 최대값을 찾음
#     # 0이 없는 경우 storage 값이 증가하지 않으므로 0을 출력
#     for i in range(n) :
#         for j in range(m) :
#             if max_value < storage[i][j] :
#                 max_value = storage[i][j]
#
#     print(max_value)

# 4. 검토 및 개선 :
# 예제 3번을 통과하지 못함
# 6 4
# 1 -1 0 0 0 0
# 0 -1 0 0 0 0
# 0 0 0 0 -1 0
# 0 0 0 0 -1 1
# 다음 입력값을 넣었을 때 6이 나와야하는데 9가 나옴
# 왜 6이 나오는지도 이해하지 못함

# 정답 코드
# 키포인트는 처음에 익은 토마토가 한군데만이 아니라 다른데도 있을 시에
# 동시에 큐에 넣어줌으로써 동시에 서로 다른 토마토가 다른 위치에서 각자
# 인접한 토마토를 익히도록하여 answer 라는 일수를 계산한다.

from collections import deque

def bfs() :
    while q :
        x, y, count = q.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m :
                if tomato[nx][ny] == 0 :
                    tomato[nx][ny] = 1
                    q.append((nx, ny, count + 1))
    return count # 갈 수 있는 모든 칸을 방문하고 그때의 count 값을 반환 = 최소 일 수


def check(answer, tomato) :
    for i in range(len(tomato)) :
        for j in range(len(tomato[i])) :
            if tomato[i][j] == 0 : # 0이 남아있으면 -1 출력
                return -1
    return answer


m, n = map(int, input().split()) # 가로m 세로n
tomato = [list(map(int, list(input().split()))) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()

for i in range(n) :
    for j in range(m) :
        if tomato[i][j] == 1 :
            q.append((i, j, 0))
            # 익은 토마토만 q에 넣어줌
            # 동시에 진행하기위해 count 값 까지 넣어줘야함
            # count 값이 같으면 동시에 진행한다는 뜻임

answer = bfs()

print(check(answer, tomato))

# 기록 :
# 0인 토마토를 방문하면 1로 변하므로 check 배열을 만들 필요 없음
# 동시에 실행되는 경우를 생각해야함

# 다시 풀어보기 :
from _collections import deque


def bfs() :
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q :
        x, y, cnt = q.popleft()

        for i in range(4) :
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < n and 0 <= ny < m :
                if tomato[nx][ny] == 0 :
                    q.append((nx, ny, cnt + 1))
                    tomato[nx][ny] = 1
    return cnt # while문 끝나고 cnt 리턴해줘야함 !


m, n = map(int, input().split())
tomato = [list(map(int, list(input().split()))) for _ in range(n)]
q = deque()

for i in range(n) :
    for j in range(m) :
        if tomato[i][j] == 1 :
            q.append((i, j, 0))

c = bfs()

result = 0
for i in range(n) :
    for j in range(m) :
        if tomato[i][j] == 0 :
            result = -1
            break

if result == -1 :
    print(-1)
else :
    print(c)
