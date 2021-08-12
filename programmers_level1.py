import math

def solution(s) :
    num = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    value = [str(i) for i in range(10)]
    num_dict = dict(zip(num,value))

    answer = ""
    temp = ""

    for i in s :
        if i.isdigit() :
            answer += i
        else :
            temp += i
            if temp in num :
                answer += num_dict[temp]
                temp = ""

    return int(answer)


def solution2(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):

        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result

print(solution2([1,3,2,4,2,3,2,1,4,5,2,1,2,3]))
print(solution("one1three7"))

def solution3(n, lost, reserve):
    set_reserve = (set(reserve) - set(lost))
    set_lost = (set(lost) - set(reserve))

    for i in set_reserve :
        if i-1 in set_lost :
            set_lost.remove(i-1)
        elif i+1 in set_lost :
            set_lost.remove(i+1)

    return n-len(set_lost)

def solution4(s):
    if len(s) % 2 == 1 :
        return s[(int(len(s) / 2))]
    else :
        answer = s[(int(len(s) / 2)) - 1] + s[int((len(s) / 2))]
        return answer


print(solution4("abcd"))


def solution5(n):
    base = ''
    answer = 0

    while n > 0:
        n, mod = divmod(n, 3)
        base += str(mod)
        print(n, base)

    for i in range(len(base)) :
        answer = answer + int(base[i]) * pow(3,len(base) - i - 1)

    return answer

print(solution5(45))


def solution6(new_id):
    #1 stage
    new_id = new_id.lower()
    #2 stage
    check_list = "-_."
    answer = ''
    for word in new_id :
        print(word)
        if word.isalnum() or word in check_list :
            answer += word
    #3 stage
    while '..' in answer :
        answer = answer.replace('..','.')
    #4 stage
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer
    #5 stage
    answer = 'a' if answer == '' else answer
    #6 stage
    if len(answer) >= 16 :
        answer = answer[:15]
        if answer[-1] == "." :
            answer = answer[:-1]
    #7 stage
    if len(answer) <= 3 :
        answer = answer + answer[-1] * (3-len(answer))
    return answer

def solution7(numbers, hand):
    answer = []
    keypad = {1: [0,0], 2:[0,1], 3:[0,2],
              4: [1,0], 5:[1,1], 6:[1,2],
              7: [2,0], 8:[2,1], 9:[2,2],
              '*': [3,0], 0:[3,1], '#':[3,2]}
    left_cs = keypad['*']
    right_cs = keypad['#']
    count = 0

    for i in numbers :
        now = keypad[i]
        if i in [1,4,7] :
            left_cs = now
            answer.append('L')
        elif i in [3,6,9] :
            right_cs = now
            answer.append("R")
        else :
            left_d = 0
            right_d = 0
            count = 0

            for a, b, c in zip(left_cs, right_cs, now) :
                left_d += abs(a-c)
                right_d += abs(b -c)


            if left_d < right_d :
                answer.append('L')
                left_cs = now
            elif left_d > right_d :
                answer.append('R')
                right_cs = now
            else :
                if hand == 'left' :
                    answer.append('L')
                    left_cs = now
                else :
                    answer.append('R')
                    right_cs = now
    answer = "".join(answer)
    return answer
print(solution7([1,4,2,5,8],"right"))

def solution8(n, arr1, arr2):
    def tentwo(t) :
        list1 = []
        while(t>0) :
            t, m = divmod(t,2)
            list1.append(m)
        if len(list1) < n :
            for i in range(n-len(list1)) :
                list1.append(0)
        list1 = list1[::-1]
        return list1

    answer = []
    for k in range(n) :
        for i, j in zip(tentwo(arr1[k]),tentwo(arr2[k])) :
            answer.append((i+j))

    print(answer)
    answer = list(map(str,answer))
    answer2 = []
    temp = ""
    for i in range(n*n) :
        if answer[i] == '0' :
            answer[i] = ' '
        elif answer[i] == '1' :
            answer[i] = '#'
        else :
            answer[i] = '#'

        temp+=answer[i]
        if (i+1) % n == 0 :
            answer2.append(temp)
            temp = ""
    return answer2

def solution9(dartResult):
    n = ''
    score = []
    for i in dartResult :
        if i.isdigit() :
            n+=i
        elif i == 'S' :
            n = int(n) ** 1
            score.append(n)
            n = ''
        elif i == 'D' :
            n = int(n) ** 2
            score.append(n)
            n = ''
        elif i == 'T' :
            n = int(n) ** 3
            score.append(n)
            n = ''
        elif i == '*' :
            score[-2] *= 2
            score[-1] *= 2
        elif i == '#' :
            score[-1] *= -1

    return sum(score)

print(solution9("1S2D*3T"))

