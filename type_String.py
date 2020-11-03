# 문자형 관련 연산자

# 문자형은 immutable에 속하는 객체이다
# immutable은 순회가 가능하고 수정이 불가능하다
str1 = 'he is a developer'
str2 = '123'
str3 = ""

# 문자열의 길이 len()
print(len(str1), len(str2), len(str3)) # 17 3 0
print('------------------------------ \n')

# 문자열의 형변환 str()
number = 12
print(str(number), type(number)) # 12 <class 'int'>
print('------------------------------ \n')
# Raw string : 이스케이프문자를 무시할 수 있다 (그대로 출력) ex) 경로표시하는 데 사용된다
raw_s1 = r'C:\Programs\Test'
print(raw_s1)
print('------------------------------ \n')

# 멀티라인
mutiline = \
"""
세로로
출력이
가능하다('\'앞에 표기)
"""
print(mutiline)
print('------------------------------ \n')

# 문자열 연산
str3 = 'abc'
str4 = 'def'
print(str3 + str4) # abcdef
print('------------------------------ \n')

# 중요 in() : 포함하는지 순회하면서 판단, return boolean
in_str = "What a nice"
print('a' in in_str) # immutable이기 때문에 가능
print('z' not in in_str) # True
print('------------------------------ \n')


# islower() : 문자열이 전부 소문자인가?? 
str4 = "javascript"
str5 = 'React'
print(str4.islower(), str5.islower())
print('------------------------------ \n')

# capitalize() : 첫번째 문자만 대문자출력
print(str4.capitalize()) # Javascript
print('------------------------------ \n')

# replace(a, b) : 문자열 대체
str6 = 'Nice man'
print(str6.replace('Nice', 'Good'))
print('------------------------------ \n')

# 문자열 슬라이싱!!!
# 슬라이싱 [1:3] : 1 >= && < 3  마지막은 포함하지 않으니까 주의!!! 
# 역순은 '-1'부터 시작한다!!!!!
print('--------------중요-------------- \n')
print(str6[0:3]) # Nic
print(str6[:len(str6)])
print(str6[::-1]) # 역순으로 출력하는 방법 nam eciN
print(str6[1:-2]) # ice m
print(str6[:6:2]) # Nc (6은 포함하지않음)