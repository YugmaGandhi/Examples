#here we are taking feet as inpput but giving answer in acre to user
length = float(input("Enter the length of field in feet: "))
width = float(input("Enter the width of field in feet: "))

area_in_feet = length * width
area_in_acre = area_in_feet/43560
#I have used two methods here to limit the float value
#in first method round(variable,limit number) command limit the value
print("the area of field in acres",round(area_in_acre,2),"acre")

#as second method is to use .format method here we need to include curly bracket
# {:.numberf} here number represent the limiting value and f represent float
print("the area of field in acres {:.2f} acre ".format(area_in_acre))