from typing import List
import sys
#sys.stdin = open("input.txt", "rt")

def sum_nums(N: int, M: int) -> int:
    num_list = list(map(int, input().split()))
    sum = num_list[0]
    count = 0
    left = 0
    right = 1
    while True:
        if sum < M :
            if right < N :
                sum += num_list[right]
                right += 1
            else :
                break
        elif sum == M :
            count += 1
            sum -= num_list[left]
            left += 1
        else :
            sum -= num_list[left]
            left += 1
        print(sum)
    return count


print(sum_nums(8, 3))
