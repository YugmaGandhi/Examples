less_1 = 0.10
more_1 = 0.25

less = int(input("how many bottles do you have which contains 1 or less liter:"))
more = int(input("how many bottles do you have which contains more than 1 liter:"))

refund = less * less_1 + more * more_1

print("here is your refund {:.2f}$".format(refund))

#the %.2f format specifier indicates that the value should be formatted as a floating point number with 2 digis to the right of  decimal points

print("here is your refund %.2f$" % refund)