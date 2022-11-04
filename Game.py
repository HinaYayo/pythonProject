import random

min = int(input("输入最小值："))
max = int(input("输入最大值："))
num = random.randint(min, max)
if max > min:
    for i in range(10):
        guess = int(input("请输入数字："))
        if guess > num:
            print("大了")
        elif guess < num:
            print("小了")
        else:
            print("答对了，你用了" + str(i + 1) + '次。')
            break
    i = i + 1
    if i == 10:
        print("你输了。")
else:
  print('数值输入错误。')
