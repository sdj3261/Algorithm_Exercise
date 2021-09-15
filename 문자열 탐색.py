import sys
#sys.stdin = open("input.txt", "rt")
def DFS(n) :
    if n == 0 :
        return
    else :
        DFS(n // 2)
        print(n % 2, end=' ')

n = int(input())
DFS(n)


