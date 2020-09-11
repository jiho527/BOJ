# 7562 - 나이트의 이동
# 1. 문제 이해 :
# 입력 : 테스트 케이스의 개수
# 첫째줄 : 체스판의 한 변의 길이 I (4 <= I <= 300)
# 체스판의 크기 : I * I
# 둘째줄 : 나이트가 현재 있는 칸
# 셋째줄 : 나이트가 이동하려고 하는 칸 {0 ~ I-1}*{0 ~ I-1}
# 출력 : 각 테스트 케이스마다 나이트가 몇번만에 이동할 수 있는지 출력

# 2. 풀이 계획 및 검증 :
# dp + bfs

# 3. 구현
from _collections import deque

dxy_list = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]


def bfs () :
    while q :
        x, y, cnt = q.popleft()

        if x == move1 and y == move2 :
            return cnt

        for dxy in dxy_list :
            nx, ny = x + dxy[0], y + dxy[1]

            if 0 <= nx < n and 0 <= ny < n :
                if arr[nx][ny] == 0 :
                    arr[nx][ny] = cnt + 1
                    q.append((nx, ny, cnt+1))


test_case = int(input())
for _ in range(test_case) :
    n = int(input())
    i, j = map(int, input().split())
    move1, move2 = map(int, input().split())

    q = deque()
    arr = [[0] * n for _ in range(n)]
    arr[i][j] = 1
    q.append((i, j, 0))
    ans = bfs()

    print(ans)

# 4. 검토 및 개선
# arr말고 dp를 위한 배열 하나만 만들어도 풀 수 있다.
from _collections import deque

dlist = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]


def bfs (x1, y1, x2, y2) :
    q = deque()
    q.append((x1, y1))
    dp[x1][y1] = 1

    while q :
        x, y = q.popleft()

        if x == x2 and y == y2 :
            return dp[x2][y2] - 1

        for d in dlist :
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < l and 0 <= ny < l :
                if dp[nx][ny] == 0 :
                    dp[nx][ny] = dp[x][y] + 1
                    q.append((nx, ny))


test_case = int(input())
for _ in range(test_case) :
    l = int(input())
    start1, start2 = map(int, input().split())
    end1, end2 = map(int, input().split())

    dp = [[0] * l for _ in range(l)]
    print(bfs(start1, start2, end1, end2))
