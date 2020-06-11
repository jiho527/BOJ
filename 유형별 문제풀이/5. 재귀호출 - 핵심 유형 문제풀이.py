# 2747번 - 피보나치 수

# 시간 초과
##import sys
##
##def fibo (n) :
##    if n == 0 :
##        return 0
##    elif n == 1 :
##        return 1
##    
##    return fibo(n-1) + fibo(n-2)
##
##n = int(sys.stdin.readline())
##print(fibo(n))

# 맞음
arr = []
arr.append(0)
arr.append(1)

n = int(input())

for i in range(2, n + 1) :
    arr.append(arr[i-1] + arr[i-2])

print(arr[n])


# 강의 내용 >
# 점화식 -> 재귀함수로 구현 가능
# 하지만 피보나치 수열은 재귀적 구현의 한계를 보여준다.
# -> 동일한 계산이 반복적으로 호출 되기 때문
# 따라서 O(2ⁿ) 이므로 n이 30만 돼도 십억개의 연산이다.
# 여기서 최대 n이 45까지 이므로 연산의 수가 너무크다 !

# -> 재귀함수가 아닌 반복문으로 문제를 풀자

n = int(input())

a, b = 0, 1

while n > 0 :
    a, b = b, a + b
    n -= 1

print (a)


# 한번 더
##n = int(input())
##a, b = 0, 1
##
##while n > 0 :
##    a, b = b, a + b
##    n -= 1
##
##print(a)



#1074번 - Z [모름]

# Z모양을 구성하는 4가지 방향에 대하여 차례대로 재귀적으로 호출

def solve (n, x, y) :
    global result # global 변수 : 전역 변수
    if n == 2 :
        if x == X and y == Y :
            print(result)
            return
        result += 1
        if x == X and y + 1 == Y :
            print(result)
            return
        result += 1
        if x == X + 1 and y == Y :
            print(result)
            return
        result += 1
        if x + 1 == X and y + 1 == Y :
            print(result)
            return
        result += 1
        return

    solve (n / 2, x, y)
    solve (n / 2, x, y + n/2)
    solve (n / 2, x + n/2, y)
    solve (n / 2, x + n/2, y + n/2)

result = 0
N, X, Y = map(int, input().split(' '))
solve(2 ** N, 0, 0)

def zvisit (n, x, y) :
    global result
    if n == 2 :
        if x == X and y == Y :
            print(result)
            return
        result += 1
        if x == X and y + 1 == Y :
            print(result)
            return
        result +=1
        if x + 1 == X and y == Y :
            print(result)
            return
        result += 1
        if x + 1 == X and y + 1 == Y :
            print(result)
            return
        result += 1
        return

    zvisit(n/2, x, y)
    zvisit(n/2, x, y + n/2)
    zvisit(n/2, x + n/2, y)
    zvisit(n/2, x + n/2, y + n/2)
        
result = 0
N, X, Y = map(int, input().split(' '))
zvisit(2 ** N, 0, 0)




# 7490번 - 0 만들기 [틀림]

# 문제 풀이 핵심 아이디어
# 1. 자연수 N의 범위가 매우 한정적이므로 완전탐색으로 문제 해결 가능
# 2. 수의 리스트와 연산자 리스트를 분리하여 모든 경우의 수 계산

# 연산자 리스트 : '+', '-', ' ' -> 사이사이에 들어가므로 경우의수는 3^(n-1)
# N이 최대 9이므로 모든 경우의 수를 곱해도 삼만개 연산보다 적은 연산 수

# 리스트를 재귀적으로 호출 -> 리스트에 내용을 추가
# 파이썬의 eval()함수를 이용해서 문자열 형태의 표현식을 계산
# (e.g. '2*3' = 6)

# 모든 경우의 수를 계산할 때도, 재귀함수가 이용될 수 있다 !

import copy

def recursive (array, n) :
    if len(array) == n - 1:
        operators_list.append(copy.deepcopy(array))
        return
    
    array.append(' ')
    recursive (array, n)
    array.pop()

    array.append('+')
    recursive (array, n)
    array.pop()

    array.append('-')
    recursive (array, n)
    array.pop()
        

test_case = int(input())
for _ in range(test_case) :
    operators_list = []
    n = int(input())
    recursive ([], n)

    integers = [i for i in range(1, n + 1)]

    for operators in operators_list :
        string = "" # string 초기화
        for i in range(n - 1) :
            string += str(integers[i]) + operators[i]
        string += str(integers[-1])
        if eval(string.replace(' ', '')) == 0 :
            print(string)
    print()


### 직접
##
##import copy
##
##def recursive (arr, n) :
##    if len(arr) == n - 1 :
##        operators_list.append(copy.deepcopy(arr)) # 깊은 복사
##        return
##
##    arr.append(' ')
##    recursive(arr, n)
##    arr.pop()
##
##    arr.append('+')
##    recursive(arr, n)
##    arr.pop()
##
##    arr.append('-')
##    recursive(arr, n)
##    arr.pop()
##
##test_case = int(input())
##
##for _ in range(test_case) :
##    n = int(input())
##    operators_list = []
##
##    recursive([], n) # operators_list 넘겨주는게 아니라 빈 arr 넘김
##
##    integers = [i for i in range(1, n + 1)]
##
##    for operators in operators_list :
##        string = ""
##        for i in range(n - 1) :
##            string += str(integers[i]) + operators[i]
##        string += str(integers[-1])
##        if eval(string.replace(' ', '')) == 0 :
##            print(string)
##    print() # 테스트 케이스 별로 구별
