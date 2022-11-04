#if-elif-else语句
age = int(input('请输入你的年龄：'))    #input返回的是str类型,需要转化为int类型
print('你的年龄是：',str(age),'岁')
if  age < 0 :
    print('输入错误!')
elif age < 7 :
    print('你是婴幼儿！')
elif age < 13 :
    print('你是少儿！')
elif age < 18 :
    print('你是青少年！')
elif age < 46 :
    print('你是青年！')
elif age < 70:
    print('你是中年！')
else :
    print('你是老年！')
