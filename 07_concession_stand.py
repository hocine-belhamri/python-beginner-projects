menu = {"pizza carre" : 10, "burger" : 100, "hmiss":50, "marine" : 250,
        "jus" : 60 , "limonade" : 60}
addition = ""
buyings = {}
total = 0
while addition != "no":
 print("----------- menu ------------------")
 for Key , Value in menu.items():
  print(f"{Key} : {Value}dzd")
 print("----------- your order ------------")
 buying = input("enter what u want:  ").lower()
 buyings.update({buying:menu.get(buying)})
 if buyings.get(buying) == None:
  buyings.pop(buying)
 addition = input("u wanna buy something else: (enter 'no' to quit) ").lower()
print("---------- your cart --------------")
for Key , Value in buyings.items():
 print(f"{Key} : {Value}dzd")
if buyings:
 for buying in buyings:
  total += buyings.get(buying)
print("---------- the total ---------------")
print(f"{total} dzd")
