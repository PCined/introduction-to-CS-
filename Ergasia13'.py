def maxDistance(distances,limit):
    distances.sort()
    max_sum=0
    new_sum=0
    if sum(distances)<=limit:
            max_sum=sum(distances)
    else:
        for i in range(len(distances)):
            new_sum=distances[i]
            for j in range(len(distances)-1,i,-1):
                if (distances[j]+new_sum)<=limit:
                    new_sum=neoAthroisma(distances,limit,new_sum,i,j)
                    max_sum=max(new_sum,max_sum)
    print("To megisto athroisma einai: ",max_sum)
def neoAthroisma(list,limit,new_sum,i,j):
    for l in range(j,i,-1):
        if (list[l]+new_sum)<=limit:
            new_sum=new_sum+list[l]
    return new_sum
mhkh=input("Dwse Mhkh:(px 1,3,6) ")
orio=int(input("Dwse orio: "))
mhkh_=(mhkh.split(","))
if len(mhkh_)==1:
    mhkh_=mhkh.split()
for i in range(len(mhkh_)):
    mhkh_[i]=int(mhkh_[i])
maxDistance(mhkh_,orio)