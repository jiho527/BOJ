# 백준 1260 - DFS와 BFS
# 1. 문제 이해 및 계획: DFS, BFS로 탐색,
# 정점 번호가 작은 것부터 방문
# 정점 : N, 간선 : M, 시작 정점 : V
# m개의 정점 쌍, 간선은 양방향
# DFS 수행결과, BFS 수행결과 순으로 출력

# 2. 검증 : BFS, DFS -> O(N + M)
# 3. 구현
# 4. 검토 및 개선
# 5. 경험 및 기록 : 작은 조건(정렬) 주의, 출력 형식 맞추기주의

from collections import deque

# stack을 이용하지 않아서 숫자가 정렬되어있으면 작은 것부터 방문한다
def dfs(v) :
    if v not in stack_visited :
        stack_visited.append(v)

    for e in adj[v] :
        if e not in stack_visited :
            dfs(e)

def bfs() :
    while q :
        node = q.popleft()
        if node not in q_visited :
            q_visited.append(node)
        for e in adj[node] :
            if e not in q_visited :
                q.append(e)


n, m, v = map(int, input().strip().split())
adj = [[] for _ in range(n + 1)]
stack_visited = []
q = deque()
q.append(v)
q_visited = []

for _ in range(m) :
    a, b = map(int, input().strip().split()) # 간선으로 이어진 정점
    adj[a].append(b)
    adj[b].append(a)

for i in range(n) :
    adj[i].sort() # 정점 번호가 작은 것부터 방문

dfs(v)
bfs()

for _ in stack_visited :
    print(_, end=' ')
print()
for _ in q_visited :
    print(_, end=' ') # 출력 포맷 맞지않아서 틀렸음;;