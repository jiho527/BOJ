# 음계
# 난이도 하/ 배열, 구현
# 15분 (최대 30분)

ascending = True # False로 하면 안됨
descending = True

data_list = list(map(int, input().split(' ')))
            
for i in range(len(data_list) - 1) :
    if data_list[i] < data_list[i+1] :
        descending = False
    else :
        ascending = False
        
if ascending :
    print('ascending')
elif descending :
    print('descending')
else :
    print('mixed')


# 블랙잭
# 난이도 하/ 배열, 완전탐색
# 20

n, m = list (map(int , input().split(' ')))
card_list = list(map(int, input().split(' ')))

result = 0

for i in range(n) :
    for j in range(i + 1, n) :
        for k in range(j + 1, n) :
            sum = card_list[i] + card_list[j] + card_list[k]
            if sum <= m :
                result = max(result, sum)

print (result)


### 음계 한번 더
##ascending = True
##descending = True
##
##data = list(map(int, input().split(' ')))
##
##for i in range(len(data) - 1) :
##    if data[i] < data[i + 1] :
##        descending = False
##    elif data[i] > data[i + 1] :
##        ascending = False
##
##if ascending :
##    print('ascending')
##elif descending :
##    print('descending')
##else :
##    print('mixed')


### 블랙잭 한번 더
##n, m = list(map(int, input().split(' ')))
##data = list(map(int, input().split(' ')))
##
##result = 0
##
##for i in range(n - 2) :
##    for j in range(i + 1, n - 1) :
##        for k in range(j + 1, n) :
##            sum = data[i] + data[j] + data[k]
##            if sum <= m :
##                result = max (result, sum)
##
##print(result)
