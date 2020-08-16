# 1679 - 숨바꼭질

# 1. 문제 이해
# 수빈 : n, 동생 : k (0 <= n, k <= 100000)
# 수빈 x : 걷거나(x+1, x-1), 순간이동(2*x) (x좌표로만 이동)
# 입력 : n, k
# 출력 : 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇초 후인지 구하기

# 2. 풀이 계획 및 검증
# 예제 n = 5, k = 17에서 n이 될 수 있는 경우는 {4, 6, 10} 이고
# 집합안의 각 숫자들이 될 수 있는 경우의 수도 각각 +1, -1, *2 로 세가지씩
# 있으므로 이는 트리로 그릴 수 있고, 그래프 탐색을 생각해볼 수 있다.
# 따라서 BFS로 최단 시간을 구해보자 -> O(V+E) = O(100000 + 3*100000)

# 3. 구현
from _collections import deque


def bfs() :
    while q :
        v, cnt = q.popleft()
        if v == k :
            return cnt

        # dx = [v-1, v+1, v*2] # 코드 길이 한 줄 개선
        for i in [v-1, v+1, v*2] :
            if 0 <= i < MAX and not(visited[i]) :
            # 큰 수에서 작아질 수 있으므로 i가 k보다 작은 것에서 수정함
                q.append((i, cnt+1))
                visited[i] = True


n, k = map(int, input().split())
MAX = 100001
visited = [False] * MAX # 갈 수 있는 모든 경우의 수 check
visited[n] = True
q = deque()
q.append((n, 0))

print(bfs())

# 4. 검토 및 개선
# 예제 답은 맞는데 런타임 에러남
# 다른 코드 찾아본 결과, 0 <= n, k <= 100000인데 10000으로 해서 틀렸음
# 상수 MAX로 설정하면 덜 헷갈릴듯
# 그리고 bfs 함수에서 갈 수 있는 경우의 수를 큐에 넣을때
# i가 k보다 작을때로 설정했는데, k보다 큰 수에서 k로 오는 경우도 있으므로
# 모든 경우의 수 100001로 제한해야한다.

# 다른 풀이
# visited 배열과 cnt를 합친, 시간을 저장하는 배열을 만들어서 푸는 방법

from collections import deque

n, k = map(int, input().split())
MAX = 100001
arr = [0] * 100001 # 0이상이면 방문 여부 + 시간 저장

def bfs() :
    q = deque([n])
    while q :
        current_pos = q.popleft()

        if current_pos == k :
            return arr[current_pos]

        for next_pos in (current_pos-1, current_pos+1, current_pos*2) :
            if 0 <= next_pos < MAX and not(arr[next_pos]) :
                q.append(next_pos)
                arr[next_pos] = arr[current_pos] + 1

print(bfs())