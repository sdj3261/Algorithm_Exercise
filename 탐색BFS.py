def DFS(v) :
    global cnt
    if v == n :
        cnt += 1
        for x in path :
            print(x, end = " ")
        print()
    else :
        for i in range(1,n+1) :
            if g[v][i] == 1 and ch[i] == 0 :
                ch[i] = 1
                path.append(i)
                DFS(i)
                #뒤로 BACK 하는 지점
                path.pop()
                ch[i] = 0
n,m = map(int, input().split())
g = [[0]*(n+1) for _ in range(n+1)]
ch=[0] * (n+1)
print(g)
for i in range(m) :
    a, b = map(int,input().split())
    g[a][b] = 1
cnt = 0
path = []
path.append(1)
ch[1] = 1
DFS(1)
print(cnt)