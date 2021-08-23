import sys
sys.stdin = open("input.txt", "rt")
n, k = map(int,input().split())
list1 = list(map(int,input().split()))
set1 = set()

for i in range(n) :
    for j in range(i+1, n) :
        for m in range(j+1, n) :
            set1.add(list1[i] + list1[j] + list1[m])
set_list = list(set1)
set_list.sort(reverse=True)
print(set_list[k-1])



