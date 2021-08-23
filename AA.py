import sys
sys.stdin = open("input.txt", "rt")
T = int(input())
for t in range(T) :
    n,s,e,k = map(int,input().split())
    temp = []
    a = list(map(int,input().split())) # 한줄로 리스트로 읽기
    a = a[s-1:e]
    a.sort()
    print(a[k-1])

