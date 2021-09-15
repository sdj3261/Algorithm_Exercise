#대학 신입생 재학생 일렬로 세우는 방법 몇가지? 1. 좌우 인접 , 재학이 k명, 신입생은 제한 x
#그룹을 하나도 만들지 못하는 경우 0 return
# from itertools import combinations
# def solution(student, k):
#     answer = 0
#     new_group = []
#     if student.count(1) < k :
#         return answer
#
#     for i in range(k,len(student)) :
#         for p in combinations(student,i) :
#             if p.count(1) == k :
#                 new_group.append(p)
#     new_group = set(new_group)
#     new_group = list(new_group)
#     print(new_group)
#     check = []
#     answer = len(new_group)
#     if student.count(1) == k :
#         answer += 1
#     print(answer)
#     for i in range(len(new_group)) :
#         check = [m for m, value in enumerate(new_group[i]) if value == 1]
#         if len(check) >= 2 :
#             for j in range(len(check)-1) :
#                 if abs(check[j+1] - check[j]) > 1 :
#                     answer -= 1
#     return answer
#
#
# print(solution([0,1,0,0,1,1,0],2))

def solution(research, n, k):
    answer = ''
    cnt = [0 for _ in range(100)]
    issue = []
    dict = {}
    dict2 = {}
    sum_dict = {}

    for j in range(len(research)) :
        for i in research[j] :
            if i not in dict :
                dict[i] = 1
                dict2[i] = 0
                sum_dict[i] = 1
            else :
                dict[i] = dict[i] + 1
                sum_dict[i] += 1
        if n == 1 and k == 1:
            return "None"
        for key, value in dict.items() :
            if value >= k :
                dict2[key] += 1

                if dict2[key] >= n and sum_dict[key] >= 2*n*k:
                    issue.append(key)
            else :
                dict2[key] = 0
        print(sum_dict)
        print(1, dict)
        print(2, dict2)
        for key, value in dict.items() :
            dict[key] = 0
    print(4, issue)
    issue = sorted(issue)
    print(4,issue)
    if len(issue) == 0 :
        return "None"
    else :
        return issue[0]

print(solution(	["yxxy", "xxyyy", "yz"],2,1))