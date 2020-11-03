# 타입종류
# Boolean
# Numbers
# String
# Bytes
# Lists
# Tuples
# Sets
# Dictionarie


type_bol = True;
type_num1 = 3;
type_num2 = 3.14;
type_str = "Hello world"
type_list = []
type_set = {3, 4, 5}
type_dic = {
    'id' : 'coco',
    'password' : 1234
}
type_tuple = 1, 2, 3

print(type(type_dic))
print(type(type_num1)) # <class 'int'> 
print(type(type_num2)) # <class 'float'>
print(type(type_tuple))
print(type(type_set))


# 숫자형 타입과 연산자
# / : 나누기
# // : 몫
# % : 나머지
# ** : 지수
num1 = 4
num2 = .5
num3 = 12.

print(num1 ** 2) # 16
print(num2, num3)
print("자동적으로 형변환 : ", num1 * num2)


#형변환
print(int(num2)) # 0
print(float(num1)) # 4.0
string1 = '3' 
print(int(string1)) # 3
print("True -> int로 형변환 : ", int(True)) # 1
print("False -> int로 형변환 : ", int(False)) # 0

# import Math
import math

print("-7의 절대값 : ", abs(-7))
n, m = divmod(100, 8) # 100을 8로 나눈다
print(n, m) # n = 몫, m = 나머지



