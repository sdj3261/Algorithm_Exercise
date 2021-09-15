import sys
from collections import deque
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = []
stack.append(0)
okunsu = [-1 for _ in range(N)]

for i in range(1,N) :
    print(stack)
    while stack and arr[stack[-1]] < arr[i] :
        okunsu[stack.pop()] = arr[i]
    stack.append(i)
print(*okunsu)


