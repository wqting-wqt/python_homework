from random import* #导入random包
print("输入您的电话号码:")
seed(int(input()))#初始化随机数种子,默认值为当前系统时间
 str1 = 'ABCDEFGHIJ0123456789'
print("您的取件码是:")
for i in range(6):
    print(choice(str1),end='')#从序列类型,例如列表中随机返回一个元素,并输出结果
