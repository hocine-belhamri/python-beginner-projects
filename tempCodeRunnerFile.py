import random as r
import string as s

print("Which cryptographic method do you want to use?")
print("1.Random One-Time Cipher")
print("2.Caesar Shift Cipher")
choice = int(input("enter the nbr of the option: "))
if choice == 1:
    chars = s.punctuation + s.digits + s.ascii_letters + " "
    chars = list(chars)
    keys= chars.copy()
    r.shuffle(keys)

    option = int(input("enter '1' to encrypt or '2' to decrypt: "))

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
elif choice == 2:
    keys = []
    chars = s.ascii_lowercase
    for char in chars:
        if char not in ["x", "y" ,"z"]:
            i = chars.index(char)
            keys.append(chars[i+3])
    keys.insert(0, "z")
    keys.insert(0, "y")  
    keys.insert(0, "x")  
    print(chars)
    print(keys)
else:
    print("invalid choice!")
