import math as m

a = float(input("please enter a:"))
b = float(input("please enter b:"))

print("sum = ", a + b)
print("difference = ", a - b)
print("product = ", a*b)
print('quotient = ', a % b)
print('remainder = ', (b-(a % b)))
print('power = ', a**b)
print('log10a = ', m.log10(a))
