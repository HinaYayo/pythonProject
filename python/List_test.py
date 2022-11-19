lists=[2,3,5,4,6,1,7]#7,6,5,4,3,2,1
newlists=[]
for i in range(len(lists)):
    for n in range(i,len(lists)):
        if lists[i]<lists[n]:
            num=lists[i]
            lists[i]=lists[n]
            lists[n]=num
print(lists)



