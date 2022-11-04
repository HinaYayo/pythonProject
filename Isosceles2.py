num=int(input('输入层数：'))
for i in range(1,num+1):
    for a in range(num-i):
        print('  ',end='')
    for b in range(2*i-1):
        print('*',end=' ')
    print()
