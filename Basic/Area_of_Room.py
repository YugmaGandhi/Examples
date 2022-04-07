#area of room in meters
# here in vaiable thare is float is used whivh is used to pre define the values
# input is used to take the input from user in which written in inveerted coma can be displayed to user to understand what to input

length = float(input("input the lenght of room in meters: "))
width = float(input("input the width of room in meters: "))

area = length * width
#here in print we need to convert area value to string else it will not print that
print("here is the area of the room "+str(area)+"meter^2. ")

#there is another mehtod to joint the variable in string function
print("here is the area of the room",area,"meter^2.")

#thare are other methods too please check --Notes on python--