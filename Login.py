user = 'wang'
password = '123456'
for i in range(3):
    user1 = str(input('输入用户名：'))
    password1 = str(input('输入密码：'))
    if user == user1 and password == password1:
        print('登陆成功。')
        break
    else:
        print('用户名或密码错误，请重新输入。')
        print('你还有{}次机会。'.format(2-i))
else:
    print('请稍后输入。')
