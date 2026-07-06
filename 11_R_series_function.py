import math
n = int(input("enter the integer nbr n: "))
x = float(input("enter x: "))
def factorial(num):
    result_fact = 1
    for x in range(1,num+1):
        result_fact *= x
    return result_fact
def power(x,n):
    return pow(x,n)
def calc_r(x , n):
    r = 1
    for i in range(1,n+1):
        r = r + pow(-1,i) *(factorial(i)/power(x,i))
    return r
print(f"the result is R={calc_r(x,n)}")


