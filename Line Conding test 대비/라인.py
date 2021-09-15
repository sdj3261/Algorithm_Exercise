# 백준 1316 그룹단어체커
# check = []
# cnt = int(input())
# for i in range(cnt) :
#     word = input()
#     for i in range(len(word)-1) :
#         if word[i] != word[i+1] :
#             if word[i] in word[i+1:] :
#                 cnt-=1
# print(cnt)

# 백준 2941 크로아이탕 알파벳
# croatia_alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']
# check_str = ""
# change_alpha = ['=','-']
# word = input()
# cnt = 0
# for i in croatia_alpha :
#     word = word.replace(i,'$')
# print(word)
#
# print(len(word))

# 백준 5622 다이얼
# word = input()
# dial = ["","","","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
# answer = 0
# for j in range(len(word)) :
#     for i in dial :
#         if word[j] in i :
#             answer += dial.index(i)
# print(answer)
# words = input().upper()
# unique_word = list(set(words))
# 백준 단어 세기
# cnt_list = []
# for x in unique_word :
#     cnt = words.count(x)
#     cnt_list.append(cnt)
# if cnt_list.count(max(cnt_list)) > 1 :
#     print("?")
# else :
#     max_index = cnt_list.index(max(cnt_list))
#     print(unique_word[max_index])

# import sys
#
# #백준 4949 균형잡힌세상
# # while True :
# #     a = input()
# #     stack = []
# #
# #     if a == "." :
# #         break
# #
# #     for i in a :
# #         if i == '[' or i == '(' :
# #             stack.append(i)
# #         elif i == ']' :
# #             if len(stack) != 0 and stack[-1] == '[' :
# #                 stack.pop() # 맞으면 지워서 stack을 비워줌 0 = yes
# #             else :
# #                 stack.append(']')
# #                 break
# #         elif i == ')' :
# #             if len(stack) != 0 and stack[-1] == '(' :
# #                 stack.pop()
# #             else :
# #                 stack.append(')')
# #                 break
# #     if len(stack) == 0 :
# #         print('yes')
# #     else :
# #         print('no')
#
#
# # 백준 1996 프린터 큐
# # from collections import deque
# # list2 = []
# # test_case = int(input())
# #
# # for i in range(test_case) :
# #     doc,guess = map(int,input().split())
# #     queue = deque(map(int,input().split()))
# #     index = [0 for _ in range(doc)]
# #     index[guess] = 1
# #     cnt = 0
# #     while True :
# #         if max(queue) == queue[0] :
# #             if index[0] == 1 :
# #                 break
# #             else :
# #                 queue.popleft()
# #                 index.pop(0)
# #                 cnt += 1
# #         else :
# #             queue.append(queue.popleft())
# #             index.append(index.pop(0))
# #
# #     print(cnt+1)
# #     print(index)
#
# # test_case = int(input())
# # from collections import deque
# #
# # for i in range(test_case) :
# #     flag = 0
# #     func = list(input())
# #     num = int(input())
# #     list = input()
# #     arr = deque()
# #     answer = []
# #     str = ""
# #
# #     for x in list :
# #         if len(list) == 2 :
# #             break
# #         if x == "," or x == list[len(list)-1]:
# #             arr.append(int(str))
# #             str = ""
# #         elif x.isdigit() :
# #             str += x
# #         else :
# #             pass
# #
# #     for f in func :
# #         if f == 'R' :
# #             for _ in range(len(arr)-1) :
# #                 arr.reverse()
# #         elif f == 'D' :
# #             if len(arr) == 0 :
# #                 flag = 1
# #                 break
# #             else :
# #                 arr.popleft()
# #     if flag == 1 :
# #         print("error")
# #     else :
# #         for i in range(len(arr)) :
# #             answer.append(arr.popleft())
# #         print(answer)
#
# from itertools import permutations
# def solution(numbers):
#     nums = list(numbers)
#     per = []
#     answer = []
#     print(nums)
#     for i in range(1,len(numbers)+1) :
#         per += list(permutations(nums,i))
#     new_nums = [int(("").join(p)) for p in per]
#
#     for n in new_nums :
#         if n < 2 :
#             continue
#         check = True
#         for i in range(2,int(n**0.5) + 1) :
#             if n % i == 0 :
#                 check = False
#                 break
#         if check:
#             answer.append(n)
#
#     print(answer)
#     return len(answer)
# print(solution("011"))

#print('나의 이름은 "%s"입니다. 나이는 %d세이고 성별은 %s입니다.'%('한사람',33,'남성'))
#print('나의 이름은 {}입니다'.format('한사람'))

#프로그래머스 타겟넘버 bfs


from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n) :
        if visited[com] == False :
            BFS(n, computers, com, visited)
            answer += 1
    return answer
def BFS(n,computers, com, visited) :
    visited[com] = True
    queue = deque()
    queue.append(com)
    while len(queue) != 0 :
        com = queue.popleft()
        visited[com] = True
        for connect in range(n) :
            if connect != com and computers[com][connect] == 1 :
                if visited[connect] == False :
                    queue.append(connect)

