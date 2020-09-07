# 2606 - 바이러스 문제

# 1. 문제 이해
# 바이러스는 연결된 컴퓨터에 퍼짐
# 컴퓨터 수 100이하 1~100
# 입력 : 컴퓨터의수 / 컴퓨터 쌍의 수 / 쌍
# 출력 : 1번 컴퓨터가 바이러스 걸렸을때 1번으로인해
# 바이러스 걸리게되는 컴퓨터 수 (1 제외)

# 2. 풀이 계획
# BFS or DFS로 바이러스 퍼뜨릴수있음
# O(V+E) 이므로 O(100 + 9900) 가능

# 3. 구현
def dfs(v) :
    global cnt
    # visited[v] = True
    # cnt += 1

    for adjacent in arr[v] :
        if not(visited[adjacent]) :
            visited[adjacent] = True
            cnt += 1
            dfs(adjacent)

n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
visited = [False] * (n+1) # (n+1)인데 n으로 씀...!!
cnt = 0

for _ in range(m) :
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited[1] = True
dfs(1)
print(cnt)

# 4. 검토 및 개선
# 이 문제에서 DFS와 BFS풀이의 차이는 거의 없다.
# 일반적으로 모든 경우를 다 탐색하는 경우는 DFS가 더 선호된다고 한다.

# 5. 기록 :
# visited에서 n+1개를 만들어줬어야했는데 (컴퓨터가 1로 시작하니까)
# n개만 만들어서 런타임 에러가 났다 ....!ㅠㅠ

# 런타임에러나서 sys.setrecursionlimit(10000) 했는데 필요없었다.
# visited 체크 하니까 recursion을 최대 100번하기때문 !
# c.f. python은 recursion 3000번까지 가능


# 오랜만에 BFS로 풀어보기
from collections import deque

def bfs(q) :
    cnt = 0
    while q :
        for adj in arr[q.popleft()] :
            if not(visited[adj]) :
                visited[adj] = True
                cnt += 1
                q.append(adj)
    return cnt


n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m) :
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

q= deque([1])
visited[1] = True
print(bfs(q))