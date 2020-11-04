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
print("---------------------------")



# 슬라이싱
print(e[2][:-2]) # apple
print(d[-4:-1]) # 200, korea, japan
print("---------------------------")


# 리스트의 연산
list1 = [1,2,3,4]
list2 = [10, 100, 1000]
print("list1 * 3 : ", list1 * 3)
print("list1 + list2 : ", list1 + list2)
print("list1[1] + 'zero' : ", str(list1[1]) + 'zero') # str()붙여서 형변환 해야한다는 것!!
print("---------------------------")

# 리스트 수정삭제
print("슬라이싱과 인덱싱 했을떄의 차이점")
list1[1:2] = [20, 200, 2000]
print(list1)
list1[1] = [20, 200, 2000]
print(list1)

del list1[1]
del list1[-2]
print("del을 이용한 삭제 : ", list1)
print("---------------------------\n")

# 리스트 함수
list3 = [1, "money", True, 100, "apple", 34]
list3.append("banana")
print("append() : 맨끝에 추가시킨다", list3)

list3.insert(2, "여기에 insert")
print("insert() : 원하는 위치에 삽입", list3)

list4 = [100, 3, 40, 12, 2]
list4.sort()
print("sort() : 정렬(오름차순)", list4)

list4.remove(12) # 해당 값을 지워버린다
print("remove() : 해당값을 지운다 ", list4) # [2,3,40,100]
print("del은 인덱스를 통해, remove()는 원소값을 찾아 지운다")

list4.pop()
print("pop() : 마지막 원소를 추출", list4) # [2, 3, 40]

c.extend(d)
print("extend() : 해당 리스트뒤로 붙여준다", c)






