def fib(n):
    if n>0:
        a = 0
        b = 1
        if n==1:
            print(a)
        else:
            print(a)
            print(b)
            for i in range(2,n):#here range should be from 2 to n because we already printed first 2 numbers
                c = a+b
                a = b
                b = c
                if c<=n:#this condition will allow us to print upto the sum limit and not number of terms
                    print(c)

    else:
        print("invalid number")

fib(int(input("enter no till you want fibonicci : ")))