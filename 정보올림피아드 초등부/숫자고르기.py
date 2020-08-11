# 사이클이 발생할 때 까지 DFS로 찾기

# 다른 풀이
n = int(input()) # N 입력
dic = {}
for i in range(n):
    dic[i+1] = int(input()) # 첫째 줄 정수에 다음 줄 정수 입력

while True: # 다음을 반복
    baseSet = set(dic.values()) # 다음 줄 정수의 집합
    dic = {key:value for key, value in dic.items() if key in baseSet} # 다음 줄 정수가 첫째 줄 정수를 가리키는 경우
    if baseSet == set(dic.values()): # 다음 줄 정수의 집합과 dic의 value의 집합이 같을 때
        break
print(len(dic))
for key in dic.keys():
    print(key)