# 2583 - 영역 구하기
# 1. 문제 이해 :
# M세로 x N가로(M,N <= 100)에 k개의 직사각형을 그린다.
# 몇개의 분리된 영역으로 나누어지는지, 각 영역의 넓이가 얼마인지 구하기
# 입력 : M, N, K <=100
# k개의 줄만큼 직사각형의 (왼쪽아래 꼭지점 x,y/오른쪽위 꼭지점 x,y) 주어짐
# 출력 : 1. 분리되어 나누어지는 영역의 개수
# 2. 각 영역의 넓이 빈칸으로 구분해서 출력(오름차순 정렬)

# 풀이 계획 :
# 좌표를 표현하는게 관건
# 직사각형이 표현된부분을 1로, 빈칸을 0으로 구분만하면
# 영역의 개수와 넓이는 bfs로 구할 수 있다.
# 좌표 표현 방법
# arr의 세로 (x좌표) : range(m-ry, m-ly)
# arr의 가로 (y좌표) : range(lx, rx)

# 3. 구현
from collections import deque

def bfs() :
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    #cnt = 1
    cnt = 1
    while q :
        a, b = q.popleft()

        for i in range(4) :
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < m and 0 <= ny < n :
                if not(visited[nx][ny]) and arr[nx][ny] == 0 :
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cnt +=1

    return cnt

m, n, k = map(int, input().split())
arr = [[0] * n for _ in range(m)]
visited = [[False] * n for _ in range(m)]

# 좌표에 직사각형 표시
for _ in range(k) :
    lx, ly, rx, ry = map(int, input().split())
    for x in range(m-ry, m-ly) :
        for y in range(lx, rx) :
            if arr[x][y] == 0 :
                arr[x][y] = 1

q = deque()
area = 0
result = []
for i in range(m) :
    for j in range(n) :
        if arr[i][j] == 0 and not(visited[i][j]) :
            visited[i][j] = True
            q.append((i, j))
            result.append(bfs())
            area += 1

print(area)
result.sort()
for width in result :
    print(width, end=' ')

# 4. 검토 및 개선 :
# while q :
#     a, b = q.popleft()
#     visited[a][b] = True
#     cnt += 1
# 처럼 쓰면 안됨, q에 중복된 값들을 거르지않고 cnt를 증가시키기때문
# 따라서 cnt 증가는 if 문으로 거르자

# 모눈종이가 맨 아래 왼쪽이 (0, 0)이라고 되어있는데
# 모눈종이를 뒤집어도 분리된 영역의 개수와 넓이는 변하지 않으므로
# 다음과 같이 해결할 수 있다.
# 나머지 방식은 동일

m, n, k = map(int, input().split())
arr = [[0] * n for _ in range(m)]
for _ in range(k) :
    y1, x1, y2, x2 = map(int, input().split())
    for x in range(x1, x2) :
        for y in range(y1, y2) :
            if arr[x][y] == 0 :
                arr[x][y] = 1


# 5. 기록 :
# dfs의 시간복잡도
# 인접 행렬을 이용한 구현 : O(V^2)
# 인접 리스트를 이용한 구현 : O(V + E)
# 직사각형이라고 인접행렬이아니라, 그래프의 연결관계를 이차원 배열로
# 나타낸 것이 인접행렬이다.