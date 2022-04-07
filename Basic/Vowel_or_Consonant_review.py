vowels = ('a','e','i','o','u')

l = input("please enter any letter:")
for vowel in vowels:
    if l==vowel:
        print(l,"is vowel")
        break
    elif l!= vowel:
        print(l, "is Consonant")
