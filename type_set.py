# 집합 : 수치연산 쪽에서 많이 사용된다
#        순서 X, 중복 X

# 선언 : set([])형태로 해야한다

a = set([1,2,3,4])
print("set(리스트) 형태로 해야만한다", a)
print("------------------------------ \n")

print("set은 대부분 형변환하여 사용된다 ex) list(a), tuple(a)")
print("------------------------------ \n")

s1 = set([1,2,3,4,5,6,7])
s2 = set([4,5,6,7,8,9,0])

# 집합 함수
print("intersection(), & : 교집합 = ", s1 & s2)
print("difference(), - : 차집합 = ", s1.difference(s2))
print("union(), | : 합집합 = ", s2.union(s1))

# 추가/제거
print("add() : ", s1.add(18))
print("add(1)을 하면 중복이 허용되지 않기 떄문에 s1그대로 출력 : ", s1.add(1))
print("remove(4) : ", s2.remove(0))