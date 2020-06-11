# 3052. 나머지

rest_list = set()

for i in range(10) :
    num = int(input())
    rest = num % 42
    if rest not in rest_list :
        rest_list.add(rest)

print(len(rest_list))



# 2953. 나는 요리사다

score_list = []

for person in range(5) :
    score = list(map(int, input().split(' ')))
    score_list.append([sum(score), person + 1])

score_list.sort()
result = score_list.pop()
print(result[1], result[0])



# 1159. 농구 경기

alphabet = {
    'a' : 0,
    'b' : 0,
    'c' : 0,
    'd' : 0,
    'e' : 0,
    'f' : 0,
    'g' : 0,
    'h' : 0, 
    'i' : 0,
    'j' : 0,
    'k' : 0,
    'l' : 0,
    'm' : 0,
    'n' : 0,
    'o' : 0,
    'p' : 0,
    'q' : 0,
    'r' : 0,
    's' : 0,
    't' : 0,
    'u' : 0,
    'v' : 0,
    'w' : 0,
    'x' : 0,
    'y' : 0,
    'z' : 0
    
}
result = False
first_list = ''

num = int(input())
for i in range(num) :
    name = input()
    alphabet[name[0]] += 1

for first in alphabet.keys() :
    if alphabet[first] >= 5 :
        result = True
        first_list += first
        
if result == False :
    print('PREDAJA')
else :
    print(first_list)



# 5397. 키로거 [틀림]

###시간초과
##num = int(input())
##
##for i in range(num) :
##    cursor = 0
##    pw = []
##    
##    keyboard = input()
##
##    for char in keyboard :
##        if char == '<' :
##            if cursor > 0 :
##                cursor -= 1
##                
##        elif char == '>' :
##            if cursor < len(pw):
##                cursor += 1
##                
##        elif char == '-' :
##            if len(pw) > 0 :
##                pw = pw[: -1]
##
##        else :
##            if cursor == len(pw) :
##                pw.append(char)
##                cursor += 1
##            else :
##                back_pw = pw[cursor:]
##                pw = pw[:cursor]
##                pw.append(char)
##                pw.extend(back_pw)
##                cursor += 1
##
##    print(''.join(pw))


# input 보다 sys.stdin이 시간을 줄여준다

import sys
import collections

for i in range(int(sys.stdin.readline().replace('\n', ''))) :
    l = collections.deque()
    r = collections.deque()

    for c in sys.stdin.readline().replace('\n', '') :
        if c == '<' :
            if l :
                r.appendleft(l.pop())
        elif c == '>' :
            if r :
                l.append(r.popleft())
        elif c == '-' :
            if l :
                l.pop()
        else :
            l.append(c)
            
    l.extend(r)
    print(''.join(l))

# 한번 더
##import sys
##import collections
##
##num = int(sys.stdin.readline())
##
##for _ in range(num) :
##    left = collections.deque()
##    right = collections.deque()
##
##    for c in (sys.stdin.readline().replace('\n', '')) :
##        if c == '<' :
##            if left :
##                right.appendleft(left.pop())
##        elif c == '>' :
##            if right :
##                left.append(right.popleft())
##        elif c == '-' :
##            if left :
##                left.pop()
##        else :
##            left.append(c)
##
##    left.extend(right)
##    print(''.join(left))



# 2846. 오르막길 [틀림]

import sys
num = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(' ')))

pre = arr[0]
temp = [pre]
max_h = 0

for h in arr[1:] :
    if h > pre :
        temp.append(h)
        pre = h
    elif h <= pre :
        d_h = temp[-1] - temp[0]
        if d_h > max_h :
            max_h = d_h
        temp = [h]
        pre = h

if len(temp) >= 2 :
    d_h = temp[-1] - temp[0]
    if d_h > max_h :
        max_h = d_h

print(max_h)

# 1874. 스택 수열 [틀림]

# 문제풀이 핵심 아이디어
# 1.스택에 원소를 삽입할 때, 단순히 특정 수에 도달할 때까지 삽입
# 2. 스택에서 원소를 연달아 빼낼 때, 내림차순을 유지할 수 있는지 확인
# ** 1부터 n까지의 수였다....

import sys
num = int(sys.stdin.readline())

stack = []
result = []
count = 1

for i in range(num) :
    data = int(sys.stdin.readline())
    while count <= data : # while 주의
        stack.append(count)
        result.append('+')
        count +=1

    if data == stack[-1] :
        stack.pop()
        result.append('-')

    else :
        print ('NO')
        exit(0)

print('\n'.join(result))

# 1966. 프린터 큐

case = int(input())

for _ in range(case) :    
    n, m = map(int, input().split(' '))
    queue = list(map(int, input().split(' ')))
    queue = [(i, idx) for idx, i in enumerate(queue)]
    # enumerate : 인덱스 번호와 컬렉션의 원소를 튜플 형태로 반환

    count = 0
    while True :
        if queue[0][0] == max(queue, key = lambda x : x[0])[0] :
            count += 1
            if queue[0][1] == m :
                print (count)
                break
            else :
                queue.pop(0)
        else :
            queue.append(queue.pop(0))
##
# 참고
# sth = max(arr, key=lambda x: x[0])[0]
    # 2차원 배열에서 열의 첫번째 값이 가장 큰 원소를 찾고,
    # 그 값의 1번째 값 리턴
    # 예시 arr = [[1,2,3],[4,5,6],[7,8,9]]
    # sth = max(arr, key=lambda x: x[0])[0]
    # sth = 7

# 한번 더

##case = int(input())
##
##for _ in range(case) :
##    n , m = map(int, input().split(' '))
##    queue = list(map(int, input().split(' ')))
##    queue = [(i, idx) for idx, i in enumerate(queue)] # 순서바꿔줘야 max 사용가능
##
##    cnt = 0 # cnt for 문안에 넣어줘야 초기화됨
##    while True :
##        if queue[0][0] == max(queue, key = lambda x : x[0])[0] :
##            cnt += 1
##            if queue[0][1] == m :
##                print(cnt)
##                break
##            else :
##                queue.pop(0)
##        else :
##            queue.append(queue.pop(0))


# 5397. 키로거

from collections import deque # appendleft, popleft 사용하려면 deque import

num = int(input())

for _ in range(num) :
    pw = input()
    left = deque()
    right = deque()

    for data in pw :
        if data == '<' :
            if left:
                right.appendleft(left.pop())
        elif data == '>' :
            if right :
                left.append(right.popleft())
        elif data == '-' :
            if left :
                left.pop()
        else :
            left.append(data)

    print(''.join(left + right))

# 강의 방식

num = int(input())

for _ in range(num) :
    pw = input()
    left = []
    right = []

    for data in pw :
        if data == '<' :
            if left:
                right.append(left.pop())
        elif data == '>' :
            if right :
                left.append(right.pop())
        elif data == '-' :
            if left :
                left.pop()
        else :
            left.append(data)

    left.extend(reversed(right))
    print(''.join(left))
