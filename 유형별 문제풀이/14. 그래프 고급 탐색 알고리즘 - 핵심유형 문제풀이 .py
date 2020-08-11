# 10282번 - 해킹
# 난이도 중/ 다익스트라 최단 경로/ 50분

# 내 풀이 [틀렸다가 강의보고 고쳐서 맞음]
##import heapq
##
##test_case = int(input())
##
##for _ in range(test_case) :
##    n, d, c = map(int, input().split())
##    adjacent = [[]for i in range(n + 1)]
##    time = [float('inf')] * (n + 1)
##    time[c] = 0
##    
##    for i in range(d) :
##        a, b, s = map(int, input().split())
##        adjacent[b].append([s, a])
##
##    queue = []
##    heapq.heappush(queue, [0, c])
##
##    while queue :
##        current_s, current_n = heapq.heappop(queue)
##
##        if current_s > time[current_n] :
##            continue
##
##        for adjacent_s, adjacent_n in adjacent[current_n] :
##            newtime = time[current_n] + adjacent_s
##            if newtime < time[adjacent_n] :
##                time[adjacent_n] = newtime
##                queue.append([newtime, adjacent_n])
##
##    cnt = 0
##    max_time = 0
##    for i in range(1, n + 1) :
##        if time[i] != float('inf') :
##            cnt += 1
##            if max_time < time[i] :
##                max_time = time[i] # 시간 구하기
##    print(cnt, end=' ')
##    print(max_time)

# 강의
# 기본적인 다익스트라 최단 경로 알고리즘 문제
# 도달할 수 잇는 정점들의 개수와 최대 거리를 출력
# 정점의 개수 N이 최대 10000이고, 간선의 개수 D는 최대 100000
# 우선순위 큐를 이용하여, 시간복잡도는 O(NlogD)로 해결 가능

##import heapq
##import sys
##input = sys.stdin.readline
##
##def dijkstra (start) :
##    heap = []
##    heapq.heappush(heap, (0, start))
##    distance[start] = 0
##
##    while heap :
##        dist, now = heapq.heappop(heap)
##        if distance[now] < dist :
##            continue
##        for i in adj[now] :
##            cost = dist + i[0]
##            if distance[i[1]] > cost :
##                distance[i[1]] = cost
##                heapq.heappush(heap, (cost, i[1]))
##                
##for _ in range(int(input())) :
##    n, m, start = map(int, input().split())
##    adj = [[] for i in range(n + 1)]
##    distance = [1e9] * (n + 1)
##
##    for _ in range(m) :
##        x, y, cost = map(int, input().split())
##        adj[y].append((cost, x))
##
##    dijkstra(start)
##    cnt = 0
##    max_distance = 0
##
##    for i in distance :
##        if i != 1e9 :
##            cnt += 1
##            if i > max_distance :
##                max_distance = i
##
##    print(cnt, max_distance)

# 한번 더 혼자
##import heapq
##import sys
##input = sys.stdin.readline
##
##def dijkstra (start) :
##    heap_data = []
##    heapq.heappush(heap_data, (0, start))
##    distance[start] = 0
##
##    while heap_data :
##        c, node = heapq.heappop(heap_data)
##
##        if c > distance[node] :
##            continue
##
##        for ec, e_node in adj[node] :
##            total = c + ec
##            if total < distance[e_node] :
##                distance[e_node] = total
##                heap_data.append((total, e_node))
##    
##for _ in range(int(input())) :
##    n, m ,start = map(int, input().split())
##    adj = [[]for i in range(n + 1)]
##    distance = [1e9] * (n + 1)
##    
##    for i in range(m) :
##        x, y, cost = map(int, input().split())
##        adj[y].append((cost, x))
##
##    dijkstra(start)
##
##    cnt = 0
##    max_value = 0
##
##    for dist in distance :
##        if dist != 1e9 :
##            cnt += 1
##            if dist > max_value :
##                max_value = dist
##
##    print(cnt, max_value)
