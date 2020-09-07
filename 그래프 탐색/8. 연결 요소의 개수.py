# 1. 문제 이해 :
# 연결 요소란 나누어진 각각의 그래프이다.
# 연결 요소의 개수를 구하는 프로그램
# 정점의 개수 N, 간선의 개수 M (N은 1000이하, M은 50만 이하)
# N, M, 쌍 입력
# 연결 요소의 개수 출력

# 2. 풀이 계획 및 검증
# BFS, DFS로 가능
# 둘다 O(V+E)

# 3. 구현
def dfs(v) :
    if not(visited[v]) : # 위에서 걸렀으므로 바로 True 가능
        visited[v] = True

        for adjacent in arr[v] :
            if not(visited[adjacent]) :
                dfs(adjacent)

n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
cnt = 0

for _ in range(m) :
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

for i in range(1, n+1) :
    if not(visited[i]) :
        dfs(i)
        cnt += 1

print(cnt)

# 4. 검토 및 개선
# python은 재귀 제한이 3000으로 걸려있으므로
# 재귀 허용치가 넘어가면 런타임 에러 일으킴
# sys.setrecursionlimit(10000)처럼 허용해야한다.
# 여기서는 정점의 개수가 1000 이하이므로 런타임 에러를 일으키지 않았다.

# 5. 기록