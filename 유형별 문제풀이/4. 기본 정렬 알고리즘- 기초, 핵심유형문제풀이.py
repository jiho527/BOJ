#[기초 문제 풀이]

# 2750 : 수 정렬하기

num_list = []
n = int(input())

for _ in range(n) :
    data = int(input())
    num_list.append(data)

num_list.sort()

for data in num_list :
    print(data)

#c.f. print('\n'.join(num_list)) 사용 불가/ join은 문자열만 사용가능

# 나는 파이썬에서 제공하는 기본 정렬 라이브러리 이용
# O(nlogn) 보장


# 강의에서 다룬 방식
# 1. 선택정렬 알고리즘 (O(n²)) [다시 해보기]

num_list = []

num = int(input())

for _ in range(num) :
    num_list.append(int(input()))

for i in range(num - 1) :
    min_idx = i
    for j in range(i + 1, num) :
        
        if num_list[min_idx] > num_list[j] :
            min_idx = j
    num_list[i], num_list[min_idx] = num_list[min_idx], num_list[i]

for data in num_list :
    print(data)

# selection sort는 여기서 더 개선할 수 없음
# 차곡차곡 정렬 가능한  bubble sort만 개선 가능



# 1427 : 소트 인사이드

num = input()
num_list = []

for data in num :
    num_list.append(int(data))

num_list.sort(reverse=True)

for data in num_list :
    print(data, end='')

# 강의 방식

arr = input()

for i in range(9, -1, -1) :
    for j in arr :
        if int(j) == i :
            print(j, end='')




#[핵심 유형 문제 풀이]

# 10814 : 나이순 정렬 [틀림]

# 파이썬의 기본 정렬 라이브러리 사용
# 나이가 동일한 경우, 먼저 입력된 이름 순서를 따르도록 key 속성을 설정해줘야함

# python 정렬 방법 두가지
# 1. list.sort()
# 2. sorted (list) -> 정렬된 결과 반환

# sort()와 sorted()의 차이
# sort()는 원본 리스트에 영향 o / sorted()는 영향 x -> 따라서 sort가 더 빠름
# 둘다 key값, reverse값 설정 가능

n = int(input())

arr = []

for _ in range(n) :
    input_data = input().split()
    arr.append((int(input_data[0]), input_data[1]))

arr = sorted(arr, key=lambda x : x[0])
# lambda : 한줄로 정의한  함수 /x : 입력, x[0] :출력
# key가 x[0]이므로 x[0]로 정렬 -> 나머지 원소들은 stable

for i in arr :
    print(i[0], i[1])


# 직접 풀어보기

##n = int(input())
##
##member = []
##
##for _ in range(n) :
##    data = input().split(' ')
##    member.append([int(data[0]), data[1]]) # 튜플로 저장해도 됨
##
##member = sorted(member, key = lambda x : x[0]) # sorted 함수 값을 저장해야함
##
##for data in member :
##    print(data[0], data[1])



# 11650번 - 좌표 정렬하기 [틀림]

# 파이썬의 기본 정렬 라이브러리는 기본적으로 튜플의 인덱스 순서대로
# 오름차순으로 정렬한다.

# 따라서 key 속성 설정 없이 단순히 기본 정렬 라이브러리를 사용하면 됨

n = int(input())

nums = []

for _ in range(n) :
    x, y = map(int, input().split())
    nums.append((x, y))

nums.sort()

for i in nums :
    print(i[0], i[1])



# 10989번 - 수 정렬하기 3 [모름] 

# 파이썬은 1초에 대략 이천만 개의 연산 가능
# 파이썬 기본 정렬 알고리즘은 O(nlogn) 이고,
# 입력 N이 천만까지 가능하기때문에 해당 문제를 시간내에 풀 수 없음

# 데이터의 수는 많지만 데이터는 만보다 작은 수로, 데이터의 범위는 좁다
# -> 이럴 때 사용할 수 있는 정렬 알고리즘 : 계수 정렬 알고리즘

# 계수 정렬 알고리즘이란 (Counting Sort) ?
# 수의 범위가 제한적일 때만 사용할 수 있지만 훨씬 빠르다. O(N)

# 배열의 인덱스를 특정한 데이터의 값으로 여기는 정렬 방법
# 배열의 크기는 데이터의 범위를 포함할 수 있도록 설정
# 데이터가 등장한 횟수를 센다.
# e.g. [3,3,7] -> 인덱스 3에 2, 인덱스 7에 1

# 유의사항
# 데이터의 개수가 많을 때 파이썬에서는 sys.stdin.readline()을 사용해라
# pypy3는 메모리를 더 먹고 시간을 빠르게 하는데 이 문제 메모리제한이 8MB라서
# pypy3 말고 python3로 제출

import sys

n = int(sys.stdin.readline())

arr = [0] * 10001

for _ in range(n) :
    num = int(sys.stdin.readline())
    arr[num] += 1

for i in range(10001):
    if arr[i] != 0 : # arr[i] > 0로 해도 됨
        for _ in range(arr[i]) :
            print(i)
