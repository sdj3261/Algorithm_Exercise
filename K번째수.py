import sys
sys.stdin = open("input.txt", "rt")
T = int(input())
for t in range(T) :
    n,s,e,k = map(int,input().split())
    temp = []
    a = list(map(int,input().split())) # 한줄을 int형   리스트로 읽기
    a = a[s-1:e]
    a.sort()
    print("#%d %d" %(t+1, a[k-1])) # %d를 이용하여 출력

