a = float(input("length of first side: "))
b = float(input("length of second side: "))
c = float(input("length of third side: "))

if a==b==c:
    print("triangle is equilateral")
elif a==b or b==c or a==c:
    print("triangle is isosceles")
else:
    print("triangle is  scalene")

