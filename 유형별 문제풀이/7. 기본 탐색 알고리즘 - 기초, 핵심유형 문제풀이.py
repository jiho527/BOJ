#[기초 문제풀이]

# 1543번 - 문서 검색 [틀림]

data = input()
search = input()
cnt = 0

for i in range(len(data) - len(search) + 1) : # range 설정 이렇게했더니 맞음
    if data [:len(search)] == search :
        cnt += 1
        data = data[len(search):]
    else :
        data = data[1:]

print(cnt)

# 문서의 길이는 최대 2500, 단어의 길이는 최대 50이므로
# 모든 경우의 수를 계산하여 문제 해결 가능 -> O(NM)

documnet = input()
word = input()

index = 0
result = 0

while len(document) - index >= len(word) :
    if document[index: index + len(word)] == word :
        result += 1
        index += len(word)
    else :
        index += 1
print(result)

# 한번 더

##document = input()
##word = input()
##
##idx = 0
##cnt = 0
##
##while len(document) - idx >= len(word) :
##    if document[idx: idx + len(word)] == word :
##        idx += len(word)
##        cnt += 1
##    else :
##        idx += 1
##print(cnt)




# 1568번 - 새

sec = 1
total = 0
bird = int(input())

while True :
    if sec <= bird :
        bird -= sec
        if bird == 0 :
            total += sec
            break
        else :
            sec += 1
    else :
        total += (sec - 1)
        sec = 1

print(total)

# 강의 답안

n = int(input()) # 새
result = 0
k = 1

while n != 0 :
    if k > n :
        k = 1
    n -= k
    k += 1
    result += 1

print(result)

# N이 최대 십억이지만, K가 반복적으로 증가(등차수열) 하므로,
# N² = 십억 이라고 할 수 있으므로 시간복잡도는 O(root(N))이라고 할 수 있다.
# 따라서 요구하는대로 단순히 구현하여 정답을 받을 수 있다.

# 한번 더
##n = int(input())
##k = 1
##result = 0
##
##while n != 0 :
##    if k > n :
##        k = 1
##    n -= k
##    k += 1
##    result += 1
##print(result)




# 1302번 - 베스트셀러

n = int(input())
books = {}
best_seller = []

for _ in range(n) :
    book = input()
    
    if book not in books :
        books[book] = 1
    else :
        books[book] += 1

max = 0
for book in books :
    if max < books[book] :
        max = books[book]

for book in books :
    if books[book] == max :
        best_seller.append(book)

best_seller.sort()
print(best_seller[0])

# 문제 풀이 핵심 아이디어
# 등장 횟수를 계산할 때는 파이썬의 Dictionary 자료형 이용하면 효과적

n = int(input())
books = {}

for _ in range(n) :
    book = input()
    if book not in books :
        books[book] = 1
    else :
        books[book] += 1

target = max(books.values())
# max함수의 인자로는 iterable 자료형(for문으로 출력 가능한 자료형)
# 딕셔너리에서 값만 받는 함수 : values() / 키만 : keys()/ 쌍 : items()
array = []

for book, number in books.items() :
    if number == target :
        array.append(book)

print(sorted(array)[0])



# 1668번 - 트로피 진열 [틀림]

##n = int(input())
##array = []
##left_cnt = 1
##right_cnt = 1
##
##for _ in range(n) :
##    array.append(int(input()))
##
##for i in range(n - 1) :
##    if array[i] < array [i+1] :
##        left_cnt += 1
##
##for j in range(n-1, 0, -1) :
##    if array[j] < array[j - 1] :
##        right_cnt += 1
##
##print(left_cnt)
##print(right_cnt)

# 길이가 일정하게 증가하는 것만 생각함
# e.g. 3 4 6 4 3 7 2 같이 트로피가 정렬되어있다면 다음과같이 풀 수 없음

# 아이디어만 보고 다시 푼 것

n = int(input())
array = []
left_cnt = 0
right_cnt = 0

for _ in range(n) :
    array.append(int(input()))

max = 0
for i in range(n) :
    if max < array[i] :
        left_cnt += 1
        max = array[i]

max = 0
for j in range(n-1, -1, -1) :
    if max < array[j]:
        right_cnt += 1
        max = array[j]

print(left_cnt)
print(right_cnt)

# 강의 답안

def ascending (array) :
    now = array[0]
    result = 1
    for i in range(1, len(array)) :
        if now < array[i] :
            result += 1
            now = array[i]
    return result

n = int(input())
array = []

for _ in range(n) :
    array.append(int(input()))

print(ascending(array))
array.reverse() # 배열을 거꾸로
print(ascending(array))



# 1236번 - 성 지키기 [틀림]

N, M = map(int, input().split())
rows = set()
cols = set()

arr = []

for row in range(N) :
    arr.append(input())
    
for row in range(N) :
    for col in range(M) :
        if arr[row][col] == 'X' :
            rows.add(row)
            cols.add(col)

if N - len(rows) >= M - len(cols) :
    print(N - len(rows))
else :
    print(M - len(cols))

# 다시 고쳐서 맞음

# 문제풀이 핵심 아이디어
# 행 기준, 열 기준으로 필요한 경비원의 수를 각각 계산하여 더 큰수를 출력

n, m = map(int, input().split())
array = []

for _ in range(n) :
    array.append(input())

row = [0] * n
column = [0] * m

for i in range(n) :
    for j in range(m) :
        if array[i][j] == 'X' :
            row[i] = 1
            column[j] = 1

row_count = 0
for i in range(n) :
    if row[i] == 0 :
        row_count += 1

column_count = 0
for j in range(m) :
    if column[j] == 0 :
        column_count += 1

print(max(row_count, column_count))



# [핵심 유형 문제풀이]

# 2110번 - 공유기 설치 [틀림] 
# 이진 탐색 -> 웬만하면 다 어려움

# 접근방법 모르겠음 ㅠㅠ

# 문제 풀이 핵심 아이디어
# 집의 개수 N은 최대 이십만개, 집의 좌표는 최대 십억

# -> 매우 큰 수를 탐색해야한다 -> 이진탐색이나 O(logX)이나 O(root(X))
# 같은 알고리즘을 이용해야한다고 가정하고 문제 풀기 !

# 이진탐색 이용 -> O(N * logX) = 육백만
# 가장 인접한 두 공유기 사이의 최대 'gap'을 이진탐색으로 찾기


# 이진탐색
# min과 max를 설정한 다음에 그 중간 값을 찾고 다시 min과 max를 갱신하고
# 다시 중간값을 찾는 과정을 반복

# 구현 방법
# 1. 재귀적
# 2. 반복적 -> 더 유리

n, c = list(map(int, input().split(' ')))

array = []
for _ in range(n) :
    array.append(int(input()))
array = sorted(array)

start = array[1] - array[0]
end = array[-1] - array[0]
result = 0

while start <= end :
    mid = (start + end) //2
    value = array[0]
    count = 1

    for i in range(1, len(array)) :
        if array[i] >= value + mid :
            count += 1
    if count >= c :
        start = mid + 1
        result = mid
    else :
        end = mid - 1

print(result)


# 혼자

##array = []
##n, c = map(int, input().split(' '))
##
##for _ in range(n) :
##    array.append(int(input()))
##
##array.sort()
##
##start = array[1] - array[0]
##end = array[-1] - array[0]
##result = 0
##
##while start <= end :
##    mid = (start + end) // 2
##    value = array[0]
##    cnt = 1
##
##    for i in range(1, len(array)) :
##        if array[i] >= value + mid :
##            cnt += 1
##            value = array[i]
##
##    if cnt >= c :
##        start = mid + 1
##        result = mid
##    else :
##        end = mid - 1
##
##print(result)




# 1939번 - 중량제한 [틀림]

##def find(islands, a, b, max) :
##    for island in islands[a] :
##        if island[1] == b :
##            if max < island[0] :
##                max = island[0]
##            return max
##        
##    max = island[0] # for문 안에 들어가면 안됨
##    return find(islands, island, b, max)
##    
##
##n, m = map(int, input().split())
##islands = {}
##
##for _ in range(m) :
##    a, b, weight = map(int, input().split())
##    if a not in islands:
##        islands[a] = [(weight, b)]
##    else :
##        islands[a].append((weight, b))
##
##    if b not in islands :
##        islands[b] = [(weight, a)]
##    else :
##        islands[b].append((weight, a))
##
##a, b = map(int, input().split())
##
##print(find (islands, a, b, 0))

# 9 -> 5 일때 내가 푼 풀이는 max값만 생각하기 때문에 최대중량 값이 5가
# 나와야하는데 9가 나오게 풀었음
# 여러가지 상황을 생각해야함


# 문제 풀이 핵심 아이디어
# 중량제한 : 십억 -> 값이 큼 -> 로그나 루트 방식 의심하기 !

# 중량제한을 찾고자함
# 이진탐색은 찾고자하는 그 값(중량제한)에 대해서 수행

# 이진 탐색 O(M * log C)
# 그래프의 탐색 방법중 BFS 사용 -> 간선의 개수만큼 반복 수행
# -> O(M)

from collections import deque

n , m = map(int, input().split())
adj = [[]for _ in range(n + 1)]

def bfs(c) :
    queue = deque([start_node])
    visited = [False] * (n + 1)
    visited[start_node] = True

    while queue :
        x = queue.popleft()
        for y, weight in adj[x] :
            if not visited[y] and weight >= c :
                visited[y] = True
                queue.append(y)
                
    return visited[end_node]
    

start = 1000000000
end = 1

for _ in range(m) :
    x, y, weight = map(int, input().split())
    adj[x].append((y, weight))
    adj[y].append((x, weight))

    start = min(start, weight) # for문 안에서 비교해야함
    end = max(end, weight)

start_node, end_node = map(int, input().split())

result = start # 두 섬을 연결하는 경로는 항상 존재하므로
while start <= end :
    mid = (start + end) //2
    if bfs (mid) :
        result = mid
        start = mid + 1
    else :
        end = mid - 1

print(result)

# 혼자

##n, m = map(int, input().split()) # 섬의개수, 경로수
##graph = [[] for _ in range(n + 1)]
##
##def bfs (mid) :
##    queue = [start_node]
##    visited = [False] * (n + 1)
##    visited[start_node] = True # 빼먹음
##
##    while queue :
##        x = queue.pop(0) # pop한건 x로 받기
##        for y, weight in graph[x] : # 인접한 섬 모두 받아오기
##            if not visited[y] and weight >= mid :
##                visited[y] = True
##                queue.append(y)
##
##    return visited[end_node]
##
##start = 1000000000 # start와 end를 반대로 설정해줘야 범위 좁힐 수 있음
##end = 1
##
##for _ in range(m) :
##    x, y, weight = map(int, input().split())
##    graph[x].append((y, weight))
##    graph[y].append((x, weight))
##
##    start = min(start, weight)
##    end = max(end, weight)
##
##start_node, end_node = map(int, input().split())
##result = start
##
##while start <= end :
##    mid = (start + end) // 2
##    if bfs(mid) : # 찾는게 bfs이므로 bfs 넣어주기
##        result = mid
##        start = mid + 1
##    else :
##        end = mid - 1
##
##print(result)

### 한번 더
##
##n, m = map(int, input().split())
##graph = [[] for _ in range(n + 1)]
##
##def bfs(c) :
##    queue = [a]
##    visited = [False] * (n + 1)
##    visited[a] = True
##
##    while queue :
##        x = queue.pop(0)
##        for y, weight in graph[x] :
##            if visited[y] == False and weight >= c :
##                # weight가 c보다 크거나 같아야함
##                visited[y] = True
##                queue.append(y)
##    return visited[b]
##
##start = 1000000000
##end = 1
##
##for _ in range(m) :
##    x, y, weight = map(int, input().split())
##    graph[x].append((y, weight))
##    graph[y].append((x, weight))
##    start = min(start, weight)
##    end = max (end, weight)
##
##result = start
##a, b = map(int, input().split())
##
##while start <= end :
##    mid = (start + end) // 2
##
##    if bfs(a) :
##        result = mid
##        start = mid + 1
##    else :
##        end = mid - 1
##
##print(result)
