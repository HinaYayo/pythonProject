for a in range(1, 10):
    for b in range(1,a+1):
        c=a*b
        print('{}x{}={}\t'.format(a, b, c), end='')
    print()