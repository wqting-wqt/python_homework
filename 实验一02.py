#生日悖论分析
#导入random包
#通过集合的无重复性来判断生日是否有重复的
# n：班级的人数
# num: 中间计数器，有重复生日的次数
# x： 随机数种子x
# a: 空集合
import random
x = 3
print("请输入需要测试的次数：")
n =  input() 	
num = 0   		
a = []
random.seed(x)
print("重复的比率如下")
for i in range(int(n)):
    for j in range(23):
        a.append(random.randint(1,365))
    if len(a) == len(set(a)):
        pass
    else:
        num+=1
    a = []
print("rate={:.2f}".format(num/int(n)))




