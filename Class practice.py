def func():
 print("This is a function")



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
func1()




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