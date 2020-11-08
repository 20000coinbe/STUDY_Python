# 조건문 알아야할 것
# 참/거짓 종류

print("참 : '내용', [내용], (내용), {내용} ")
print("거짓 : '', [], (), {} ")

city = ''
if city:
    print("YYES")
else:
    print("NOO") # 출력

# 논리연산자 (and or not)
a = 100
b = 2
print("not a > b : ", not a > b) # false
print("not False : ", not False)

# 연산자 우선순위
print("연산자 우선순위 : 산술 > 관계 > 논리")
print("5 + 10 > 0 and not 3 + 7 == 10 : ", 5 + 10 > 0 and not 3 + 7 == 10)

# 다중if 
# ex) if~elif~elif~elif~else
age = 4
if age <= 20 and age > 5:
    print("HI")
elif age >= 30:
    print("30")
else:
    print("zzzz")
    




