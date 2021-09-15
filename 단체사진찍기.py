from itertools import permutations

def solution(n,data) :
    answer = 0
    friends = ['A', 'C', 'F', 'J', 'M', 'N', 'R', 'T']
    for case in permutations(friends):
        for cond in data:
            others = abs(case.index(cond[0]) - case.index(cond[2])) - 1
            if cond[3] == '=' and others != int(cond[4]):
                break
            elif cond[3] == '>' and others <= int(cond[4]):
                break
            elif cond[3] == '<' and others >= int(cond[4]):
                break
        else:
            answer += 1
    return answer

list = ["N~F=0", "R~T>2"]
print(solution(2,list))