# 2606번 - 바이러스
# 난이도 하/ BFS, DFS, 30분

# 내 풀이 [맞음]

# 1. BFS 이용 [맞음]
##from collections import deque
##
##def bfs(x) :
##    q = deque([x])
##    while q :
##        v = q.popleft()
##        if v not in visited :
##            visited.append(v)
##
##            for e in array[v] :
##                if e not in visited :
##                    q.append(e)
##
##n = int(input())
##c = int(input())
##
##array = [[] for _ in range(n + 1)]
##
##for _ in range(c) :
##    x,y = map(int, input().split())
##    array[x].append(y)
##    array[y].append(x)
##
##visited = []
##bfs(1)
##
##if 1 in visited :
##    result = len(visited) - 1
##else :
##    result = len(visited)
##
##print(result)

# 2. DFS 이용 [맞음]]

##def dfs(x) :
##    if not(visited[x]) :
##        visited[x] = 1
##        
##        for next in array[x] :
##            if not(visited[next]) :
##                dfs(next)
##
##n = int(input())
##c = int(input())
##
##array = [[] for _ in range(n + 1)]
##
##for _ in range(c) :
##    x,y = map(int, input().split())
##    array[x].append(y)
##    array[y].append(x)
##
##visited = [0] * (n + 1)
##dfs(1)
##cnt = 0
##
##for i in range(2, n + 1) :
##    if visited[i] :
##        cnt += 1
##
##print(cnt)


# 강의
# 단순히 시작 정점에서부터 도달할 수 있는 노드의 수를 계산하는 문제
# DFS 또는 BFS를 이용하여 방문하게 되는 노드의 개수를 계산
# 컴퓨터의 수가 적으므로, DFS를 이용해 빠르게 문제를 푸는 것이 유리(코드가 짧음)
# (컴퓨터의 수가 많을 때는 재귀함수 이용하는 것이 불리할 수 있음)

##n = int(input())
##m = int(input())
##adj = [[] for _ in range(n + 1)]
##visited = [False] * (n+1)
##count = 0
##
##for _ in range(m) :
##    x, y = map(int, input().split())
##    adj[x].append(y)
##    adj[y].append(x)
##
##def dfs (current_pos) :
##    global count
##    count += 1
##    
##    visited[current_pos] = True
##    
##    for next_pos in adj[current_pos] :
##        if not(visited[next_pos]) :
##            dfs(next_pos)
##
##dfs(1)
##print(count - 1)




# 1012번 - 유기농 배추
# 난이도 하/ DFS, BFS/ 30분
