# 4963 - 섬의 개수
# 1. 문제 이해
# 섬과 바다 지도
# 섬의 가로, 세로, 대각선까지 같은 섬
# 입력 : 지도의 너비 w, 높이 h / w,h <= 50
# h개의 줄에 지도 주어짐 땅은 1, 0은 바다
# 입력의 마지막 줄에는 0이 두개 주어짐 -> 종료
# 출력 : 각 테스트 케이스에 대해 섬의 개수를 출력

# 2. 풀이 계획 및 검증
# 테스트케이스의 개수가 주어지지 않고 마지막에 0 0 이 주어짐
# input이 0 0 일때까지 반복
# 대각선까지 같은 섬이므로
# dx = [1, -1, 0, 0, 1, 1, -1, -1]
# dy = [0, 0, 1, -1, -1, 1, -1, 1]
# dfs나 bfs로 가 호출되는 횟수로 섬의 개수를 구해서 출력 -> O(2500 * 8)
# 재귀가 많이 호출될 것 같으니까 bfs로 풀어보자 -> 이부분은 추후에 더 찾아보기*
# visited도 만들어줘야함

# 3. 구현
from collections import deque

def bfs() :
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, -1, 1, -1, 1]

    while q :
        x, y = q.popleft()

        for i in range(len(dx)) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w :
                if not(visited[nx][ny]) and arr[nx][ny] == 1 :
                    visited[nx][ny] = True
                    q.append((nx, ny))


w, h = map(int, input().split())
while w != 0 or h != 0 :
    arr = []
    visited = [[False] * w for _ in range(h)]

    for _ in range(h) :
        arr.append(list(map(int, input().split())))

    q = deque()
    cnt = 0

    for i in range(h) :
        for j in range(w) :
            if not(visited[i][j]) and arr[i][j] == 1 :
                visited[i][j] = True
                q.append((i, j))
                bfs()
                cnt += 1

    print(cnt)

    w, h = map(int, input().split())

# 4. 검토 및 개선
# dfs로 풀 경우 setrecursionlimit(10000)을 해줘야했다.

# 5. 기록
# 단지번호붙이기에 대각선만 더 고려하면 풀 수 있는 문제
# 자꾸 nx, ny 범위 설정 안해줘서 한번씩 에러난다.
# deque를 사용하는 잉는 list보다 속도가 빠르기 때문이다.
