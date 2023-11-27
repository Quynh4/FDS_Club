def funct(x,y):
     if((-1<x<1) and (-1<y<1)):
          return x-y-1
     elif((x>=1) and (y>=1)):
          return x+y-1
     elif((x < -1) and (y>0)):
          return x*y-1
     else:
          return x-1
     
x = float(input("Enter x: "))
y = float(input("Enter y: "))

print(funct(x,y))