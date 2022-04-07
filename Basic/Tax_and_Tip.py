ammount = float(input("please enter the total bill ammount:"))
tax_rate = 0.05 #which is 5% GST
tip_rate = 0.18 #as requirement here 18%

tax = ammount * tax_rate
tip = ammount * tip_rate
grand_total = ammount + tax + tip

print("tax will be of %.2f"%tax)
print("tip will be of %.2f"%tip)
print("the grand toatal will be of %.2f"%grand_total)

# the above printing method include print function 3 times which is time consuming
#here we use bracket after % sign in which include all the parameters which we need to display in order
print("the tax will be %.2f, tip will be %.2f, total will be %.2f"%(tax,tip,grand_total))