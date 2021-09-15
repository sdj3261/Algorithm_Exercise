#input
n,m = map(int,(input().split()))
#행렬을 받을 2차원 배열
arr = []
#파리새끼들 행렬에 append
for i in range(n) :
    fly = list(map(int,input().split()))
    arr.append(fly)
#최대값 비교하기위해
max = 0
#최대값 비교 전체 큰행렬 쓰윽 탐색
for i in range(n-m+1) :
    for j in range(n-m+1) :
        sum_arr = 0
        # M X M 행렬 쓰윽 탐색
        for dx in range(m) :
            for dy in range(m) :
                sum_arr += arr[i+dx][j+dy]
        #최대값 계속 넣어주기
        if sum_arr > max :
            max = sum_arr
print(max)


