# l = ["果芽","百度","阿里","腾讯","B站"]
# if ("果芽" in l):
#     print("合作方")
# else:
#     print("非合作方")
#
#
# a = 59
# if (0 <= a <= 59):
#     print("不及格")
# if (60 <= a <= 70):
#     print("及格")
# if (71 <= a <= 80):
#     print("良好")
# if (81 <= a <= 100):
#     print("优秀")
#
# b = 80.5
# if (0 <= b and b <= 59):
#     print("不及格")
# if (60 <= b and b <= 70):
#     print("及格")
# if (71 <= b and b <= 80):
#     print("良好")
# if (81 <= b and b <= 100):
#     print("优秀")
#
# # l = {0<=a<=59,60<=a<=70,71<=a<=80,81<=a<=100}
# # print l(1)
# b = 60
# if (0 <= b and b <= 59):
#     print("不及格")
# elif (60 <= b and b <= 70):
#     print("及格")
# elif (71 <= b and b <= 80):
#     print("良好")
# elif (81 <= b and b <= 100):
#     print("优秀")
# else:
#     print("请输入正确成绩")
#
# x = 30
#
# score = [60,70,88,95,100,25,40] for循环属于精确循环
# for b in score:
#     if (0 <= b and b <= 59):
#         print("不及格")
#     elif (60 <= b and b <= 70):
#         print("及格")
#     elif (71 <= b and b <= 80):
#         print("良好")
#     elif (81 <= b and b <= 100):
#         print("优秀")
#     else:
#         print("请输入正确成绩")
#
# # 100以内数的和（不包括100）
# s = 0
# for i in range(100):
#     s = s + i
# print(s)
#
#
# 求出10的阶乘 for循环属于精确循环
# a = 1
# for i in range(10,0,-1):
#     # a = a*i
#     a *= i
# print(a)

# 猜数字
# flag = True
# while flag:
#     b = 800
#     i = int(input("请输入数字"))
#     if i < b:
#         print("小了")
#     elif i > b:
#         print("大了")
#     else:
#         print("猜对了")
#         flag = False


# 100以内可以被3整除的数字
# for i in range(1,100 ):
#     if (i % 3 != 0):
#         continue
#     print(i)

#  定义一个求两个数商和余数的方法d
# def方法定义
# def level(a,b):    #方法定义
#     if (b == 0)
#         print("除数不能为0")
#     else:
#         print("商:",a // b , "余:",a % b)
#
# level(10 , 7)       #方法调用
# level(7 ,17)
# level(10, 9)
# level(20,20)
# level(10 ,0)

# def shang_yu(a,b):
# #     if (b == 0):
# #         return None
# #     else:
# #         return (a // b , a%b)
# # result = shang_yu(10,20)
# #
# # if result is None:
# #     print("参数错误")
# # else:
# #     print("商为:",result[0] ,",余数为:" , result[1])


# 九九乘法表

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j, "X",i,"=" ,i*j,end ="\t")
#     print()

#
# for a in  range(1,10):
#     for b in range(1,)
#     print(a)




def name():
    print("我是control的name方法")

class Test():
    name = "我是comtrol中的Test类"

a = "我是control的变量a"