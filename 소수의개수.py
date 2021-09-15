import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
def reverse(x) :
    res = 0
    while x > 0 :
        remainder = x % 10
        res = res * 10 + remainder
        x = x // 10
    return res

    return remainder
def isPrime(x) :
    if x == 1 :
        return False
    for i in range(2,x//2 + 1) :
        if x % i == 0 :
            return False
    else :
        return True

m = map(int,(input().split()))

for i in m :
    if isPrime(reverse(i)) :
        print(reverse(i), end = " ")
