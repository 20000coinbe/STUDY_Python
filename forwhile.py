# for while


# 1 ~ 100까지 더하기
sum1 = 0
n = 1
while n <= 100:
    sum1 += n
    n += 1

print("while을 이용한 방법 : ", sum1) # 5050

print("sum() 이용한 방법 : ", sum(range(1,101))) # 5050


# python의 iterable함수 : map, range, reversed, enumerate, filter, zip

names = ['k', 'l', 'p', 's', 'y']

for name in names:
    print(name)

# 중요 : 딕셔너리의 반복
my_info = {
    "name" : "kim",
    "age" : 130,
    "height" : 190,
    "city" : "seoul"
}

for info in my_info:
    print("키값만 나오게 된다 : ", info) # name, age, height, city 

for info in my_info.values():
    print("values()를 이요해서 값만 출력 : ", info)

for key, value in my_info.items():
    print("중요!!! itmes()를 활용해서 둘다 출력 : ", key, value)


# 문제 : 문자열에서 소문자일 경우 대문자, 대문자일 경우 소문자로 고쳐라
str1 = "JavAScript"

for s in str1:
    if s.isupper():
        print(s.lower())
    else:
        print(s.upper())

# for-else문 : for문이 완전히 실행된 후에 else문으로 들어간다

# continue

lt = [1, "hi", 3143, False, 3.41, 'kim', 1.4]

for i in lt:
    if type(i) is float:
        continue
    print("타입 : ", type(i))
print("float타입을 제외하고 type()을 실행")

