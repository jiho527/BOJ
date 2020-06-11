# 10930 : SHA-256

import hashlib

data = input()
result = hashlib.sha256(data.encode())
print(result.hexdigest()) # hexdigest()로 해시결과 문자열을 반환

## 한번 더
##import hashlib
##data = input()
##result = hashlib.sha256(data.encode())
##print(result.hexdigest())



# 1920 : 수 찾기

num1 = int(input())
list1 = list(map(int, input().split(' ')))
num2 = int(input())
list2 = list(map(int, input().split(' ')))

for data in list2 :
    if data in list1 :
        print(1)
    else :
        print(0)

# 강의에서 다룬 방식 : set -> 중복 x
# 해쉬로도 풀 수 있음, 여기서 해쉬는 딕셔너리로 구현 가능

n = int(input())
arr = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

for i in x :
    if i not in arr :
        print(0)
    else :
        print(1)



# 4195 : 친구 네트워크 [틀림] [ㅠㅠㅠㅠㅠㅠㅠ]

# 문제풀이 핵심 아이디어
# 1. 해시를 활용한 Union-Find 알고리즘 (합집합 찾기)
# 2. Python에서는 dictionary 자료형을 해시처럼 사용 가능

# 합집합 찾기(Union-Find) 알고리즘 (Kruskal 알고리즘에서 사용됨)
# : 원소들의 연결 여부를 확인하는 알고리즘

# 부모테이블을 만들어서 1 -> 4 연결되었다고 가정하면,
# 더 작은 원소를 부모로 삼고, 부모테이블을 이용하여 집합을 구별할 수 있다

def find(x) :
    if x == parent[x] :
        return x
    else :
        x = parent[x] # 시간초과
        return find(x) # 재귀함수는 스택처럼 쌓이므로 return 해줘야함

def union (x, y) :
    x = find(x)
    y = find(y)
    
    if x != y :
        parent[y] = x
        number[x] += number[y]

test_case = int(input())

for _ in range(test_case) :
    parent = dict()
    number = dict()
    
    n = int(input())
    
    for i in range(n) :
        x, y = input().split()

        if x not in parent :
            parent[x] = x
            number[x] = 1
        if y not in parent :
            parent[y] = y
            number[y] = 1

        
        union (x, y)
        print(number[find(x)])
        
# 한번 더

##import sys
##
##def find (x) :
##    if x == parent[x] :
##        return x
##    else :
##        p = find(parent[x])
##        parent[x] = p # 안해주면 시간초과남 # root 값을 parent로 지정
##        return p
##
##def union (x, y) :
##    x = find(x)
##    y = find(y)
##    
##    if x != y :
##        parent[y] = x
##        number[x] += number[y]
##
##test_case = int(sys.stdin.readline())
##
##for _ in range(test_case) :
##    parent = {}
##    number = {}
##    
##    n = int(sys.stdin.readline())
##
##    for i in range(n) :
##        x, y = sys.stdin.readline().split()
##
##        if x not in parent :
##            parent[x] = x
##            number[x] = 1
##        if y not in parent :
##            parent[y] = y
##            number[y] = 1
##
##        union (x, y)
##        print(number[find(x)])
