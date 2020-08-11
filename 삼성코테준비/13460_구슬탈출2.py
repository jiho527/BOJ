# # 내 풀이 [틀림]
# # 10번 이하로 움직이면 움직인 횟수 출력, 10번 초과면 -1 출력
# # 문제점 : 두 공이 동시에 움직이는 것을 처리안해줌, 지나간 곳을 체크 안해줌, 최단 거리구할 때 bfs 생각 못함
#
# def move (arr, cnt, yr, xr, yb, xb, result) :
#     cnt += 1
#     print(cnt)
#     print(arr)
#     print(yr, xr, yb, xb)
#
#     if cnt > 10:
#         return
#
#     # 왼쪽
#     while arr[yr][xr - 1] != 'O' and arr[yr][xr - 1] == '.' :
#         arr[yr][xr-1] = 'R'
#         arr[yr][xr] = '.'
#         xr -= 1
#
#     while arr[yb][xb - 1] != 'O' and arr[yb][xb - 1] == '.':
#         arr[yb][xb - 1] = 'B'
#         arr[yb][xb] = '.'
#         xb -= 1
#
#     if arr[yr][xr - 1] == 'O' and arr[yb][xb - 1] != 'O' :
#         result.append(cnt)
#
#     move(arr, cnt, yr, xr, yb, xb, result)
#
#
#     # 오른쪽
#     while arr[yr][xr + 1] != 'O' and arr[yr][xr + 1] == '.':
#         arr[yr][xr + 1] = 'R'
#         arr[yr][xr] = '.'
#         xr += 1
#
#     while arr[yb][xb + 1] != 'O' and arr[yb][xb + 1] == '.':
#         arr[yb][xb + 1] = 'B'
#         arr[yb][xb] = '.'
#         xb += 1
#
#     if arr[yr][xr + 1] == 'O' and arr[yb][xb + 1] != 'O':
#         result.append(cnt)
#
#     move(arr, cnt, yr, xr, yb, xb, result)
#
#
#     # 위쪽
#     while arr[yr + 1][xr] != 'O' and arr[yr + 1][xr] == '.':
#         arr[yr + 1][xr] = 'R'
#         arr[yr][xr] = '.'
#         yr += 1
#
#     while arr[yb + 1][xb] != 'O' and arr[yb + 1][xb] == '.':
#         arr[yb + 1][xb] = 'B'
#         arr[yb][xb] = '.'
#         yb += 1
#
#     if arr[yr + 1][xr] == 'O' and arr[yb + 1][xb] != 'O':
#         result.append(cnt)
#
#     move(arr, cnt, yr, xr, yb, xb, result)
#
#
#     # 아래쪽
#     while arr[yr - 1][xr] != 'O' and arr[yr - 1][xr] == '.':
#         arr[yr - 1][xr] = 'R'
#         arr[yr][xr] = '.'
#         yr -= 1
#
#     while arr[yb - 1][xb] != 'O' and arr[yb - 1][xb] == '.':
#         arr[yb - 1][xb] = 'B'
#         arr[yb][xb] = '.'
#         yb -= 1
#
#     if arr[yr - 1][xr] == 'O' and arr[yb - 1][xb] != 'O':
#         result.append(cnt)
#
#     move(arr, cnt, yr, xr, yb, xb, result)
#
#
# n, m = map(int, input().split(" ")) # n: 세로 m: 가로
#
# arr = []
# result = []
# for i in range(n) :
#     arr.append(list(input())) # 파이썬의 문자열은 변경 x -> string을 list로 변환방법 : arr= list(string)
#
#
# for y in range(n) :
#     for x in range(m) :
#         if arr[y][x] == 'R' :
#             yr = y
#             xr = x
#
#         if arr[y][x] == 'B' :
#             yb = y
#             xb = x
#
# move(arr, 0, yr, xr, yb, xb, result)
#
# print("result: ", result)
#
# if min(result) > 10 :
#     print(-1)
# else :
#     print(min(result))




# 구슬탈출 - 정답 코드
# 구슬 두개가 동시에 움직이므로 4차원 배열을 통해 방문여부 체크
# from sys import stdin
# from collections import deque # bfs
#
# input = stdin.readline
# n, m = map(int, input().split())
# a = [list(input().strip()) for _ in range(n)]
# check = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
# # 4차원 배열의 인덱스 [빨간 x좌표][빨간 y좌표][파란 x좌표][파란 y좌표]
# dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
# q = deque()
#
# def init() :
#     _rx, _ry, _bx, _by = [0] * 4
#     for i in range(n) : # 현재 빨간공 파란공 좌표값 저장
#         for j in range(m) :
#             if a[i][j] == 'R' :
#                 _rx, _ry = i, j
#             elif a[i][j] == 'B' :
#                 _bx, _by = i, j
#     q.append((_rx, _ry, _bx, _by, 0))
#     check[_rx][_ry][_bx][_by] = True
#
# def move(_x, _y, _dx, _dy, _c) :
#     while a[_x+_dx][_y+_dy] != '#' and a[_x][_y] != 'O' : # 다음 이동이 벽이거나 구멍이 아닐 때 까지 이동
#         _x += _dx
#         _y += _dy
#         _c += 1
#     return _x, _y, _c
#
# def bfs() :
#     while q :
#         rx, ry, bx, by, d = q.popleft()
#         if d >= 10 : # 10번보다 많이 움직이면 0 출력
#             break
#         for i in range(4) :
#             nrx, nry, rc = move(rx, ry, dx[i], dy[i], 0)
#             nbx, nby, bc = move(bx, by, dx[i], dy[i], 0)
#             if a[nbx][nby] == 'O' :
#                 continue
#             if a[nrx][nry] == 'O' :
#                 print(1)
#                 return
#             if nrx == nbx and nry == nby : # 빨, 파 같은경우 많이 이동한 것이 한칸 전으로
#                 if rc > bc :
#                     nrx, nry = nrx-dx[i], nry-dy[i]
#                 else :
#                     nbx, nby = nbx-dx[i], nby-dy[i]
#             if not check[nrx][nry][nbx][nby] : # 방문하지 않았으면
#                 check[nrx][nry][nbx][nby] = True
#                 q.append((nrx, nry, nbx, nby, d+1))
#     print(0)
#
# init()
# bfs()





# 구슬탈출2 - 정답 코드
# depth를 출력, 실패하면 -1 출력
# 최단거리 -> bfs로 구하기
# from sys import stdin
# from collections import deque # bfs
#
# input = stdin.readline
# n, m = map(int, input().split())
# a = [list(input().strip()) for _ in range(n)]
# check = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
# # 4차원 배열의 인덱스 [빨간 x좌표][빨간 y좌표][파란 x좌표][파란 y좌표]
# dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
# q = deque()
#
# def init() :
#     _rx, _ry, _bx, _by = [0] * 4
#     for i in range(n) : # 현재 빨간공 파란공 좌표값 저장
#         for j in range(m) :
#             if a[i][j] == 'R' :
#                 _rx, _ry = i, j
#             elif a[i][j] == 'B' :
#                 _bx, _by = i, j
#     q.append((_rx, _ry, _bx, _by, 1)) # 위치정보와 depth
#     check[_rx][_ry][_bx][_by] = True
#
# def move(_x, _y, _dx, _dy, _c) :
#     while a[_x+_dx][_y+_dy] != '#' and a[_x][_y] != 'O' : # 다음 이동이 벽이거나 구멍이 아닐 때 까지 이동
#         _x += _dx
#         _y += _dy
#         _c += 1
#     return _x, _y, _c
#
# def bfs() :
#     while q :
#         rx, ry, bx, by, d = q.popleft()
#         if d >= 10 : # 10번보다 많이 움직이면 0 출력
#             break
#         for i in range(4) :
#             nrx, nry, rc = move(rx, ry, dx[i], dy[i], 0)
#             nbx, nby, bc = move(bx, by, dx[i], dy[i], 0)
#             if a[nbx][nby] == 'O' :
#                 continue
#             if a[nrx][nry] == 'O' :
#                 print(d)
#                 return
#             if nrx == nbx and nry == nby : # 빨, 파 같은 칸인 경우 많이 이동한 것이 한칸 전으로
#                 if rc > bc :
#                     nrx, nry = nrx-dx[i], nry-dy[i]
#                 else :
#                     nbx, nby = nbx-dx[i], nby-dy[i]
#             if not check[nrx][nry][nbx][nby] : # 방문하지 않았으면
#                 check[nrx][nry][nbx][nby] = True
#                 q.append((nrx, nry, nbx, nby, d+1))
#     print(-1)
#
# init()
# bfs()




# 다시 풀기
from sys import stdin
from collections import deque

#input = stdin.readline # 한 라인 입력받기

def move(x, y, dx, dy) :
    cnt = 0 # 이동한 칸 수 -> 더 많이 이동한 구슬이 한칸 전으로
    while arr[x+dx][y+dy] != '#' and arr[x][y] != 'O' :
        # 다음 이동이 벽이거나 현재 구멍에 있는 게 아닐 때 까지
        x = x + dx
        y = y + dy
        cnt += 1
    return x, y, cnt


def bfs() :
    while queue :
        rx, ry, bx, by, depth = queue.popleft()
        check[rx][ry][bx][by] = True

        if depth > 10 :
            break

        for i in range(4) :
            mrx, mry, r_cnt = move(rx, ry, dx[i], dy[i])
            mbx, mby, b_cnt = move(bx, by, dx[i], dy[i])

            if arr[mbx][mby] == 'O' : # 파란구슬이 구멍에 떨어지면
                continue
            if arr[mrx][mry] == 'O' : # 빨간 구슬이 구멍에 떨어지면
                print(depth)
                return

            if mrx == mbx and mry == mby :
            # 빨간 구슬과 파란 구슬은 같은 칸에 있을 수 없다
                if r_cnt > b_cnt :
                    mrx, mry = mrx-dx[i], mry-dy[i]
                else :
                    mbx, mby = mbx-dx[i], mby-dy[i]

            if not check[mrx][mry][mbx][mby] :
                queue.append((mrx, mry, mbx, mby, depth + 1))

    print(-1)


n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
check = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
# rx, ry, bx, by의 4차원 배열
queue = deque()
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)

for i in range(n) :
    for j in range(m) :
        if arr[i][j] == 'R' :
            rx, ry = i, j
        elif arr[i][j] == 'B' :
            bx, by = i, j

queue.append((rx, ry, bx, by, 1))
bfs()