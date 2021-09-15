import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
a = list(map(int, input().split()))
ave = round(sum(a)/n)
avmin = float('inf')

for index, value in enumerate(a) :
    index+= 1
    if abs(value - ave) < avmin :
        avmin = abs(value - ave)
        score = value
        res = index + 1
    elif abs(value - ave) == avmin :
        if value > score :
            score = value
            res = index + 1
print(ave, res)


#올림 ceil 내림 floor 0에가까운 내림 trunc
#round함수의 두번째 인자를 통해 소수 x번째자리에서 반올림 가능 기본은 1