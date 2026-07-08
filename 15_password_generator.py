import string as s
import random as r
print("welcome to Secure Password & API Key Generator")
print()
length = int(input("What length do they want the password to be?(enter a nbr) : "))
upper = input("Do they want to include uppercase letters? (Yes/No)").lower()
lower = input("Do they want to include lowercase letters? (Yes/No)").lower()
digits = input("Do they want to include digits? (Yes/No)").lower()
special_cha = input("Do they want to include special character symbols? (Yes/No)").lower()
allowed_char = ""
if upper == "yes":
    allowed_char += s.ascii_uppercase
if lower == "yes":
    allowed_char += s.ascii_lowercase
if digits == "yes":
    allowed_char += s.digits
if special_cha == "yes":
    allowed_char += s.punctuation
pass_word = []
if allowed_char == "":
    print("Error: You must select at least one character type!")
else:
    for x in range(length):
        pass_word.append(r.choice(allowed_char))
    r.shuffle(pass_word)
    print(f"your secure password is: ",end="")
    for char in pass_word:
        print(char,end= "")
