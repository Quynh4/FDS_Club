def funct(x,y):
     if((0 < x <= 1) and (y < 0)):
          return x + y
     elif((x > 1) and (0 < y <= 5)):
          return x * y
     else:
          return x - y

x = int(input("Enter x: "))
y = int(input("Enter y: "))
     
print(funct(x,y))