import sys
#sys.stdin = open("input.txt", "rt")
lists = [i for i in range(1,21)]
stack = []

for i in range(10) :
    n, m = map(int, input().split())
    for j in range((m-n+1) // 2) :
        lists[(n-1)+j], lists[(m-1)-j] = lists[(m-1)-j] , lists[(n-1) + j]

print(*lists)

