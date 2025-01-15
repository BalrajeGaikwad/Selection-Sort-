"""def sort(num):
    for i in range(4):
        minpoint=i
        for j in range(i,5):
            if num[j]<num[minpoint]:
                minpoint=j
        temp=num[i]
        num[i]=num[minpoint]
        num[minpoint]=temp
num=[5,3,6,7,2]
sort(num)
print(num)
"""



num=[5,3,4,5,6,7]
"""for i in range(5):
    minpoint=i
    for j in range(i, 6):
        if num[j]<num[minpoint]:
            minpoint=j

    temp=num[i]
    num[i]=num[minpoint]
    num[minpoint]=temp

print(num)
"""

for i in range(len(num),0,-1):
    for j in range(i):
        if num[j] > num[j+1]:
            temp=num[j]
            num[j]=num[j+1]
            num[j+1]=temp

print(num)