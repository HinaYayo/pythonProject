list1 = ['a', 'b', 1, 3, 9, 9, 'a']
list2 = []
for list in list1:
    if list not in list2:
        list2.append(list)
print(list2)