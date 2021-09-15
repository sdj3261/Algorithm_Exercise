#4673 셀프 넘버
# num = set(range(1,10001))
# make_num = set()
#
# for i in range(1,10001) : #i = 850
#     for j in str(i) : # j = "8" , " 5" , "0"
#         i += int(j)
#     make_num.add(i)
#
#
# self_num = sorted(num - make_num)
# for i in self_num :
#     print(i)

#1806 부분합
# import sys
# n , s = map(int,input().split())
# num_list = list(map(int,input().split()))
#
# left,right = 0, 0
# tmp_sum = 0
# min_length = sys.maxsize
# while True :
#     if tmp_sum >= s :
#         min_length = min(min_length, right-left)
#         tmp_sum = tmp_sum - num_list[left]
#         left += 1
#     elif right == n :
#         break
#     else :
#         tmp_sum += num_list[right]
#         right += 1
# if min_length == sys.maxsize :
#     print(0)
# else :
#     print(min_length)
#

A, B, C = map(int,input().split())
day = 1
if B > C:
    print(-1)
else :
    print(int(A/(C-B))+1)





