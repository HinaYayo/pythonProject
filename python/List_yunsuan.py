list1 = [1,2,3,4,5,6,7]
newlist=[]
for list in list1:
    if list%2==1:
        newlist.append(list)
    else:
        list=list*2
        newlist.append((list))
print(newlist)
