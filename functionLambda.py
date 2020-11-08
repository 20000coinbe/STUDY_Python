# 함수

# 함수사용의 이유 : 반복되고 중복되는 프로그래밍을 피할 수 있다
#  - 하나의 함수에 하나의 기능만을 만드는 것이 좋다

# 함수 정의 방법
# def 함수명(parameter):
#    code;

def hello_return(word):
    val = 'Hello' + str(word)
    return val

# 함수의 리턴
def func_mul(data):
    y1 = data * 10
    y2 = data * 100
    y3 = data * 1000
    return y1, y2, y3 #리턴을 세개 했으니까 일반적으로 3개의 변수를 사용

val1, val2, val3 = func_mul(5)
print(val1, val2, val3)
print("-------------------------- \n")
# 그러나 리턴함수를 다른 데이터 타입을 이용하면 변수 1개로 받을 수 있다
def func_add(data):
    z1 = data + 10
    z2 = data + 100
    z3 = data + 1000
    return [z1, z2, z3] 
    # return (z1, z2, z3) # 튜플도 가능

val4 = func_add(10)
print("리턴함수 : ", val4)

# *args, *kwargs : 가변적인 길이로 파라미터를 받을 수 있음
# '*' : 튜플형태(튜플이기 때문에 iterable)
# '**' : 딕셔너리형태

print("-------------------------- \n")
def args_func(*args):
    print(args)

args_func("kim")
args_func("kim", 'Lee')
args_func("kim", 'Lee', 'park')

print("-------------------------- \n")
# enumerate를 활용한 방법 : index번호를 생성해서 순회
def args_func_enum(*args):
    for i, v in enumerate(args):
        print(i, v)

args_func_enum("seoul", "busan", "jeonju") # 0 seoul, 1 busan, 2 jeonju
print("-------------------------- \n")

# kwargs : keyword의 줄임말
def kwargs_func(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

kwargs_func(name1 = 'kim', name2 = 'lee', name3 = 'park')
print("-------------------------- \n")

# 매개변수의 혼합
def a(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, *args, **kwargs)

a('yes', 'or')
a('yes', 'or', 'yes')
print("-------------------------- \n")


# 중첩함수(스코프)
def nested_func(num):
    def func_in_func(num):
        print(num)
    print('in func') # 1번 출력
    func_in_func(num + 10000) # 2번 출력

print("중첩함수 : (순서중요) ", nested_func(1000))
print("-------------------------- \n")

# 람다(lambda) : 메모리 절약, 코드가 간결해짐, 가독성 향상
#  - 함수는 객체생성 -> 리소스(메모리) 할당 (파이썬은 함수도 객체임)
#  - 람다는 즉시실행(Heap 초기화) -> 메모리초기화

def mul_10(num : int) -> int:
    return num * 10

var_func = mul_10 # 객체생성
print(var_func(10)) # 할당
print("람다식으로 표현한다면 lambda_mul_10 = lambda num : num * 10")
lambda_mul_10 = lambda num : num * 10
print(lambda_mul_10(10))
print("-------------------------- \n")

# 매개변수로 함수를 받는 경우
def func_final(x, y, func):
    print(x * y * func(10)) # 여기서 None이 나온다

func_final(10, 10, lambda_mul_10)
print("람다식을 직접 집어넣기 : ", func_final(10, 10, lambda x: x * 1000))






