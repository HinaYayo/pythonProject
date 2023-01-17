num = int(input('Num:'))
start = 1
for i in range(1, 10):
    start = start*i
    print(i)
    print(start)
    print("--------")
print('%d的阶乘为：%d' % (num, start))
