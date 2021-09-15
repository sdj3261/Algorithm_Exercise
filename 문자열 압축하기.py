def solution(s):
    result = []
    if len(s) ==1 :
        return 1
    for i in range(1,(len(s)//2) + 1) :
        co = ''
        cnt = 1
        tmp = s[:i]
        for j in range(i,len(s), i) :
            if tmp == s[j:i+j] :
                cnt += 1
            else :
                if cnt != 1 :
                    co = co + str(cnt) + tmp
                else :
                    co = co + tmp
                tmp=s[j:i+j]
                cnt = 1
        if cnt != 1 :
            co = co + str(cnt) + tmp
        else :
            co = co + tmp

        result.append(len(co))
    return min(result)
print(solution("aabbacc"))