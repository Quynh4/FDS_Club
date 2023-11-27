def calculate_price(color, bill):
     discount = 0
     if(200 <= bill <= 300):
          if(color == "yellow"):
               discount = 0.3
          elif(color == "white"):
               discount = 0
          else:
               discount = 0
     elif(300 < bill <= 500): 
          if(color == "yellow"):
               discount = 0.4
          elif(color == "white"):
               discount = 0.3
          else:
               discount = 0
     elif(bill > 500):
          if(color == "yellow"):
               discount = 0.6
          elif(color == "white"):
               discount = 0.5
          else:
               discount = 0
     else:
          discount = 0
     return discount

color = input("Enter color: ")
bill = float(input("Enter bill: "))

print(calculate_price(color, bill))
          
          