# 1. 문제 이해 :
# 연구소 크기 N 세로 x M 가로 둘다 9보다 작음
# 빈칸 0, 벽 1, 바이러스 2
# 바이러스는 상하좌우로 이동
# 세울 수 있는 벽의 개수 3
# 안전 영역 크기의 최댓값을 출력(0의 개수)

# 2. 풀이 계획 및 검증 :
# 연구소의 크기가 최대 64이고,
# 벽을 세개 놓을 수 있으니까 64*64*64 번 비교
# 배열에서 2 찾아서 바이러스 이동해서 2로 만들기 dfs -> O(64 * 4)
# 0 개수 세서 전보다 크면 result에 저장

# 3. 구현
# import copy
#
# def dfs(i, j) :
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]
#
#     copy_arr[i][j] = 2
#
#     for _ in range(4) :
#         nx = i + dx[_]
#         ny = j + dy[_]
#
#         if 0 <= nx < n and 0 <= ny < m :
#             if not(copy_visited[nx][ny]) and copy_arr[nx][ny] == 0 :
#                 dfs(nx, ny)
#
#
# n, m = map(int, input().split())
# arr = [[] for _ in range(n)]
# visited = [[False] * m for _ in range(n)]
# result = 0
#
# for i in range(n) :
#     arr[i].extend(list(map(int, input().split())))
#
# for i in range(n) :
#     for j in range(m) :
#         copy_arr = copy.deepcopy(arr) # 얕은복사 = arr[:]
#         copy_visited = copy.deepcopy(visited) # 깊은복사
#         if arr[i][j] == 0 :
#             copy_arr[i][j] = 1
#
#             for k in range(n) :
#                 for l in range(m) :
#                     if arr[k][l] == 0 :
#                         copy_arr[k][l] = 1
#
#                         for o in range(n) :
#                             for p in range(m) :
#                                 if arr[o][p] == 0 :
#                                     copy_arr[o][p] = 1
#
#                                     for q in range(n) :
#                                         for r in range(m) :
#                                             if copy_arr[q][r] == 2 :
#                                                 dfs(q, r)
#
#                                                 cnt = 0
#                                                 for s in range(n) :
#                                                     for t in range(m) :
#                                                         if copy_arr[s][t] == 0 :
#                                                             cnt += 1
#                                                             if cnt >= result :
#                                                                 result = cnt
#
# print(result)

# 검토 및 개선 : for문을 너무 많이 무분별하게 사용했다.
# 따라서 그 전 for문보다 cnt 계산을 더 먼저하여 완전히 틀렸다.

# n*m 개 중에서 3개를 뽑는 Combination(조합)을 구해야한다.
# 숫자를 0 ~ n*m 까지 증가시킬때, (i/m, i%m)을 좌표로 하면
# 2차원 배열의 모든 인덱스를 탐색할 수 있다.

# import copy # 깊은 복사를 위해 (주소값까지 따로) / 얕은 복사 => arr[:] (주소값은 같음)
# import sys
#
# n = m = 0
# arr = []
# virusList = [] # 바이러스 좌표를 미리 list에 저장
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# maxVal = 0
#
# # 안전구역 넓이 구하기
# def getSafeArea(copyed) :
#     safe = 0
#     for i in range(n) :
#         for j in range(m) :
#             if copyed[i][j] == 0 :
#                 safe += 1
#     return safe
#
# # DFS로 바이러스 퍼뜨리기
# def spreadVirus (x, y, copyed) :
#     for i in range(4) :
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if 0 <= nx < n and 0 <= ny < m :
#             if copyed[nx][ny] == 0 :
#                 copyed[nx][ny] = 2
#                 spreadVirus(nx, ny, copyed)
#
# # 조합으로 벽 3개 놓는 모든 경우 구하기
# def setWall (start, depth) :
#     global maxVal # 전역변수
#
#     if depth == 3 : # 벽 3개를 놓은 경우
#         copyed = copy.deepcopy(arr)
#         # 최대값을 찾기위해 조합에따른 결과값을 계속 비교해야하므로 copy
#
#         for i in range(len(virusList)) :
#             [virusX, virusY] = virusList[i]
#             spreadVirus(virusX, virusY, copyed)
#
#         maxVal = max(maxVal, getSafeArea(copyed))
#         return
#
#     for i in range(start, n*m) :
#         x = (int) (i/m) # python에서 나누면 실수로 변환되므로
#         y = (int) (i%m)
#
#         if arr[x][y] == 0 :
#             arr[x][y] = 1
#             setWall(i+1, depth + 1)
#             arr[x][y] = 0 # 세웠던 벽을 없애기
#
#
# n, m = map(int, sys.stdin.readline().split())
# for i in range(n) :
#     arr.append(list(map(int, sys.stdin.readline().split())))
#
# for i in range(n) :
#     for j in range(m) :
#         if arr[i][j] == 2 :
#             virusList.append([i, j])
#
# setWall(0, 0)
# print(maxVal)

# 기록:
# 뜻이 있는 숫자들로 이루어진경우 잘 생각해보면
# visited 같은 True/False 체크를 해줄 필요가 없다.
# virusList같이 리스트를 먼저 작성해놓으면 전체를 스캔할 필요가 없다.

# 브루트포스 + 그래프 탐색(BFS or DFS)가 합쳐진 문제다.
# 브루트포스를 연습해야겠다.

# 다시 풀어보기
import copy

# 안전구역 구하기
def getSafeArea(copyed) :
    safe = 0
    for i in range(n) :
        for j in range(m) :
            if copyed[i][j] == 0 :
                safe += 1
    return safe

# 바이러스 퍼뜨리기
def spreadVirus(x, y, copyed) :
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4) :
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m :
            if copyed[nx][ny] == 0 :
                copyed[nx][ny] = 2
                spreadVirus(nx, ny, copyed)


# 벽 3개 세우기
def setWalls (start, depth) :
    global maxVal

    if depth == 3 :
        copyed = copy.deepcopy(arr)

        for virus in virusList :
            virusX = virus[0]
            virusY = virus[1]
            spreadVirus(virusX, virusY, copyed)

        maxVal = max(maxVal, getSafeArea(copyed))
        return

    for i in range(start, n*m) :
        x = (int)(i/m)
        y = (int)(i%m)

        if arr[x][y] == 0 : # 빼먹음 ...!!!!
            arr[x][y] = 1
            setWalls(start + 1, depth + 1)
            arr[x][y] = 0


n, m = map(int, input().split())
arr = []
virusList = []
maxVal = 0
for _ in range(n) :
    arr.append(list(map(int, input().split())))

for i in range(n) :
    for j in range(m) :
        if arr[i][j] == 2 :
            virusList.append([i, j])

setWalls(0, 0)
print(maxVal)

