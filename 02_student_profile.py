import math
name=input("enter ur full name: ")
temp_name=name.replace(" ","")

if temp_name.isalpha():
  if len(name)>2:
   age =input("enter ur age: ")
   if not age.isdigit():
    print("the age must contains only digits")
   else: 
    age = int(age)
    if age>16 and age<60:
     id= input("enter ure student id: ")
     if id.isalpha():
      print("the id must contains at least one digit")
     else:
      bio = input("enter the bio: ")
      if len(bio)>=10:
       nbr_ch = len(bio)
       nbr_a = bio.count("a") + bio.count("A")
       i_space = bio.find(" ")
       first_w = bio[:i_space]
       upper_bio = bio.upper()
       reversed_bio = bio[::-1]
       replaced_i = bio.replace("i","*")
       stu_cat = "young student" if age <20 else "regular student" if 20 <= age <= 25 else "mature student"
       print("======================================")
       print("STUDENT PROFILE")
       print("======================================")
       print(f"Name : {name} ")
       print(f"Age : {age} ")
       print(f"Student ID : {id}")
       print(f"Bio length : {len(bio)}")
       print(f"First word : {first_w}")
       print(f"Letter 'a' : {nbr_a} times")
       print(f"The bio in uppercase : {upper_bio}")
       print(f"The bio reversed : {reversed_bio}")
       print(f"The bio with every 'i' replaced by '*' : {replaced_i}")
       print(f"Student Category : {stu_cat}")
       temp_name = temp_name.lower()
       if temp_name == temp_name[::-1]:                        #optional
        print("the name is palindrome") 
       print("=======================================")
      else:
       print("the bio is short!")
    else:
     print("the age must be between 16 and 60")
  else:
   print("the name must contain more than 2 characters")
else:
 print("ERROR_name must not contain digits")