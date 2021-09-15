def solution(v) :
    answer = []
    x = []
    y = []
    for i in range(len(v)) :
        x.append(v[i][0])
        y.append(v[i][1])
    for t in x :
        print(x.count(t))
        if x.count(t) == 1 :
            answer.append(t)
            break
    for t in y :
        if y.count(t) == 1 :
            answer.append(t)
            break

    return answer