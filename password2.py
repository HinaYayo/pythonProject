name='root'
password='123'
for i in range(3):
    name1=str(input('输入用户名：'))
    password1=str(input('输入密码：'))
    if name==name1 and password==password1:
        print('登录成功。')
        break
    else:
        print('账号或密码错误，请重新输入。')
        print('您还有{}次机会。'.format(2-i))
        #if i==2:
            #print('结束。')
else:
    print('jieshu')



