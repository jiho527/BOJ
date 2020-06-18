# 9251번 - LCS
# Longest Common Subsequence : 최장 공통 부분수열
# 난이도 하/ 동적프로그래밍, LCS, 30
# 많이 언급되는 문제임

# 내 풀이 [틀림]
##a = input()
##b = input()
##
##dp = [[0] * len(a) for _ in range(len(b))]
##
##for i in range(len(b)) :
##    for j in range(len(a)) :
##        if b[i] == a[j] :
##            dp[i][j] = 1
##            for k in range(i) :
##                dp[i][j] = max(dp[i][j], dp[i][k] + 1)
##
##print(max(max(dp)))

# 강의
# 두 수열의 길이가 N 미만일 때, 시간복잡도 O(N²)으로 해결 가능

# 값이 같을때는 대각선에 + 1
# 값이 다를때는 위와 왼쪽을 비교해서 더 큰 값을 넣어주기

a = input()
b = input()

dp = [[0] * (len(a) + 1) for _ in range(len(b) + 1)]

for i in range(1, len(b) + 1) :
    for j in range(1, len(a) + 1) :
        if b[i - 1] == a[j - 1] :
            dp[i][j] = dp[i-1][j-1] + 1 # 대각선 + 1
        else :
            dp[i][j] = max(dp[i][j-1], dp[i-1][j]) # 왼쪽, 위쪽 중 큰 것

print(dp[len(b)][len(a)])




# 1495번 - 기타리스트
# 난이도 중/ 동적 프로그래밍/ 40분

# 강의
# 차례대로 곡을 연주한다는 점에서, 동적 프로그래밍으로 해결할 수 있는 문제임
# 곡의 개수가 N, 볼륨의 최대값은 M
# 동적 프로그래밍을 이용하여 시간복잡도 O(NM)으로 해결 가능

# 핵심 아이디어 : 모든 볼륨에 대해서 연주 가능 여부를 계산하기
# D[i][j + 1] = i번째 노래일 때 j크기의 볼륨으로 연주 가능한지 여부
# -> 노래를 순서대로 확인하며, 매 번 모든 크기의 볼륨에 대하여 검사

n, s, m = map(int, input().split())
arr = list(map(int, input().split()))

dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][s] = 1

for i in range(1, n + 1) :
    for j in range(m + 1) :
        if dp[i-1][j] == 0 :
            continue
        if j - arr[i - 1] >= 0 :
            dp[i][j - arr[i - 1]] = 1
        if j + arr[i - 1] <= m :
            dp[i][j + arr[i - 1]] = 1

result = -1
for i in range(m, -1, -1) :
    if dp[n][i] == 1 :
        result = i
        break

print(result)





# 2655번 - 가장높은탑쌓기
# 난이도 상/ 동적프로그래밍, LIS/ 50분

# 강의
# 가장 긴 증가하는 부분수열 (LIS)의 심화 변형 문제
# 벽돌의 개수가 N개일 때, 시간 복잡도 O(N²)으로 해결 가능
# 벽돌의 번호를 출력해야하므로, 계산된 테이블을 역추적 해야함

# 가장 먼저 벽돌을 무게기준으로 정렬
# D[i] = 인덱스가 i인 벽돌을 가장 아래에 두었을 때의 최대 높이
# 각 벽돌에 대해서 확인하며 D[i]를 갱신

n = int(input())

array = []
array.append((0,0,0,0))

for i in range(n) :
    area, height, weight = map(int, input().split())
    array.append((i+1, area, height, weight))

array.sort(key = lambda x : x[3])

dp = [0] * (n + 1)

for i in range(1, n + 1) :
    for j in range(0, i) :
        if array[i][1] > array[j][1] :
            dp[i] = max(dp[i], dp[j] + array[i][2])

max_value = max(dp)
result = []
index = n

while index > 0 :
    if dp[index] == max_value :
        result.append(array[index][0])
        max_value -= array[index][2]
    index -= 1

result.reverse()
print(len(result))
[print(i) for i in result]




# 강의 말고 동적프로그래밍 문제
# 1463번 - 1로 만들기 [틀림]

n = int(input())

dp = [-1] * (n + 1)

for i in range(1, n + 1) :
    dp[i]  = dp[i - 1] + 1
    if i % 2 == 0 :
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0 :
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])
