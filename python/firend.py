names=['赵1','钱2','孙3','李4']
cars=['BMW','honda','BYD','benz']
wants=['周5','吴6','郑7']
for i in names:
    print(i)
for i in range(0,4):
    print('早上好，',names[i])
for i in range(0,4):
    print(names[i]+'乘坐'+cars[i])
for i in wants:
    print(i+'我想请你吃晚饭。')
print(names[0]+'无法来赴约。')
print(wants[0]+'可以来。')
names[0]=wants[0]
for i in names:
    print(i)