def func1(a, b):
     if(a > b):
          while(a >= b):
               a -= 1
               b += 1
     else:
          b += a 
     return b 

a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(func1(a,b))