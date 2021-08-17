def solution(record):
    answer = []
    dict = {}
    str = ''

    for line in record :
        line_split = line.split() # enter uid1234 muzi 0,1,2 배열 생성
        if line_split[0] == "Enter" or line_split[0] == "Change" :
            dict[line_split[1]] = line_split[2] # uid1234,muzi
    print(dict)

    for line in record :
        line_split = line.split()
        if line_split[0] == "Enter" :
            str += dict[line_split[1]] + "님이 들어왔습니다."
            answer.append(str)
        elif line_split[0] == "Leave" :
            str += dict[line_split[1]] + "님이 나갔습니다."
            answer.append(str)
        str = ''

    return answer

def solution2(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        print(r)
        rr = r.split(' ')
        print(rr,"?")
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]
    print(namespace,"a")
    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer


print(solution2(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))