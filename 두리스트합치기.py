import sys
#sys.stdin = open("input.txt", "rt")
n,m = map(int,input().split())
list1 = list(map(int,input().split()))
cnt = 0
sumlist = []
for i in range(n) :
    sum = 0
    sumlist = []
    for j in range(i,n) :
        sum += list1[j]
        sumlist.append(list1[j])
        if sum == m :
            cnt += 1
            sum = 0
            sumlist = []
            break
print(cnt)
