# 상속을 하는 이유 : 유지보수, 생산성

class Car:
    def __init__(self, car_Type, color):
        self.car_Type = car_Type
        self.color = color
    
    def show(self):
        return 'Car Class "Show Method"'


class BmwCar(Car):
    """Sub CLass"""
    def __init__(self, car_name, car_Type, color):
        super().__init__(car_Type, color)
        self.car_name = car_name
    
    def show_model(self) -> None:
        return 'Your Car Name : %s' % self.car_name


class BenzCar(Car):
    """Sub CLass"""
    def __init__(self, car_name, car_Type, color):
        super().__init__(car_Type, color)
        self.car_name = car_name
    
    def show_model(self) -> None:
        # Parent Method Call
        print("부모의 메소드 콜 : ", super().show())
        return 'Your Car Name : %s' % self.car_name

    # 오버라이딩
    def show(self):
        return 'Car Info : %s %s %s' % (self.car_name, self.car_Type, self.color)



# 
model1 = BmwCar('520d', "SUV", 'black')

print(model1.color, model1.car_name, model1.car_Type)
print("부모의 메소드 : ", model1.show())
print("자식의 메소드 : ", model1.show_model())

model2 = BenzCar('220d', "hatchback", 'red')

print("오버라이딩 show() : ", model2.show())
print()
print(model2.show_model())


# 다중상속

class X:
    pass

class Y:
    pass

class Z:
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(A, B):
    pass

print(M.mro())