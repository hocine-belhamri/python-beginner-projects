operator = input("enter the operator: ")
fst =  float(input("enter the 1st nbr: "))
snd = float(input("enter the second nbr: "))
if operator == "+":
   print(f"the result is :{fst+snd}")
elif  operator == "-":
   print(f"the result is :{fst-snd}")
elif  operator == "*":
   print(f"the result is :{fst*snd}")
elif  operator == "/":
   print(f"the result is :{fst/snd}")
else: print("enter a valid operator")