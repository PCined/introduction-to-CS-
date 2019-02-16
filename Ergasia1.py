def sumIntervals(diasthmata):
    OneByOne=[]
    k=0
    for i in range(0,len(diasthmata),2):       
        OneByOne.append([1,2])
        OneByOne[k][0]=diasthmata[i]
        OneByOne[k][1]=diasthmata[i+1]
        k=k+1
    for i in range(len(OneByOne)):
        f=0
        Check=False
        for j in range(len(OneByOne)):
            if i==f:
                f=f+1
                continue
            if OneByOne[i][0]<=OneByOne[f][0] and OneByOne[i][1]>=OneByOne[f][0]:
                if OneByOne[i][1]>=OneByOne[f][1]:
                    OneByOne.remove(OneByOne[f])            
                    if OneByOne[f-1]==OneByOne[-1]:
                        break
                    f=f-1
                    Check=True
                else:
                    OneByOne[j][0]=OneByOne[i][1]
            f=f+1
        if OneByOne[i]==OneByOne[-1]:
            break
        if Check==True:
            i=i-1
    Sum=0
    for i in range(len(OneByOne)):
        Space=OneByOne[i][1]-OneByOne[i][0]
        Sum=Sum+Space
    print(Sum)

c=input("Grapse ta diasthmata mesa se agkules xwrismena me komma:  ")
a=c.split("[")
k=""
for i in range(len(a)):
    k=k+a[i]
a=k.split("]")
k=""
for i in range(len(a)):
    k=k+a[i]
a=k.split(",")
h=[]
for i in range(len(a)):
    h.append(int(a[i]))
sumIntervals(h)
