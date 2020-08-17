# 1. 输入任意三个整数，将它们从小到大排列并输出
# nums=[]
# for i in range(3):
#     nums.insert(i,int(input("请输入3个整数，第{}个数：".format(i+1))))
# nums.sort()
# print("您输入的三个数字从小到大的顺序是：")
# for i in nums:
#     print(i,end='\t')
# 2. 求任意字符串的长度
# num = input("请输入任意字符串：")
# print("字符串的长度是："+str(len(num)))
# 3. 定义一个函数，输入任意三个学生的姓名，然后写入到 D 盘根目录下的test.txt 中
# def input_name():
#     with open(r"D:\student_name.txt","w",encoding="utf-8") as f:
#         for i in range(3):
#             name = input("请输入第{}个学生姓名：".format(i+1))
#             f.write(name+"\n")
#     with open(r"D:\student_name.txt","r",encoding="utf-8") as f:
#         print("您输入的学生姓名为：")
#         return f.read()
# print(input_name())
# 4. 定义一个函数，求 1-n 之间的所有偶数和，默认计算 1-10
# def oushu_sum(n=10):
#     sum = 0
#     for i in range(2,n+1,2):
#         sum+=i
#     return print("1-{}之间的所有偶数和为{}".format(n,sum))
# oushu_sum(20)
# 5. 定义一个函数，可以将任意两个字符串拼接到一起
# def connect_str(string1,string2):
#     string = string1+string2
#     return string
# string1=input("请输入第一个字符串：")
# string2=input("请输入第二个字符串：")
# print(connect_str(string1,string2))
# 6. 输入任意三个整数，计算前两数之和与第三数的乘积
# num=[]
# for i in range(3):
#     num.append(int(input("请输入第{}个整数:".format(i+1))))
# print("({}+{})x{}={}".format(num[0],num[1],num[2],(num[0]+num[1])*num[2]))
# 7. 写出Python的优势，三个以上
#1.开源，免费  2.简单明确  3.可移植性强  4.扩展性强
# 8. 学习Python可以用来干什么
# 1.自动化测试   2.web开发   3.人工智能   4.云计算
# 9. 现有 str="ABEFG" ，如何取出 FG 并打印
# str = "ABEFG"
# str_new=str[-2:]
# print(str_new)
# 10. 编写一个小程序：让用户输入任意的用户名与密码，然后将他输入的用户名与密码打印出来，
# 如用户输入 abc/123 ，则打印您输入的用户名是 abc ，密码是 123
# str = input("请输入用户名和密码格式为（用户名/密码）：")
# message = str.split("/")
# print("您输入的用户名为:{},密码为:{}".format(message[0],message[1]))
# 11. 字符串有哪些特点
# 1.有序  2 不可变
# 12. 字符串在使用 % 格式化时，要不要考虑数据类型，若要，如何考虑？
#  需要考虑数据类型，如：%d 填充int  %f  填充float   %s  填充字符串   等等
# 13. 写出Python中常见的基础数据类型
#  int（整数）  float（浮点数）   string（字符串）   None（空）    bool（布尔值）
# 14. 现有 a = (3>=8) and (2!=2) ，则 a 的值是？
# a = (3>=8)and(2!=2)
# print(a)   # 结果为False
# 15. （判断题）Python是一门编译型语言，运行前需要将代码编译成机器码再执行
#      Python 是一门解释型语言,运行前无需编译
# 16. 在Python中，想要打开 E 盘下的 t 目录下的 a.doc 文件，在表示该文件的路径时需要注意什么？
#   注意：转义字符，解决办法：1.在字符前加 r ，2.在每个反斜杠后再加一个反斜杠
# 17. 使用while循环写出九九乘法表
# x=1
# while x<=9:
#     y=1
#     while y<=x:
#         print("{}x{}={}".format(x,y,x*y),end='\t')
#         y+=1
#     x+=1
#     print()
# 18. 生成一个包含1-1000之间的所有奇数的列表
# num=[]
# for i in range(1,1000):
#     if i%2!=0:
#         num.append(i)
# print(num)
# 19. 现有 nums=[2, 5, 7] ，如何在该数据最后插入一个数字 9 ，
# 如何在2前面插入一个数字 0
# nums =[2,5,7]
# nums.append(9)
# nums.insert(0,0)
# 20. 如何对一个数字列表从小到大以及从大到小排序
# 从小到大：sort()     从大到小：sort(reverse=True)
# 21. 元组与列表有啥区别
#  元组 有序不可变，  列表有序可变
# 22. 现有 employee={"id":1, "salary":2000} 用来储存员工的一些基本信息，
# 如何在该数据中插入员工的手机号，号码自定义
# employee["phone"]="12345678900"
# 23. 编写一个小程序：设计一个登录程序，需要用户输入用户名与密码，用户名/密
# 码是： Alexx/123 则登录成功，否则登录失败
# print("欢迎进入登录小程序~")
# name=input("请输入用户名：")
# password=input("请输入密码：")
# if name =="Alexx" and password=="123":
#     print("登录成功")
# else:
#     print("登录失败")
# 24. 写出程序的三大执行方式
#  1顺序执行   2选择执行   3循环执行
# 25. 如何打印十次 中国很强
# print("中国很强"*10)
# 26. 现有 nums=(1,2,3,4) ，如何在该数据最后插入数字 5
# nums=(1,2,3,4)
# nums = list(nums)
# nums.append(5)
# nums = tuple(nums)
# 27. 使用 for 循环写出九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{}x{}={}".format(i,j,i*j),end="\t")
#     print()
# 28. 什么是文档注释，用来干什么
#  1 用来解释函数的作用 2 一般用三单或三双引号  3 可以使用help()查看函数的文档注释
# 29. 函数中的参数有哪些传递方式
#    位置传参，关键字传参，默认值参数
# 30. 为什么要捕获异常，捕获异常的格式是？
#  捕获可能会出现异常的代码块，以保证程序正常运行
#  格式：
# try:
#     可能出现问题的代码块
# except Exception as e:
#     出现异常运行的代码块
# else:
#     没有异常会运行的代码块
# finally:
#     不管是否有异常都会运行的代码块
# 31. 在python中如何快速安装一个第三方模块
#  pip install 模块名
# 32. 什么是函数的返回值，有什么特点
#  1返回函数执行结果给调用者   2没有return的函数返回为空  3return后面的语句，函数不再执行
# 33. 生成一个包含 24 个斐波那契数列的列表
# a,b = 0,1
# num =[]
# for i in range(24):
#     num.append(b)
#     a,b = b,a+b
# print(num)
# 34. 现有 a=‘{"a":1, "b":2}’ ，如何将其转为字典
# import json
# a='{"a":1, "b":2}'
# a_dict = json.loads(a)
# print(type(a_dict))
# print(a_dict)
# 35. 如何暂停代码 3 秒钟
# sleep(3)
# 36. 怎么读取文件中的所有内容，并返回一个列表
# readlines()
# 37. 什么是继承，有什么特点
#  子类能使用父类中的所有属性和方法，子类中与父类的同名方法或属性，可以修改 ，子类可以自定义不同于父类的属性和方法
# 38. 现有一个文本文件 f 如下，执行 f.read(3) ，得到什么
# 如果是第一次，读取f文件中的三个字符，如果是有历史记录，则从上一次记录起的三个字符
# 39. 文件操作后如何自动关闭文件
# with open("文件名","mode") as f:
# 40. 面向对象中，类的组成部分有哪些
#   类名，属性，函数
# 41. 定义一个类 class login() ，找出该代码中的错误并修正
#  1变量名首字母最好大写，2没有冒号  3 没有属性  4 没有定义函数
# class Login():
#     def __init__(self):
#         pass
#     def toindex(self):
#         pass
# 42. 类的初始化使用哪个函数（方法）
#  __init__(self)
# 43. 现有 a = “tashi” ，请将字符 t 改成 T
# a = "tashi"
# b=a.replace("t","T")
# print(b)
# 44. 现有 True = “123” - “1” ，找出其中的错误，并修正
#   1True不能作为变量名 2字符串不能直接相减
#   num = int("123")-int("1")
# 45. 现有 num = True - (False - True) ，请问 num 的值是多少
# num = True - (False - True)
# print(num)  # 结果为2
# 46. 现有 hi = “hi001” ，如何取出 1 ，如何取出 001
# hi = "hi001"
# print(hi[-1])
# print(hi[-3:])
# 47. 写出所有已学的字符串格式化的占位符
# %f  %d %s
# 48. 写出变量的命名规范
# 1只能使用数字、字母和下划线
# 2区分大小写
# 3数字不能作为开头
# 4不能使用系统关键字作为变量名
# 49. 变量的赋值有哪些方法
# 1普通赋值
# 2序列解包赋值
# 3链式赋值
# 50. 如何反转一个列表
# reverse()
# 51. 以下选项中，属于可变类型的有  B,C
# A. () B. [1] C.(1) D.“abc”
# 52. 现有 a = [["A"，1], ["B"，2]] ，如何取出 2
#a[1][1]
# 53. 如何获取字典中的所有键以及所有值
#  所有键 keys()         所有值 values()
# 54. 用一行代码生成一个包含1-10之间所有偶数的列表
#num = range(1,11,2)
# 55. 现有 a = {"id":01, "price":3999.9} ，该数据是编号为01，价格为
# 3999.9元华为P30手机的信息，请在该数据中，插入该手机的名称
# a["name"]="华为P30"
# 56. 定义一个函数：计算 1-n 之间的所有 5 的倍数之和，默认计算 1-100 （ n 是 一个整数）
# def five_num(n=100):
#     sum=0
#     for i in range(1,100+1):
#         if i%5==0:
#             sum = sum+i
#     return sum
# n=int(input("请输入一个整数："))
# print("1-{}的所有5的倍数之和为：{}".format(n,five_num(n)))
# 57. 假定一对大兔子每月能生一对小兔子，且每对新生的小兔子经过两个月可以长
# 成一对大兔子,具备繁殖能力，如果不发生死亡，且每次均生下一雌一雄，问两
# 年后共有多少对兔子？
# year=int(input("请输入多少年："))
# month=year*12
# datu=1
# xiaotu=0
# sum =0
# for i in range(1,month+1):
#     if i%2!=0:
#         datu+=0
#         xiaotu+=1
#     else:
#         datu2=datu
#         datu=datu+xiaotu
#         xiaotu =datu2
# sum =datu+xiaotu
# print("{}年共有{}只兔子".format(year,sum))
# 58. 现有 student = {"name":"zs", "age":18, ...} ，
# 请将该数据输出成 name=zs,age=18... （注意省略号）
# student = {"name":"zs", "age":18}
# for i in student.keys():
#     print("{}={}".format(i,student[i]))
# 59. 什么是局部变量，有什么特点，如何将局部变量声明成全局变量
# 局部变量是定义在函数内部的变量，可以使用global 变量名 将局部变量变成全局变量
# 60. 定义一个函数，可以判断任意的字符串中有几个数字
# def str_num():
#     string = input("请输入一个字符串：")
#     string1 = list(string)
#     sum = 0
#     for i in string1:
#         if i in "1234567890":
#             sum+=1
#     print("您输入的字符串{}，一共包含{}个数字".format(string, sum))
# str_num()
# 61. 定义一个函数，将用户输入的用户名与密码写入到 D 盘根目录下 data.txt 中
# def input_user():
#     name=input("请输入用户名：")
#     password=input("请输入密码：")
#     with open(r"D:\data.txt","w",encoding="utf-8") as f:
#         f.write("用户名："+name+"\n"+"密码："+password+"\n")
# input_user()
# with open(r"D:\data.txt","r",encoding="utf-8") as f:
#     print(f.read())
# 62. 导入模块有哪几种方法
# 1 import 模块名   2 from 模块名 import 函数名    3form 模块名 import *
# 63. 如何使代码暂停 0.5 秒
# import time
# time.sleep(0.5)
# 64. 现有 a = ‘{"A":1, "B":2}’ ，如何快速将 2 修改成 4
# import json
#
# a = '{"A":1, "B":2}'
# a=json.loads(a)
# a["B"]=4
# a=json.dumps(a)
# 65. 如何将任意一个列表的所有数据复制到另外一个列表（禁止赋值）
# num=[1,2,5,7,8,2,5]
# num_new=[]
# for i in num:
#     num_new.append(i)
# 66. 任意输入一个字符串，如果字符串中包含 tashi ，则将该字符串写入到
# tashi.txt 中，并自动关闭该文件
# string = input("请输入一个字符串：")
# if "tashi" in string:
#     with open("tashi.txt","a",encoding="utf-8") as f:
#         f.write(string)
# 67. 编写一个电费计算器程序，当用电量在 100 度及以下时，收费 1 元/度；当超
# 过 100 度，则收费 1.5 元/度
# print("这是一个电费计算程序~")
# electric=float(input("请输入你的用电量(度)："))
# dianprice = 0
# if electric<=100:
#     dianprice=electric*1
# else:
#     dianprice=electric*1.5
# print("您的电费是：{}".format(dianprice))
#68.如何主动抛出一个异常
# raise Exception
# 69. 计算 1+2-3+4-5... ...100 的值
# sum =1
# for i in range(2,101):
#     if i%2==0:
#         sum+=i
#     else:
#         sum-=i
# print(sum)
# 70. 将任意列表的元素值按照相反的顺序打印出来
# num=[1,5,9,5,3,6,3,2]
# print(num[::-1])
# num.reverse()
# print(num)
# 71. 如何将一个列表中的重复值去除，如 [1, 2, 2] 去重后得到 [1, 2]
# num = [3,6,8,3,5,4,5]
# num=list(set(num))
# nums=[]
# for i in num:
#     if i not in nums:
#         nums.append(i)
# print(nums)