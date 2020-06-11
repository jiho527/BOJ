# 1927번 - 최소 힙 [틀림]

# 내 풀이 [시간초과]
##import heapq
##
##test_case = int(input())
##arr = []
##
##for _ in range(test_case) :
##    n = int(input())
##
##    if n > 0 :
##        heapq.heappush(arr, n)
##    elif n == 0 :
##        if len(arr) == 0 :
##            print(0)
##        else :
##            print(heapq.heappop(arr))

# 한번에 몰아서 출력하는 걸로 바꿨더니 맞음

### 강의
### 최소 힙의 기본적인 기능 구현
### 파이썬의 heapq 라이브러리 이용
##
import heapq

n = int(input())
heap = []
result = []

for _ in range(n) :
    data = int(input())
    if data == 0 :
        if heap : # len함수 쓰지않음
            result.append(heapq.heappop(heap))
        else :
            result.append(0)
    else :
        heapq.heappush(heap, data)

for data in result : # 한번에 몰아서 출력
    print(data)




#1715번 - 카드 정렬하기 [틀림]
# 난이도 : 하
# 유형 : 힙, 자료구조, 그리디

# 내 풀이 [틀림]

##test_case = int(input())
##arr = []
##
##for _ in range(test_case) :
##    arr.append(int(input()))
##
##arr.sort()
##
##total = 0
##sum = arr[0]
##
##for i in range(1, test_case) :
##    sum += arr[i]
##    total += sum
##    
##print(total)

##import heapq
##test_case = int(input())
##heap = []
##
##for _ in range(test_case) :
##    data = int(input())
##    heapq.heappush(heap, data)
##
##sum = heapq.heappop(heap)
##total = 0
##
##while heap :
##    sum += heapq.heappop(heap)
##    total += sum
##
##print(total)

# 숫자를 작은 순서대로 차례대로 더하는 것이 아니라, 
# 결과값이 가장 작은 순서대로 더하는 것이다.
# 따라서, 배열이 아니라 힙으로 구현해서 가장 작은 두개를 빼서 더하고
# 다시 힙에 넣어줘야한다.

# 강의
# 가장 크기가 작은 숫자 카드 묶음들을 먼저 합쳤을 때 비교 횟수가 가장 적다.

import heapq

n = int(input())
heap = []

for i in range(n) :
    data = int(input())
    heapq.heappush(heap, data)

result = 0

while len(heap) != 1 :
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)

# 한번 더

##import heapq
##
##heap = []
##total = 0
##test_case = int(input())
##
##for _ in range(test_case) :
##    data = int(input())
##    heapq.heappush(heap, data)
##
##while len(heap) != 1 :
##    first = heapq.heappop(heap)
##    second = heapq.heappop(heap)
##    sum_value = first + second
##    total += sum_value
##    heapq.heappush(heap, sum_value)
##
##print(total)




# 1766번 - 문제집 [틀림]
# 난이도 중
# 문제 유형 : 힙, 위상 정렬

# 강의
# 전형적인 위상정렬 문제
# 순서가 정해져 있는 작업을 차례로 수행해야 할 때, 순서를 결정해주는 알고리즘
# 위상정렬의 시간복잡도 : O(V + E)

# 위상정렬(Topology Sort) 알고리즘
# 1. 진입차수(자기자신으로 들어오는 간선)가 0인 정점을 큐에 삽입
# 2. 큐에서 원소를 꺼내서 해당 원소와 간선 제거 (우선순위 큐 = 힙)
# 3. 제거 이후에 다시 진입차수가 0이 된 정점을 큐에 삽입
# 4. 큐가 빌때까지 2-3 과정을 반복

# 모든 원소를 방문하기전에 큐가 빈다면 사이클이 존재한다는 것
# 위상정렬은 사이클이 존재하면 안됨 (1->3 ,3->1 이라면 끝나지 않기때문)

# 모든 원소를 방문했다면 큐에서 꺼낸 순서가 위상정렬의 결과

import heapq

n, m = map(int, input().split())
array = [[] for i in range(n + 1)]
indegree = [0] * (n + 1)

heap = []
result = []

for _ in range(m) :
    x, y = map(int, input().split())
    array[x].append(y)
    indegree[y] += 1

for i in range(1, n + 1) : # 진입차수가 0인 정점을 큐에 삽입
    if indegree[i] == 0 :
        heapq.heappush(heap, i)

result = []

while heap : # 큐에서 원소를 꺼내서 해당 원소와 간선 제거
    data = heapq.heappop(heap)
    result.append(data)
    for y in array[data] :
        indegree[y] -= 1
        if indegree[y] == 0:
            heapq.heappush(heap, y)

for i in result :
    print(i, end=' ')

### 한번 더
##import heapq
##
##n, m = map(int, input().split())
##
##array = [[] for i in range(n + 1)]
##indegree = [0] * (n + 1)
##
##heap = []
##result = []
##
##for _ in range(m) :
##    x, y = map(int, input().split())
##    array[x].append(y)
##    indegree[y] += 1
##
##for i in range(1, n + 1) :
##    if indegree[i] == 0 :
##        heapq.heappush(heap, i)
##
##while heap :
##    data = heapq.heappop(heap)
##    result.append(data)
##
##    for num in array[data] :
##        indegree[num] -= 1
##        if indegree[num] == 0 :
##            heapq.heappush(heap, num)
##
##for data in result :
##    print(data, end=' ')
