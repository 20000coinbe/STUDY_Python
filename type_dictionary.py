# 딕셔너리(dic) : 웹에서 송수신과정에서 표준구조인 JSON과 비슷하다
#                 순서 X, 중복X, 수정삭제가능
#                 key와 value로 이루어짐

# 선언
a = {'name' : "kim", 'age' : 12}
b = { 0 : 'hello', 1 : 'bye'}
c = { 0 : 1, 5 : [2,3,4,5]} # value 부분에는 나머지 자료형 사용가능 

# 조회
print(a['name']) # kim
print("get() : 안전하게 값을 조회 가능 있으면 조회, 없으면 None", b.get('address')) # None
print("c[5][1:3] : ", c[5][1:3])
print("---------------------------------- \n")

# 추가
a['address'] = 'seoul'
print("딕셔너리의 추가방법 : a['address'] = 'seoul' : ", a)
print("---------------------------------- \n")

# item은 key와 value를 합친 개념이다
print("a.items() : ", a.items())
print("key값만 리스트형태로 불러오기 : ", b.keys())
print("value값만 리스트형태로 불러오기 : ", c.values())
print("하지만 리스트형태일 뿐이지 리스트는 아니기 떄문에 조작불가능 형변환을 해야한다")
list_key = list(a.keys())
list_values = list(b.values())
print("list_key.index('age') : ", list_key.index('age'))
print("list_values.pop(), list_values : ", list_values.pop(), list_values)
print("in, not in도 사용가능")