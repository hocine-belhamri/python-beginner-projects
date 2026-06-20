foods = []
prices = []
total = 0
while True:
    food = input("enter the food u wanna buy: (q to quit) ")
    if food.lower() == 'q':
        break
    foods.append(food)
    prices.append(int(input("enter the price of u re food: ")))
print("------------------your cart:----------------")
for x in range(len(foods)):
    print(f"{foods[x]} : {prices[x]} dzd")
    total += prices[x]
print("-----the total-----")
print(f"it costs u: {total} dzd")

