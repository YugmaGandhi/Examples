#in this program we are taking string from user in number format if we use int format it become lenthy
num = input("enter number: ")
#taking sum=0 else it will take garbage value
sum = 0
#creating for loop here where we use range 0 to length of number
#now when user input any number this loop run and suppose it start with value of i as 0
#then it goes in loop where sum has initial value 0 wnd int(num[i]) will convert string into number so that we can add and i has value 0
#so as per indexing i will go from 0 to length of number and take index values from user
for i in range(0,len(num)):
    sum = sum + int(num[i])
#finally when loop completes the value of sum wiil be sum of all digits user have entered
print(sum)