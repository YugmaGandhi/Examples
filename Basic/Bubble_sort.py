def sort(num):
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            if num[j]>num[j+1]:
                num[j],num[j+1] = num[j+1],num[j]


no = [1,5,21,2,8,6,3,9,7]
sort(no)
print(no)

