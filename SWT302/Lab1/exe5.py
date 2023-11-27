def calculate_price_Tdque(baseprice, specialprice, extraprice, extras, discount):
     addon_discount = 0
     result = 0
     if extras <= 3:
          addon_discount = 10
     elif extras >= 5:
          addon_discount = 15
     else:
          addon_discount = 13
     if discount > addon_discount:
          addon_discount = discount
     result = baseprice/100.0*(100-discount) + specialprice + extraprice/100.0*(100-addon_discount)
     return result

baseprice = float(input("Enter baseprice: "))
specialprice = float(input("Enter specialprice: "))
extraprice = float(input("Enter extraprice: "))
extras = int(input("Enter extras: "))
discount = float(input("Enter discount: "))

print(calculate_price_Tdque(baseprice, specialprice, extraprice, extras, discount))