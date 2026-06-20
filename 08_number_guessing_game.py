import random
entered_nbr = int(input("enter a nbr between 0 and 100: "))
nbr = random.randint(0,100)
attempts = 1
while entered_nbr != nbr:
 attempts += 1
 if entered_nbr > nbr:
    if entered_nbr - nbr > 10:
        print("too much higher")
    else:
        print("you re close, but  you are higher")
 elif entered_nbr < nbr:
    if nbr - entered_nbr > 10:
        print("too much lower")
    else:
        print("you re close, but you are lower")
 if attempts == 10:
    break
 entered_nbr = int(input("enter a nbr between 0 and 100: "))
if attempts == 10:
   print("game over! you lost")
   print(f"the nbr was: {nbr}")
else:
 print("you found it !")
 print(f"you had: {attempts} attempts")

