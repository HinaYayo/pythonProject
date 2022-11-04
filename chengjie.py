num = int(input('Num:'))
start = 1
for i in range(1, num + 1):
    start = start*i
print('%d的阶乘为：%d' % (num, start))
