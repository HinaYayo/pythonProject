num=int(input('输入层数：'))
for i in range(num):
    for j in range(i,2*num-1-i):#i.max=a-1;2*a-1-i.mix=a+a-1-a-(a-1)=a
        print('*',end=' ')
    print()
    for k in range(0,1+i):
        print('  ',end='')
for y in range(2,num+1):
    for a in range(num-y):
        print('  ',end='')
    for b in range(2*y-1):
        print('*',end=' ')
    print()
