for i in range(3):
    name = input('UserName:')
    passwd = input('Password:')
    if name == 'root' and passwd =='12345':
        print('Login success!')
        break
    else:
        print('Login failed!')
        print('%d chance last' %(2-i))
print('Please try later!')