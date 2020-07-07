# -*- coding:utf-8 -*-


#
# def div(a,b):
#     try:
#         return  a/b
#     except:
#         return
#
# print(div(10,0))


# try:
#     f = open("bbbb.txt",'r')
#     print(f.read())
#     f.close()
# except:
#     print("文件不存在")
#
# print("文件不存在")

class CustomException(Exception):
    def __init__(self,value = "值不能为0"):
        self.value = value

    def __str__(self):
        return  self.value

a = 0

try:
    if a == 0:
        print("a = {} 触发异常".format(a))
        raise CustomException("值不能为0")
    print("a = {} 触发异常".format(a))
except CustomException as e:
    print(e)