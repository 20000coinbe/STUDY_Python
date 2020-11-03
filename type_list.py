# 리스트 : 중복허용,, 순서있음, 수정삭제 가능

# 선언방법 2가지
a = []
b = list() # 명식적 선언방법

c = [1, 2, 4, 6]
d = [10, 200, "korea", "japan", 'america']
e = [31, 32, ['apple', 'banana', 'grape']]

# 인덱싱
print(e[1]) # 32
print(e[2][2]) # grape
print(c[-1]) # 6


# 슬라이싱
print(e[2][:-2]) # apple
print(d[-4:-1]) # 200, korea, japan