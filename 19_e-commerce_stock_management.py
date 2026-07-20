# 1  Add Products: I want to add new items to my system by entering their name, price, size (like 54, 58, 62), and how many I have in stock.
# 2  Sell Items: If a customer buys a shirt, I want to type in the name and size. The program should automatically subtract 1 from the stock.
#       If I am completely out of that size, it should warn me: "Out of stock!"
class product:
    def __init__(self,name, price, sizes,quantity):
        self.name = name
        self.price = price
        self.sizes = sizes
        self.quantity = quantity

products = {}
nbr_product = int(input("enter the number of product u wanna add: "))
for nbr in range(1, nbr_product+1):
    quantity= {}
    sizes = []
    name = input(f"enter the name of the {nbr} product: ")
    price = int(input(f"enter the price of the {nbr} product: "))
    nbr_sizes = int(input("enter the number of the sizes: "))
    for x in range(1, nbr_sizes +1):
        sizes.append(int(input(f"enter the {x} size of the {nbr} product: ")))
    for size in sizes:
        nbr = int(input(f"enter the number of items of the size {size}: "))
        quantity[size] = nbr
    products.update({name : product(name , price , sizes , quantity)})

running = True
while running:
    print("1. sell item")
    print("2. check inventory")
    print("3. quit")
    option = int(input("enter the number of the option: "))
    if option == 1:
        name = input("enter the name of the product: ")
        size = int(input("enter the size of the product: "))

        if name in products and size in products[name].sizes:
            if products[name].quantity[size] != 0:
                products[name].quantity[size] -= 1
            else:
                print("Out of stock!")       
        else:
            print("Out of stock!")
    elif option == 2:
        x = 1
        for name , values in products.items():
            print(f"the {x} product: {name}")
            print(f"price: {values.price}dzd")
            i = 0 
            for size in values.sizes:
                print(f"size: {size}",end=", ")
                print(f"quantity: {values.quantity[size]}")

            x += 1
    elif option == 3:
        print("good bye!!")
        running = False
    else:
        print("invalid choice !!")
