import sys
#sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
lists = []
for i in range(1,n+1) :
    for j in range(1,m+1) :
        lists.append(i+j)

count = {}

for i in lists :
    try: count[i] += 1
    except: count[i] = 1

sort_reverse_value = sorted(count.items(),reverse=True,key=lambda item: item[1])
for items in sort_reverse_value :
    if items[1] == max(count.values()) :
        print(items[0], end =' ')

#올림 ceil 내림 floor 0에가까운 내림 trunc
#round함수의 두번째 인자를 통해 소수 x번째자리에서 반올림 가능 기본은 1