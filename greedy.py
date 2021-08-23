n = 1260
count = 0
array = [500,100,50,10]

for coin in array :
    count += n // coin
    n = n % coin
print(count)


n, k = map(int,input().split())

result = 0
target = (n // k) * k
result += (n - target)
while True :
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k :
        break
    result += 1
    n //= k
result += (n-1)
print(result)