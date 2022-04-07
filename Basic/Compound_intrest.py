#let user input their savings

deposite = float(input("please enter the ammount that you want to deposite:"))
#here the intrest rate is 4%

intrest = 0.04

#let user input the no of year that they want to save their money for

year = int(input("for how many full years you want to save :"))
#formula for compound intrest
final_ammount = deposite*((1+intrest)**year)

print("here is the ammount you will get back after %i years %.2f"%(year,final_ammount))
