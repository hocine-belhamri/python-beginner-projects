x = 0
while x == 0:
    the_sentence = input("enter the sentence: ").lower()
    no_space = the_sentence.replace(" " , "")
    if no_space.isalpha():
        x = 1
        included_letters = ""
        for letter in no_space:
            if letter not in included_letters:
                included_letters += letter
        if len(included_letters) == 26:
            print("the string is Pangram")
        else:
            print("the string is not Pangram")
    else:
        print("the sentence must contain only alphabets!")
        x = 0