
class Calculator():
  x=0
  y=0
  def __init__(self,x,y,oper):
    self.x = x
    self.y = y
    if(oper=="+"):
      self.plus()
    elif(oper=="-"):
      self.minus()
    elif(oper=="*"):
      self.multiply()
    elif(oper=="/"):
      self.divide()
    else:
      print("Your operation was wrong !")
  def multiply(self):
    result = self.x * self.y
    print("Result of", self.x ," x ",self.y," = ",result)
  
  def divide(self):
    result = self.x / self.y
    print("Result of", self.x ," / ",self.y," = ",result)

  def plus(self):
    result = self.x + self.y
    print("Result of", self.x ," + ",self.y," = ",result)

  def minus(self):
    result = self.x - self.y
    print("Result of", self.x ," - ",self.y," = ",result)

print("Calculator formate :  x (+,-,*,/) y")
x = int(input("Enter x :"))
oper = input("Enter operation :")
y = int(input("Enter y :"))

cal=Calculator(x,y,oper)
