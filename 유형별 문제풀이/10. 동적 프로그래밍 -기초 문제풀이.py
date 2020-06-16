# 동적프로그래밍 대표유형 확실히 파악하기

# 1904번 - 01타일 [틀림] 
# 난이도 하 / 동적 프로그래밍 / 20분

# 내 풀이 [런타임 에러]
##def solve(n) :
##    if n == 1 :
##        return n
##    if n == 2 :
##        return n
##
##    return solve(n - 1) + solve(n - 2)
##
##n = int(input())
##
##print(solve(n))

# 내풀이 2 [메모리 초과]
##n = int(input())
##
##arr = [0]
##arr.append(1)
##arr.append(2)
##
##for i in range(3, n + 1) :
##    arr.append(arr[i - 1] + arr[i - 2])
##
##print(arr[n] % 15746)


# 강의
# 동적 프로그래밍은 한번 구한 값을 나중에 다시 구하지 않는다. (Memoization)
# 동적 프로그래밍 문제를 풀기 위해서는 점화식(인접한 항들 사이의 관계식)을 세워야함

# 길이가 i 인 수열을 형성하는 방법
# [i-1] + 1 / [i - 2] + 00
# 따라서 D[i] = 수열의 길이가 i일때의 경우의 수라고 하면,
# D[i] = D[i-1] + D[i-2]

# 따라서 이는 피보나치수열과 동일

n = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1) :
    dp[i] = (dp[i-2] + dp[i-1]) %15746 # 엄청 큰 값에 대해 대비

print(dp[n])

# 동적프로그래밍은 점화식을 잘 세우고 문제가 원하는 게 무엇인지 파악하는 지가 중요!




# 12865번 - 평범한 배낭 [틀림]
# 난이도 하/ 동적 프로그래밍 / 30분
# 가장 많이 나오는 예제 !! 꼭 기억 !! 반복 !!

# 강의
# 핵심 아이디어 : 모든 무게에 대하여 최대 가치를 저장
# 시간복잡도 O(NK) <- 행이 N개 열이 K개인 테이블

n, k = map(int, input().split())

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1) :
    weight, value = map(int, input().split())
    for j in range(1, k + 1) :
        if j < weight :
            dp[i][j] = dp[i - 1][j]
        else :
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

print(dp[n][k])

# 한번 더

##n, k = map(int, input().split())
##
##dp = [[0] * (k+1) for _ in range(n + 1)]
##
##for i in range(1, n + 1) :
##    weight, value = map(int, input().split())
##    for j in range(1, k + 1) :
##        if j < weight :
##            dp[i][j] = dp[i-1][j]
##        else :
##            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
##
##print(dp[n][k])





# 11053번 - 가장 긴 증가하는 부분 수열
# 난이도 하/ 동적프로그래밍, LIS, 30분

# 내 풀이 [틀림]
##result = []
##
##n = int(input())
##arr = list(map(int, input().split(' ')))
##
##for i in range(n) :
##    current = arr[i]
##    cnt = 1
##    for j in range(i + 1, n) :
##        if current < arr[j] :
##            cnt += 1
##            current = arr[j]
##    result.append(cnt)
##
##result.sort()
##print(result[-1])

# 반례 : 4 \n 1 4 2 3
# 가장 증가하는 부분 수열은 1 2 3으로 3이 될 수도 있는 건데
# 내가 짠 코드는 4보다 2가 작으니까 세어지지않는다.

# 강의
# 가장 긴 증가하는 부분수열 (LIS) -> 전형적인 동적 프로그래밍 문제
# 수열의 크기가 N일때 시간복잡도는 O(N²)

# 각각의 원소를 마지막 원소로 가지는 부분수열의 최대 길이이다!
# 테이블의 열은 입력된 수열
# 테이블의 행은 열의 원소를 마지막으로 할 때, 부분수열의 최대 길이

n = int(input())
array = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n) :
    for j in range(0, i) :
        if array[j] < array[i] :
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
