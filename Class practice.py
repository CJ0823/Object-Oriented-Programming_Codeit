class Car:
 def __init__(self, color, speed) :
  self.color = color
  self.speed = speed
  print("color : %s, speed : %d" % (color, speed))
 def speedUp(self) : 
  self.speed += 10

car1 = Car("blue", 100)
car2 = Car("black", 50)

print(car1.speedUp())