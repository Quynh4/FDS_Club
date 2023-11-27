def identify_class(ticket, card):
     notify = ""
     if(ticket == "economy"):
          if(card == "gold"):
              notify = "You may get upgraded to business class"
          else:
               notify = "You may delay"
     else:
          notify = "You may delay"
     
     return notify

ticket = input("Enter your ticket: ")
card = input("Enter your card: ")

print(identify_class(ticket, card))