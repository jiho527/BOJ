# 1260번 - DFS와 BFS
# 난이도 하/ DFS, BFS, 30분

# 내 풀이 [맞음]
##n, m, v = map(int, input().split())
##graph = [[] for _ in range(n + 1)]
##
##for _ in range(m) :
##    x, y = map(int, input().split())
##    graph[x].append(y)
##    graph[y].append(x)
##
##for i in range(n + 1) :
##    graph[i].sort(reverse=True)
##    
##stack = [v]
##dfs_result = []
##
##queue = [v]
##bfs_result = []
##
##while stack :
##    data = stack.pop()
##    if data not in dfs_result :
##        dfs_result.append(data)
##
##        for num in graph[data]:
##            stack.append(num)
##
##
##for i in range(n + 1) :
##    graph[i].sort()
##
##while queue :
##    data = queue.pop(0)
##    if data not in bfs_result :
##        bfs_result.append(data)
##
##        for num in graph[data] :
##            queue.append(num)
##
##for data in dfs_result :
##    print(data, end=' ')
##    
##print()
##
##for data in bfs_result :
##    print(data, end=' ')


# 강의
# 정점번호가 작은 것을 먼저 방문해야함
# 모든 노드와 간선을 차례대로 조회하여 O(N + M)의 시간복잡도로 문제 해결
# 이 문제를 매우 빠르게 풀 수 있도록 숙달해라 !! 많이 많이 연습!!
# 큐 구현을 위해 collections 라이브러리의 deque 사용

from collections import deque

def dfs(v) :
    print(v, end=' ')
    visited[v] = True
    for e in adj[v] :
        if not(visited[e]) :
            dfs(e)

def bfs(v) :
    q = deque([v])
    while q :
        v = q.popleft()
        if not(visited[v]) : # 꺼낸 노드가 방문한 것인지 아닌지 확인
            visited[v] = True
            print(v, end=' ')

            for e in adj[v] :
                if not(visited[e]) :
                    q.append(e)

n, m, v = map(int, input().split())

adj = [[]for _ in range(n + 1)]

for _ in range(m) :
    x,y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

for e in adj :
    e.sort()

visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)
