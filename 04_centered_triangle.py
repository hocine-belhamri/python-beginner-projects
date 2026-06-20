#rectangle 
rows = int(input("enter the nbr of rows: "))
#columns = int(input("enter the nbr of columns: "))
columns = 1
triangle = ""
for y in range(0,rows):
    for x in range(0,columns):
        triangle = triangle + "* "
    print(f"{triangle:^{rows*2}}",end = "")
    print()
    columns += 1
    triangle = ""
