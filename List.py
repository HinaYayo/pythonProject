commuting = ['car', 'bicycle', 'motorcycle']
brands = ['Benz', 'GIANT', 'Honda']
guests = ["Tom", "John", "Mike", "Padma"]
for name in guests:
    print(name)
for name in guests:
    print(name + '，Good moning!')
for num in range(0, 3):
    print('I would like to own a ' + brands[num] + ' ' + commuting[num])
for guest in guests:
    print(guest + ", 我可以邀请你共进晚餐吗?")
print(guests[2] + "不能一起吃饭!" + "\n")
guests[2] = 'Bob'
for guest in guests:
    print(guest + ", 我可以邀请你共进晚餐吗? ")


