a=int(input('输入行数：'))
for i in range(a):
    for j in range(i,2*a-1-i):#i.max=a-1;2*a-1-i.mix=a+a-1-a-(a-1)=a
        print('*',end=' ')
    print()
    for k in range(0,1+i):
        print('  ',end='')