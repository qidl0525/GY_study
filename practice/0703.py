# def方法定义
# def level(a,b):    #方法定义，a b 形参
#     if (b == 0)
#         print("除数不能为0")
#     else:
#         print("商:",a // b , "余:",a % b)
#
# level(10 , 7)       #方法调用 10 ,7 实参
# level(7 ,17)
# level(10, 9)
# level(20,20)
# level(10 ,0)

# def shang_yu(a,b):
#     if (b == 0):
#         return None
#     else:
#         return (a // b , a%b)
# result = shang_yu(10,20) #按照位置传参
# result = shang_yu(b=15,a=20) #按照关键字传参，不用考虑传参次序

# if result is None:
#     print("参数错误")
# else:
#     print("商为:",result[0] ,",余数为:" , result[1])


#    定义关键字形参，给参数b设置默认值,m默认值放在后面（接口测试中有默认值、非必填项可以用）
# def shang_yu(a,b=2):
#     if (b == 0):
#         return None
#     else:
#         return (a // b , a%b)
# result = shang_yu(10,20) #按照位置传参
# result = shang_yu(2) #按照关键字传参，不用考虑传参次序

# if result is None:
#     print("参数错误")
# else:
#     print("商为:",result[0] ,",余数为:" , result[1])
#
# def sm(a,b=2):# 定义关键字形参，给参数b设置默认值,m默认值放在后面（接口测试中有默认值）
#     return a+b
# print(sm(2))


# c = 1,2,3,4
# a,*b =(1,2,3,4)
# print(b)
# def sum1(name,*args,**kwargs):   # *args接收动态位置传参，**kwargs 接收动态关键字参数
#     print(kwargs)
#     print(name)
#     s = 0
#     for i in args:
#         s +=i
#     return s
# print(sum1(1,2,3,4,5,6,7,8,9))
# print(sum1(name = "王大锤"))


# 面向对象编程
# class calc(): #类的定义
#     a = None
#     b = None
#     result = None
#     def input(self,c,d):
#         self.a = c
#         self.b = d
#     def sum(self):
#         self.result = self.a + self.b
#     def div(self):
#         self.result = self.a / self.b
#     def get_result(self):
#         print(self.result)
#
# c = calc() #类的实例化 C 对象
# c.input(10,20)
# c.sum()
# c.get_result()
# c.div()
# c.get_result()


# class calc(): #类的定义
#     result = None
#
#     def __init__(self,a,b):  #魔法函数，类实例化的时候调用，又称构造方法
#         self.a = a
#         self.b = b
#
#     def sum(self):
#         self.result = self.a + self.b
#
#     def div(self):
#         self.result = self.a / self.b
#
#     def get_result(self):
#         print(self.result)
#
# c = calc(29,39)
# c.sum()
# c.get_result()

# 九九乘法表

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j, "X",i,"=" ,i*j,end ="\t")
#     print()



# 冒泡排序

# l = [3,5,7,6,4,2,1]
#
#
#
# length = len(l) # 查询数据长度
# print(len(l))

# for i in range(length-1,0,-1): #外层循环确定排好序的数据下标
#     for j in range(0,i): #遍历未排好序的列表
#         if (l[j] > l[j+1]):  #判断相邻两个数据，若前一个大于后一个，则交换两个数据的位置
#             l[j],l[j+1] = l[j+1],l[j]
# print(l)


# print(len(l))
# for i in range(length-1,0,-1): #外层循环确定排好序的数据下标
#     for j in range(i): #遍历未排好序的列表
#         if (l[j] < l[j+1]):  #判断相邻两个数据，若前一个大于后一个，则交换两个数据的位置
#             l[j],l[j+1] = l[j+1],l[j]
# print(l)



# 冒泡排序
# l = [0,3,6,8,9,10,5,4,2,1]
# length = len(l)
# print(length)
#
# for i in range(length-1,0,-1):
#     for j in range(0,i):
#         if l[j]>l[j+1]:
#             l[j],l[j+1] = l[j+1],l[j]
# print(l)

# 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,'X',i, '=',i*j,end = '\t')
#
#     print()


# 倒叙输出
# a= (1,2,3,4,5)
# print(a[::-1])

# b = "uujdiwueijijeklhljkhljk"
# print(b[::-1])

# 输入四位数，每位都加5，在倒序输出
a = input("请输入四位数字")
c = " "
print(c)
for i in a:
    b = str((int(i)+5)%10)
    c = c+b
print(c[::-1])
print(c)

# a = input("请输入4位")
# c=""
# for i in a :
#     b=str((int(i)+5)%10)
#     c=c+b
# print(c[::-1])
# print(c)

a = "我是0703的变量a"

def name():
    print("我是0703的name方法")

class Test():
    name = "我是0703中的Test类"



























