# 튜플(tuple) : 순서 O, 중복 O, 수정삭제 X, '()'를 사용한다
#               ex) 수정삭제가 불가능 하기 때문에 계좌번호, key값 등 바뀌지 않는 값들에서 많이 사용된다

a = (1)
b = (2,)
c = (1,2,2,4,5)
d = (10,(100, 1000))

print(a, "원소가 하나일 경우 print()할떄는 문제가 없지만 연산시에 튜플이 아니게 되기 떄문에 ','를 붙여주자")
print("del c[1] : ERROR")
print("중첩 가능 : ", d)

# 튜플의 연산
print("튜플연산 b + c : ", b + c)
print("튜플연산 b * 2 : ", b * 2) # (2,2)


# 튜플함수
print("in 사용가능 : ", 3 in d) # false
print("index(a) : 값a의 위치에 인덱스를 반환 c.index(4) = ", c.index(4))
print("count() : 튜플에서 해당값의 개수 c.count(2) = ", c.count(2))