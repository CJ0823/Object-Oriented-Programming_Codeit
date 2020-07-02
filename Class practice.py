def func():
 print("This is a function") # Line 15를 출력하기 위한 func 함수.

def Deco(any_func):
 def SE():
  print("---start---")
  any_func()
  print("---end---")
 return SE

@Deco
def func1():
 print("This is another function")

Deco(func)() 
# 실행 시, Deco 함수의 parameter로 func 함수를 넣는다.
# Deco 함수는 실행되면 SE 함수를 리턴하는데, SE 함수는 parameter로 받은 any_func함수를 실행(any_func())하고,
# 이 함수의 앞뒤로 ---start---, 와 ---end--- 구문을 넣어준다.
# 함수 자체를 parameter로 넣어줄때는 함수명만 입력하고, 함수를 실행할 때는 함수명 뒤에 ()를 붙여야 함을 기억하자.

func1()
#func1 함수 정의 시에, func1함수 위에 Decorator를 나타내도록 @Deco라고 작성해주었기 때문에,
#func1 함수는 Deco 함수의 parameter로서 들어가서 SE 함수로 바뀌어서 나오게 되고, SE 함수가 실행되어 결과가 출력되게 된다.



"""class Car:
 count = 0 #Class 변수 count를 정의
 
 def __init__(self, color, speed) :
  self.color = color
  self.speed = speed

  Car.count +=1 # __init__ 호출때마다 Car class의 count 변수에 +1

car1 = Car("blue", 100)
car2 = Car("black", 120)
car3 = Car("red", 150)

Car.count = 1
## class이름.class변수이름 = value 로 class 변수값을 지정해주도록한다.
## 이렇게 하면 아래 print구문에서 출력값들이 instance의 숫자인 '3'이 아니라 '1'이 된다.

print(Car.count)  #class이름.class변수이름 으로 class 호출 가능함
print(car1.count) #instance이름.class변수이름 으로 class 호출 가능함
"""


"""class Car:
 def MakeCar(self, color, speed):
  self.color = color
  self.speed = speed

car1 = Car()
car1.MakeCar('blue', 100)"""