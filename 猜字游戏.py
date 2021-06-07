gold=5000
print("金币:",gold)
import random
num = random.randint(1, 3)
i=15
while i>0:
    i=i-1
    number = input("请输入你猜测的数:")
    number = int(number)
    if number!=num:
        gold=gold-500
    else:
        gold=gold+3000
    if gold<=0:
        break
    if i==0:
        break
    if number > num:
        print("大了,金币扣除,当前金币为",gold)
    elif number < num:
        print("小了，金币扣除，当前金币为",gold)
    elif number == num:
        print("恭喜你猜中了，本次字符为", num,"金币增加,当前金币为",gold)
        break
    else:
        print("输入非法字符")