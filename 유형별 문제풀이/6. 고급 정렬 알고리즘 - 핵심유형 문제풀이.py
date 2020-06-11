# 고급정렬 이용 -> 퀵, 병합, 힙

# 2751번 - 수 정렬하기 2

test_case = int(input())
num_list = []

for _ in range(test_case) :
    num_list.append(int(input()))

num_list.sort() # num_list = sorted(num_list)

for num in num_list :
    print(num)

# 강의 내용
# 데이터 최대 개수가 백만개이므로 시간복잡도 O(NlogN)정렬 알고리즘 이용해야함
# 병합정렬, 퀵정렬, 힙정렬 or 기본 정렬 라이브러리
# 메모리가 허용된다면 pypy3로 제출

# 파이썬은 1초에 이천만 연산 가능

# 병합 정렬 알고리즘
# 분할 정복
# 절반씩 합치면서 정렬하면 전체리스트가 정렬됨
# 시간복잡도 O(NlogN)

def merge_sort(arr) :
    if len(arr) <= 1 :
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = [] # 배열 새로 파야함/ 아니면 새로운 idx = 0 정의
    left_idx, right_idx = 0, 0
    
    while len(left) > left_idx and len(right) > right_idx :
        if left[left_idx] < right[right_idx] :
            result.append(left[left_idx])
            left_idx += 1
        else :
            result.append(right[right_idx])
            right_idx += 1

    while left_idx < len(left) :
            result.append(left[left_idx])
            left_idx += 1

    while right_idx < len(right) :
            result.append(right[right_idx])
            right_idx += 1
            
    return result # return 해줘야함

arr = []
test_case = int(input())

for _ in range(test_case) :
    arr.append(int(input()))

result = merge_sort(arr)

for num in result :
    print(num)




# 11004번 - K번째 수

n, k = map(int, input().split())

num_list = list(map(int, input().split()))

num_list.sort()
print(num_list[k - 1])

# 강의 내용
# 데이터의 개수가 최대 오백만개이므로 (1억개 연산)-> 시간복잡도 O(NlogN) 이용해야함
# 고급정렬 알고리즘(병합정렬, 퀵정렬, 힙정렬 등)을 이용하여 문제 해결가능 or 파이썬 기본정렬
# 시간적 이점을 위해 PyPy3 이용 !

def merge_sort(num_list) :
    if len(num_list) <= 1 :
        return num_list
    
    mid = len(num_list) // 2
    left = merge_sort(num_list[:mid])
    right = merge_sort(num_list[mid:])

    left_idx, right_idx = 0, 0
    result = []
    
    while left_idx < len(left) and right_idx < len(right) :
        if left[left_idx] < right[right_idx] :
            result.append(left[left_idx])
            left_idx += 1
        else :
            result.append(right[right_idx])
            right_idx += 1

    while left_idx < len(left) :
        result.append(left[left_idx])
        left_idx += 1

    while right_idx < len(right) :
        result.append(right[right_idx])
        right_idx += 1

    return result

n, k = map(int, input().split())
num_list = list(map(int, input().split()))

num_list = merge_sort(num_list)

print(num_list[k-1])


# 퀵소트 (퀵소트는 최악의경우 O(N²)이기 때문에 틀리는 것 같음)
# 병합정렬로 가자

##def quick_sort(num_list) :
##    if len(num_list) <= 1 :
##        return num_list
##    
##    pivot = num_list[0]
##    left = [item for item in num_list[1:] if item < pivot] # 틀림
##    right = [item for item in num_list[1:] if pivot < item]
##
##    return quick_sort(left) + [pivot] + quick_sort(right)
##
##n, k = map(int, input().split())
##num_list = list(map(int, input().split()))
##
##num_list = quick_sort(num_list)
##
##print(num_list[k-1])
