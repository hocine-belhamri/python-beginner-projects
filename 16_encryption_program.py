import random as r
import string as s


chars = s.punctuation + s.digits + s.ascii_letters + " "
chars = list(chars)
keys= chars.copy()
r.shuffle(keys)
while True:
    option = int(input("enter '1' to encrypt or '2' to decrypt or '3' to quit: "))

    #Encrypt

    if option == 1:
        original_text = input("enter the text u want to encrypt: ")
        encrypted = ""
        for char in original_text:
            i = chars.index(char)
            encrypted += keys[i]
        print()
        print(f"the encrypted: {encrypted}")
        print(f"the original: {original_text}")

    #Decrypt

    elif option == 2:
        encrypted = input("enter the text u want to decrypt: ")
        decrypted = ""
        for char in encrypted:
            i = keys.index(char)
            decrypted += chars[i]
        print()
        print(f"the decrypted: {decrypted}")
        print(f"the encrypted: {encrypted}")
    
    elif option == 3:
        print("assalam alikum !")
        break
    else:
        print("invalid choice!")
