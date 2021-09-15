from typing import Optional, List

a= [1,2,3,2,45,2,5]
print(list(enumerate(a))) #인덱스와 같이 출력하고 싶을 때
divmod(5,3) # 몫과 나머지를 한꺼번에 계산
#print(' '.join(a)) # 문자열 리스트 출력시 join으로 묶어서 계산

#딕셔너리 모듈
import collections
a = collections.defaultdict(int)
a['A'] = 5
a['B'] = 4
a['C'] += 1
#기본데이터 0 이삽입되고 1을 더해 C = 1출력
b = [1,2,3,4,5,5,5,6,6]
b = collections.Counter(b) #객체에 대한 반복적인 값 개수 계산 딕셔너리로 리턴
print(b)
#가장 빈도수 높은 요소 출력
print(b.most_common(2))
#입력 순서 그대로 유지되는 딕셔너리
collections.OrderedDict({'banana' : 3, 'dd' : 4})


