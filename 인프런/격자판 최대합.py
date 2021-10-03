from typing import List
import sys
sys.stdin = open("input.txt", "rt")
sums = []
arr = []
column = []
degak = []
degak2 = []


# sums.append(sum(map(int, input().split())))
def solution(N: int) -> int:
    # 행
    for i in range(N):
        arr.append(list(map(int, input().split())))
        sums.append(sum(arr[i]))
    # 열
    for j in range(N):
        column.append([])
        for k in range(N):
            column[j].append((arr[k][j]))
        sums.append(sum(column[j]))
    # 대각선
    for i in range(N):
        degak.append(arr[i][i])
        degak2.append(arr[(N-1)-i][i])
    sums.append(sum(degak))
    sums.append(sum(degak2))

    return max(sums)


print(solution(int(input())))
