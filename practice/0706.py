#封装


# class aaa():
    # 变量
    # pub_res = "共有变量"
    # _pri_res = "私有变量1"
    # __pri_res = "私有变量2"
    #

    # 方法
    # def pub_funcation(self):
    #     print("公有方法")
    #
    # def _pri_funcation(self):
    #     print("私有方法1")
    #
    # def __pri_funcation(self):
    #     print("私有方法2")

# print(aaa.pub_res)
# print(aaa._pri_res)
# print(aaa.__pri_res) 这个是封装，无法调用的变量
# print(aaa.pub_funcation(""))
# print(aaa._pri_funcation(""))
# print(aaa.__pri_funcation())这个是封装，无法调用的方法


# 继承
# class Parent():
#     money = 10000000000
#     house = 100
#     __clothes = "裤子"
#
#     def shou_yi(self):
#         print("点石成金")
#
# class Child(Parent):
#     ai_hao = "花钱"
#     pass
#
# c = Child()
# print(c.ai_hao)
# print(c.house)
# print(c.money)
# c.shou_yi()

# 多态
# class Parent():
#     money = 10000000000
#     house = 100
#     __clothes = "裤子"
#
#     def shou_yi(self):
#         print("点石成金")
#
# class Child(Parent):
#
#     def shou_yi(self):
#         super().shou_yi()  #多态：一定是发生在子类和父类之间，必须重写父类的方法
#         print("影分身")
#     ai_hao = "花钱"
#     pass
#
# c = Child()
# print(c.ai_hao)
# print(c.house)
# print(c.money)
# c.shou_yi()

# class Parent():
#     money = 10000000000
#     house = 100
#     __clothes = "裤子"
#
#     # def __init__(self,a):
#     #     self.a = a
#
#     def shou_yi(self):
#         print("点石成金")
#
# class Child(Parent):
#
#     def shou_yi(self):
#         super().shou_yi()  #多态：一定是发生在子类和父类之间，必须重写父类的方法
#         print("影分身")
#     ai_hao = "花钱"
#     pass
#
# c = Child(123)
# print(c.ai_hao)
# print(c.house)
# print(c.money)
# c.shou_yi()


# # from ***import ****
# from practice.control import a as control_a
# from practice.control import name as control_name

# print(a)
# name()
# print(Test.name)


# a = "我是0706的变量a"
#
# def name():
#     print("我是0706的name方法")
#
# class Test():
#     name = "我是0706中的Test类"

# print()
# name()
# print(Test.name)

# print(control_a)
# print(control_a)


# 字符串、数字互转（字符串只能是数字）
# a = 123
# b = "456"
# print(int(b)+a)
# print(str(a)+b)


#元组、列表、集合、字符串相互转换
# t = (1,2,3,4,5,6,7,8,9)
# print(list(t))
# print(set(t))
#
# str = "eqweqdd214"
# print(list(str))
# print(set(str))
# print(tuple(str))

# 打开模式：r 读取，w 清空写入，a 追加写入，b,二进制写入
# s = """
# 海的女儿
# 他是谁
# 我告诉你
# 她叫
# 胡月梅
# """
# d = open("dpm.txt","w")
# d.write(s)
# d.close()
#
# d = open("dpm.txt","r")
# # print(d.read()) #全部读取
# print(d.read(5))# 读取5个字符
# print(d.readline()) #读取一行
# print(d.readlines())# 读取全部行




# 字符串的截取
# a = "abcdefghijk"
# print(a[0])
# print(a[-1])
# print(a[1:])


# 猜数字游戏
# flag = True
# import random
# a=random.randint(0,100)
# while flag:
#    b=int(input('请输入数字'))
#    if b>a :
#       print('大了')
#    elif(b<a):
#       print('小了')
#    else:
#       print('猜对了')
#       flag = False



# 数据切片
# l = "eqdadfa,qdfvsdter,rqweq"
# print(l.split(","))
#
# with open("dpm.txt","r") as d: #with 使用一个上下文管理器
#     lines = d.readlines()
#     print(lines)
#     for i in lines:
#         print(i.replace("\n",""),end="") #print 默认带一个换行





# 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,'X',i, '=',i*j,end = '\t')
#
#     print()
#
# for i in range(1,10):
#     for j in range(1,i + 1):
#         print("%d x %d = %d"%(j,i,i*j),end="\t")
#     print()
#
#     for i in range(1, 10):
#         for j in range(1, i + 1):
#             print("{} x {} = {}".format(j,i,i*j),end="\t")
#         print()




# 列表的操作
# l = [0,1,2,3,4,5,6,7,8,9]
# l[0] = 9
# print(l)
# l[2:5] = [5,7]
# # print(l[2:5,])
# print(l)
# print(l[:2])

# 新增数据
# l = []
# l.append("果芽")
# print(l)
#
# ll = []
# ll.extend(("果芽","2006A","测试基础"))#可以是元组/列表/集合
# print(ll)
# ll.insert(2,"初级班") #根据下角标插入数据
# print(ll)
#
# print(ll.pop(3)) #根据角标删除
# print(ll)
#
# ll.remove("果芽") #根据具体数据删除
# print(ll)
#
# ll.clear()#清空表格
# print(ll)

#
# 字典的操作
# d = {"name":"小明","age":18,"sex":"男"}
#
# for key in d:      #只能遍历key值
#     print(d[key])
#
# d.items()          #对字典全部遍历，先转成items，再用for循环
# print(d.items())
#
# for k,v in d.items():
#     print(k,v)
#
# # 修改值
# d["name"] = "小红"
# print(d)

# 增加一对值
# d["addr"] = "上海市浦东新区"
# print(d)


# 增加多对值
# e = {"name":"小刚"}
# e.update(sex = "男",age = 18)   #key值不加引号，只有字符串（汉字）才会带
# print(e)
#
# t = {"手机号":"18242370123","addr":"上海市闵行区"}  # 两个集合也可以拼接
# e.update(t)
# print(e)



l = ["b",4,5,78,90]
for b in l:
    print(b)

a = [0,1,2,3,4,5,6,7,8,9]
for i in a:
	print(i)