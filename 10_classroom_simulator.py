import math
import time
import random
abscences = []         # for option 6 and 7
clss_nm = ""
while clss_nm == "":
 clss_nm = input("enter class name: ")
 no_space = clss_nm.replace(" ","")
 if no_space.isalpha():
    if len(clss_nm)>2:
      break
    else:
       print("class name must contains more than 2 characters!")
       clss_nm = ""
 else:
    print("class name must contains only letters and spaces!")
    clss_nm = ""
nbr_st = 3
while nbr_st <= 10 and nbr_st >= 3:
 nbr_st = input("enter number of students: ")
 if nbr_st.isdigit():
   nbr_st = int(nbr_st)
   if nbr_st >= 3 and nbr_st <= 10:
    break
   else:
    print("number of student must be between 3 and 10")
    nbr_st = 3
 else:
   print("number of student must be a number")
   nbr_st = 3
    
names = {}
grades = {}
i = 0
for student in range(0,nbr_st):
 i += 1
 id = ""
 while id == "":
   id_check = False
   id = input(f"enter the id of the {i} student: ")
   no_space = id.replace(" " , "")
   if id.isdigit():
     break
   else:
     if id.isalpha():
       print("student id must contain at least one digit")
       id = ""
     else:
        for char in id:
           if char.isdigit():
            id_check = True
            break
        if id_check == False:
          print("the id must contain at least one digit !")
          id = ""

       
 name_st = ""
 while name_st == "":
   name_st = input(f"enter the full name of the {i} student: ")
   no_space = name_st.replace(" " , "")
   if no_space.isalpha():
     break
   else:
     print("the name of the student must contain only letters and spaces")
     name_st = ""
     
 names.update({id : name_st})
 grade1 = ""
 grade2 = ""
 grade3 = ""
 while grade1 == "":
  grade1 = input("enter grade 1: ")
  if grade1.isdigit():
   grade1 = int(grade1)
   if grade1 >= 0 and grade1 <= 20:
     break
   else:
     print("grade 1 must be between 0 and 20")
     grade1 = ""
  else:
    print("grade 1 must be a number!")
    grade1 = ""
 while grade2 == "":
  grade2 = input("enter grade 2: ")
  if grade2.isdigit():
   grade2 = int(grade2)
   if grade2 >= 0 and grade2 <= 20:
     break
   else:
     print("grade 2 must be between 0 and 20")
     grade2 = ""
  else:
    print("grade 2 must be a number!")
    grade2 = ""
 while grade3 == "":
  grade3 = input("enter grade 3: ")
  if grade3.isdigit():
   grade3 = int(grade3)
   if grade3 >= 0 and grade3 <= 20:
     break
   else:
     print("grade 3 must be between 0 and 20")
     grade3 = ""
  else:
    print("grade 3 must be a number!")
    grade3 = ""
 grades.update({id : [grade1 , grade2 , grade3]})

option = ""
while option == "": 
  print("==============  Hello Sir ==================")
  print("============================================")
  print("1. Show all students")
  print("2. Search student")
  print("3. Show grades")
  print("4. Class ranking")
  print("5. Random student picker")
  print("6. Attendance check ")
  print("7. Class report")
  print("8. Quit")
  print("=============================================")
  option = input("choose an option by typing the nbr of it:")
  if option.isdigit():
    option = int(option)
    if option > 0 and option <= 8:
     print(f"you re option is: {option}")
    else:
      print("the nbr of option should be between 1 and 8!")
      option = ""
  else:
    print("the option should be a nbr!")
    option = ""

  if option == 1:
    for Key , Value in names.items():
      print(f"Id: {Key} , name of student: {Value}")
    option = ""
  elif option == 2:
    id = ""
    while id == "":
      id = input("enter the id of the student: ")
      no_space = id.replace(" " , "")
      if id.isdigit():
        break
      else:
        if id.isalpha():
          print("student id must contain at least one digit")
          id = ""
        else:
         break    
    
    print(f"the full name of the student: {names.get(id , 'not found')} , his Id: {id} ")
    option = ""
  elif option == 3:
    id = ""
    while id == "":
      id = input("enter the id of the student: ")
      no_space = id.replace(" " , "")
      if id.isdigit():
        break
      else:
        if id.isalpha():
          print("student id must contain at least one digit")
          id = ""
        else:
         break    
    grades_of_student = grades.get(id , "not found")
    if grades_of_student == "not found":
     print("not found!")
     option = ""
    else:
     sum = 0
     i = 0
     print(f"student id: {id}")
     for grade in grades_of_student:
      i += 1
      print(f"the {i} grade: {grade}")
      sum += grade
     avg = sum / 3
     print(f"the average of the student is: {avg}")
     option = ""
     print()

  elif option == 4:
    avgerages = {}          
    avgs = []
    for Key , Value in grades.items():
     sum = 0
     id_st = Key                     #id of the student
     for grade in Value:
      sum += grade
     avg = sum/3
     avgerages.update({id_st : avg})
     avgs.append(avg)
    avgs.sort()
    sorted_averages = {}
    for i in reversed(range(len(avgs))):
     for Key , Value in avgerages.items():
       if Value == avgs[i]:
         sorted_averages.update({Key : avgs[i]})
    print("your option is: 4")
    print(" students sorted from highest to lowest average")
    i = 1
    for Key , Value in sorted_averages.items():
      print(f"the {i} student: id: {Key} , average: {Value:.2f} ")   # add floor func
      i += 1
    option = ""
         

  elif option == 5:
    names_list = []
    for Value in names.values():
      names_list.append(Value)
    for second in reversed(range(3)):
      print(second+1)
      time.sleep(1)
    print(random.choice(names_list))
    option = ""

  elif option == 6:
    abscence_report = {} 
    for name in names.values():
      print(name)
      abscence = ""
      while abscence != "p" and abscence != "a":
       abscence = input("enter 'p' for present or 'a' for absent").lower()
       if abscence == "p" or abscence == "a":
         abscences.append(abscence)
         if abscence == "p":
           abscence_report.update({name : "present"})
         if abscence == "a":
           abscence_report.update({name : "abscent"})
       else:
         print("enter a valid chioce pls")
    option = ""
  elif option == 7:
    avgerages = {}          
    avgs = []
    sorted_averages = {}
    if abscences == []:
      abscence_report = {} 
      for name in names.values():
        abscence = ""
        while abscence != "p" and abscence != "a":
          abscence = input("enter 'p' for present or 'a' for abscent").lower()
          if abscence == "p":
              abscence_report.update({name : "present"})
          elif abscence == "a":
              abscence_report.update({name : "abscent"})
          else:
            print("enter a valid chioce pls")

    for Key , Value in grades.items():
     sum = 0
     id_st = Key                  
     for grade in Value:
      sum += grade
     avg = sum/3
     avgerages.update({id_st : avg})
     avgs.append(avg)
    avgs.sort()
    lowest_avg = avgs[0]
    highest_avg = avgs[-1]
    for i in reversed(range(len(avgs))):
     for Key , Value in avgerages.items():
       if Value == avgs[i]:
         sorted_averages.update({Key : avgs[i]})
      
     for Key , Value in avgerages.items():
       if Value == highest_avg:
          first_st = Key
       if Value == lowest_avg:
          last_st = Key    
    sum = 0      
    for i in range(len(avgs)):
      sum += avgs[i]
    class_avg = sum / len(avgs)

    nbr_passed_stu = 0
    nbr_FAILED_stu = 0 
    for aver in avgerages.values():
      if aver >= 10:
        nbr_passed_stu += 1
      else:
        nbr_FAILED_stu += 1
    
    grade_category = {}
    for id , grade in avgerages.items():
      if grade >= 16: 
        grade_category.update({id : "excellent"})
      elif grade >= 14 and grade < 16:
        grade_category.update({id : "very good"})
      elif grade >= 12 and grade < 14:
        grade_category.update({id : "good"})
      elif grade >= 10 and grade < 12:
        grade_category.update({id : "pass"})
      else:
        grade_category.update({id : "fail"})
  
    print("==========================================")
    print()
    print(f"CLASS REPORT - {clss_nm}")
    print()
    print("==========================================")
    print()
    print(f"Total Students : {nbr_st}")
    print()
    print(f"Class Average : {class_avg:.2f}")
    print()
    for id , average in sorted_averages.items():
      print(f"highest average : {average} ({names.get(id)})")
      break
    for id , average in sorted_averages.items():
      if lowest_avg == average:
        print(f"lowest average : {average} ({names.get(id)})")
        break
    print()
    print(f"passed students: {nbr_passed_stu}")
    print()
    print(f"failed students: {nbr_FAILED_stu}")
    print()
    print("------------------------------------------")
    print("NAME ID AVERAGE CATEGORY")
    print()
    print("------------------------------------------")
    print()

    for id1 , name in names.items():
      for id2 , average in sorted_averages.items():
       if id2 == id1:
        for id3 , category in grade_category.items():
          if id3 == id2:
            print(f"{name} {id1} {average} {category}")
            print()
    print("==========================================")
    print()
    abscent_students = []
    for name , abcence in abscence_report.items():
      if abcence == "abscent":
        abscent_students.insert( 0 , name)
    print(f"Abscent Students: " , end="")
    for i in range(len(abscent_students)):
      print(abscent_students[i], end = ", ")
    print()
    print(f"Present Students: {nbr_st-len(abscent_students)}/{nbr_st}")
    print()
    print("==========================================")
    option = ""
  else:
    print("thank you for using the program!")
    print()
    print("goodbye sir !")
    break
