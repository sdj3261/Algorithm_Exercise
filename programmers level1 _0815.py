#수박수박수박? Level1 문제

def solution(n):
    answer = ''
    for i in range(n) :
        if i % 2 == 0 :
            answer += "수"
        else :
            answer += "박"
    return answer


def solution2(lottos, win_nums):
    answer = []
    count = 0
    zerocount = 0

    for i in range(len(win_nums)) :
        if lottos[i] in win_nums :
            count+=1
        elif lottos[i] == 0 :
            zerocount+=1
        else :
            pass

    max_count = zerocount + count
    min_count = count

    if min_count < 0 :
        min_count = 0

    if 7-max_count <= 5 :
        answer.append(7-max_count)
    else :
        answer.append(6)
    if 7-min_count <= 5 :
        answer.append(7-min_count)
    else :
        answer.append(6)

    return answer
print(solution2([44,1,0,0,31,25],[31,10,45,1,6,19]))
