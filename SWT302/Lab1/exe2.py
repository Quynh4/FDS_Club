def func2(x,y):
     if((1 > x > 0) and (y < 0)):
          return x + y
     elif(x > 1):
          return x*y
     else:
          return x-y

x = int(input("Enter x: "))
y = int(input("Enter y: "))
     
print(func2(x,y))