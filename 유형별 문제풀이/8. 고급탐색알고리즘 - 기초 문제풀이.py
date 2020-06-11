# [1. 기초 문제풀이]

#1991번 - 트리 순회 [틀림]

# 문제 풀이 핵심 아이디어

# 기본적으로 재귀함수에 대해서 이해해야함
# 전위 순회 : 루트 -> 왼 -> 오
# 중위 순회 : 왼 -> 루트 -> 오 (왼쪽에 있는 것 부터 차례로 출력됨 !)
# 후위 순회 : 왼 -> 오 -> 루트

# tree를 데이터 개수가 적거나 간단하게 구현해야할 때 dict 사용 가능!

class Node :
    def __init__(self, data, left_node, right_node) :
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

def pre_order(node) :
    print(node.data, end='')
    if node.left_node != '.' :
        pre_order(tree[node.left_node])
    if node.right_node != '.' :
        pre_order(tree[node.right_node])

def in_order(node) :
    if node.left_node != '.' :
        in_order(tree[node.left_node])
    print(node.data, end='')
    if node.right_node != '.' :
        in_order(tree[node.right_node])

def post_order(node) :
    if node.left_node != '.' :
        post_order(tree[node.left_node])
    if node.right_node != '.' :
        post_order(tree[node.right_node])
    print(node.data, end='')

n = int(input())
tree=  {}
for i in range(n) :
    data, left_node, right_node = input().split()
    tree[data] = Node(data, left_node, right_node)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])

# 혼자

##class Node :
##    def __init__(self, data, left, right) :
##        self.data = data
##        self.left = left
##        self.right= right
##
##def pre_order(node) :
##    print(node.data, end='')
##    if node.left != '.' :
##        pre_order(tree[node.left])
##    if node.right != '.' :
##        pre_order(tree[node.right])
##
##def in_order(node) :
##    if node.left != '.' :
##        in_order(tree[node.left])
##    print(node.data, end='')
##    if node.right!= '.' :
##        in_order(tree[node.right])
##
##def post_order(node) :
##    if node.left != '.' :
##        post_order(tree[node.left])
##    if node.right != '.' :
##        post_order(tree[node.right])
##    print(node.data, end='')
##
##tree = {}
##
##n = int(input())
##for _ in range(n) :
##    data, left, right = input().split()
##    tree[data] = Node(data, left, right)
##
##pre_order(tree['A'])
##print()
##in_order(tree['A'])
##print()
##post_order(tree['A'])




# 2250번 - 트리의 높이와 너비 [틀림]

# 문제 풀이 핵심 아이디어
# 중위 순회를 이용하면 X축을 기준으로 왼쪽부터 방문한다!
# 중위 순회 알고리즘을 이용하고, 추가적으로 level 값을 저장하여 해결

class Node :
    def __init__(self, number, left_node, right_node) :
        self.parent = -1 # 노드 1번이 항상 루트가 되는 것이 아님
        self.number = number
        self.left_node = left_node
        self.right_node = right_node

def in_order(node, level) :
    global level_depth, x # level은 높이, x는 x축 값
    level_depth = max(level_depth, level)
    if node.left_node != -1 : # 왼쪽 노드 방문
        in_order(tree[node.left_node], level + 1)
        
    level_min[level] = min(level_min[level], x)
    # 해당 레벨에 대해서 x축이 가장 큰 값을 반복적으로 찾기
    level_max[level] = max(level_max[level], x)
    # 해당 레벨에 대해서 x축이 가장 큰 값을 반복적으로 찾기
    # 나중에 빼서 너비계산 할 것임
    x += 1
    
    if node.right_node != -1 : # 오른쪽 노드 방문
        in_order(tree[node.right_node], level + 1)


n = int(input()) # 노드의 개수 받아오기
tree = {} # 트리를 딕셔너리형으로 만들기
level_min = [n] # number가 1부터 시작하므로 0번째를 초기화
level_max = [0]
root = -1 # root 초기화
x = 1
level_depth = 1

for i in range(1, n + 1) : # n개의 노드와 각각의 최대최소값 초기화
    tree[i] = Node(i, -1, -1)
    level_min.append(n) # x축 최소값 초기화
    level_max.append(0) # x축 최대값 초기화

for _ in range(n) :
    number, left_node, right_node = map(int, input().split())
    tree[number].left_node = left_node
    tree[number].right_node = right_node
    if left_node != -1 :
        tree[left_node].parent = number # 부모 초기화
    if right_node != -1 :
        tree[right_node].parent = number

for i in range(1, n + 1) :
    if tree[i].parent == -1 : # 루트 노드인 경우
        root = i

in_order(tree[root], 1)

result_level = 1 # 결과 level 초기화
result_width = level_max[1] - level_min[1] + 1 # 결과 너비 초기화
for i in range(2, level_depth + 1) :
    width = level_max[i] - level_min[i] + 1
    if result_width < width :
        result_level = i
        result_width = width

print(result_level, result_width)

# 혼자

##class Node :
##    def __init__(self, number, left, right) :
##        self.parent = -1
##        self.number = number
##        self.left = left
##        self.right = right
##
##def in_order(node, level) :
##    global x, level_depth
##    level_depth = max(level, level_depth)
##    if node.left != -1 :
##        in_order(tree[node.left], level + 1)
##    level_max[level] = max(level_max[level], x)
##    level_min[level] = min(level_min[level], x)
##    x += 1
##    if node.right != -1 :
##        in_order(tree[node.right], level + 1)
##
##n = int(input())
##tree = {}
##level_max = [0]
##level_min = [n]
##root = -1
##x = 1
##level_depth = 1 # 최대 레벨 알기위해 존재
##
##for i in range(1, n + 1) :
##    tree[i] = Node(i, -1, -1)
##    level_max.append(0)
##    level_min.append(n)
##
##for _ in range(n) :
##    number, left, right = map(int, input().split())
##    tree[number].left = left
##    tree[number].right = right
##    if left != -1 :
##        tree[left].parent = number
##    if right != -1 :
##        tree[right].parent = number
##
##for i in range(1, n + 1) :
##    if tree[i].parent == -1 :
##        root = i
##
##in_order(tree[root], 1)
##
##result_level = 1
##result_width = level_max[1] - level_min[1] + 1
##
##for i in range(2, level_depth + 1) :
##    width = level_max[i] - level_min[i] + 1
##    if result_width < width :
##        result_level = i
##        result_width = width
##
##print(result_level, result_width)

### 한번 더
##
##class Node :
##    def __init__(self, number, left, right) :
##        self.parent = -1
##        self.number = number
##        self.left = left
##        self.right = right
##
##def in_order(node, level) :
##    global level_depth, x
##    level_depth = max(level, level_depth)
##
##    if node.left != -1 :
##        in_order(tree[node.left], level + 1)
##
##    level_max[level] = max(level_max[level], x)
##    level_min[level] = min(level_min[level], x)
##    x += 1
##
##    if node.right != -1 :
##        in_order(tree[node.right], level + 1)
##
##n = int(input())
##tree = {}
##level_max = [0] * (n + 1)
##level_min = [n] * (n + 1)
##root = -1
##level_depth = 1
##x = 1
##
##for i in range(n + 1) :
##    tree[i] = Node(i, -1, -1)
##
##for _ in range(n) :
##    number, left, right= map(int, input().split())
##    tree[number].left = left
##    tree[number].right= right
##    if left != -1 :
##        tree[left].parent = number
##    if right != -1 :
##        tree[right].parent = number
##
##for i in range(1, n + 1) :
##    if tree[i].parent == -1 :
##        root = i
##
##in_order(tree[root], 1)
##
##result_level = 1
##result_width = level_max[1] - level_min[1] + 1
##
##for i in range(2, level_depth + 1) :
##    width = level_max[i] - level_min[i] + 1
##    if result_width < width :
##        result_level = i
##        result_width = width
##
##print(result_level, result_width)
