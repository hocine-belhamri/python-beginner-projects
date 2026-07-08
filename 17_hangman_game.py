import random as r
words = ["business" , "granada" , "coconut" , "beginner" , "understand" , "programmer"]
secret_word = r.choice(words)
past_letters = ""
constant_secret_word = secret_word
secret_word = list(secret_word)
display = ""
hearts = 7
mistakes = 0
hangman = [
        r"""
       _______
        |     |
        |     |
        |     
        |    
        |    
        |
        """,
        r"""
       _______
        |     |
        |     |
        |     o
        |    
        |    
        |
        """,
        r"""
       _______
        |     |
        |     |
        |     o
        |     |
        |    
        |
        """   , 
        r"""
       _______
        |     |
        |     |
        |     o
        |    /|
        |     
        |
        """,
        r"""
       _______
        |     |
        |     |
        |     o
        |    /|\
        |     
        |
        """,
        r"""
       _______
        |     |
        |     |
        |     o
        |    /|\
        |    / 
        |
        """,
        r"""
           _______
            |     |
            |     |
            |     o
            |    /|\
            |    / \
            |
           """]
print("--------------------------------")
print("          HangMan Game          ")
print("--------------------------------")
for underscore in range(len(secret_word)):
    display += "-"
display = list(display)
while "-" in display and hearts != 0:
    print(f"you have '{hearts}' hearts!")
    print(f"the secret word: ",end="")
    for underscore in display:
        print(underscore,end="")
    print()
    while True:
        guessed_letter = input("enter one letter: ").lower()
        if guessed_letter in past_letters:
            print("you enterd this letter before!")
            continue
        else:
            if guessed_letter.isalpha() and len(guessed_letter) == 1:
                break
            elif guessed_letter.isalpha():
                print("enter one letter !!")
            else:
                print("enter a letter !!")
    if guessed_letter in secret_word:

        repeat = secret_word.count(guessed_letter)
        for x in range(repeat):
            i = secret_word.index(guessed_letter)
            display[i] = guessed_letter
            secret_word[i] = 0
        print("RIGHT!!")
    else:
        hearts -= 1
        print("OH NO!!!!")
        print(hangman[mistakes])
        mistakes += 1
    past_letters += guessed_letter

if "-" not in display:
    print("YOU WIN !!!")
    print(f"the secret word is: {constant_secret_word}")
else:
    print("GAME OVER!")
    print("YOU LOSE")
    print(f"the secret word is: {constant_secret_word}")