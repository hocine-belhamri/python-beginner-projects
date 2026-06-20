questions = (("who is the biggest animal"),
             ("what is the largest city"),
             ("where is hocine from"),
             ("is eating eggs a lot good?"))
answers = (("A. elephant" , "B. lion " , "C. zebra" , "D. chicken"),
           ("A. jijel" , "B. adrar" , "C. bomarche" , "D. algiers" ),
           ("A. malawi" , "B. TIMIMOUN" , "C. bomarche" , "D. dubai"),
            ("A. yes" , "B. no") )
right_answers = ("A","B","C","B")
guesses = []
score = 0
i = 0
question_nbr = 0
for question in questions:
    print("-------------------------")
    print(question)
    for answer in answers[question_nbr]:
      print(answer, end = " ")
    print()
    guesses.append(input("enter ure guess (A,B,C,D): ").upper())
    if guesses[i] == right_answers[i]:
        print("correct !")
        score += 1
    else:
        print("incorrect !!!!")
    i += 1
    question_nbr += 1

print("----------------------------------------------")
print("                  your score                  ")
print(f"right answers : {right_answers}")
print(f"your answers: {guesses}")
print(f"your score: {score/4*100 : .0f}%")

