list = [7,5,4,6,1,3,2]

for m in range(len(list) - 1):#len(list)列表长度
    for n in range(m + 1, len(list)):
        if list[m] > list[n]:
            temp = list[n]
            list[n] = list[m]
            list[m] = temp
print(list)
