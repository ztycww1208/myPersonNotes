# Python

## 一、Python基础

### 1 Python简介

#### 1.1 Python起源

> Python的中文意思：`蟒蛇`
>
> Python是由 `吉多` 在1989年圣诞节发明的一个解释程序
>
> Python是一门 `解释型` 语言，运行前无需编译
>
> 相同功能的情况下，Python的代码量只有java的1/5左右
>
> 
>
> Python的版本
>
> Python2：最初发布于2001年 
>
> Python3：最初发布于2008年
>
> 格言： `Life is short， you need Python` （人生苦短，我用Python） 

#### 1.2 Python应用

> `自动化测试`
>
> web开发：豆瓣，知乎，YouTube
>
> 人工智能：语音助手，用户行为分析
>
> `云计算`：云服务器

#### 1.3 Python优势

> 开源，免费
>
> 简单，明确
>
> 可移植性强（Windows、macOS 、Linux）
>
> 扩展性强（丰富的库）

### 2 Python安装

#### 2.1 下载

官网地址：`https://www.python.org/`

#### 2.2 安装

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200809193429739.png" alt="image-20200809193429739" style="zoom:67%;" />

#### 2.3 验证Python

命令行中输入 Python ，如果现实版本号，则安装成功

### 3 Pycharm安装

#### 3.1 下载

官网地址：` https://www.jetbrains.com/ `

学习选择社区版

#### 3.2 安装

注意勾选创建桌面图标，其余默认

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200809193843234.png" alt="image-20200809193843234" style="zoom:67%;" />

#### 3.3 创建项目

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200809193915778.png" alt="image-20200809193915778" style="zoom:67%;" />

#### 3.4 设置快捷键

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200809193954000.png" alt="image-20200809193954000" style="zoom:67%;" />

#### 3.5 设置主题

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200809194013615.png" alt="image-20200809194013615" style="zoom:67%;" />

####  3.6 设置字体

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200809194030396.png" alt="image-20200809194030396" style="zoom:67%;" />

#### 3.7 设置解释器

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200809194054098.png" alt="image-20200809194054098" style="zoom:67%;" />

### 4.注释

#### 4.1 定义

> 注释是用来解释说明代码的作用的
>
> 注释是不会执行的

#### 4.2 单行注释

> 单行注释用` # `表示，单行注释只在一行内生效
>
> 单行注释可以写在代码后面，也可以单独写一行

#### 4.3 多行注释

> 多行注释用 `一对三单引号/三双引号` 表示
>
> 多行注释可以换行
>
> 多行注释有特殊用途（函数中的文档注释）

#### 4.4 注释快捷键

> 选中代码，` Ctrl + /`
>
> 再按一次即可取消注释

### 5 基础数据类型

```python
# 可以使用type查看数据类型
# 整数 int
print(type(1))
print(type(-1))
print(type(0))
# 浮点数 float
print(type(1.1))
print(type(-1.1))
print(type(0.0))
# 字符串 string
print(type("abc"))
print(type('abc'))
print(type("i'm ok"))
# 布尔值 bool
print(type(True))
print(type(False))
# 空值 None
print(type(None))
```

### 6 变量

#### 6.1 定义

> 1 变量是一个容器，可以存放任意类型的数据
>
> 2 变量实质上是存储在内存中的值
>
> 3 变量定义好后可以重复使用

#### 6.2 变量的命名规则

> `命名规范`：
>
> 1 只能使用数字，字母，下划线
>
> 2 不能用数字开头
>
> 3 区分大小写
>
> 4 不能使用系统关键字

>`推荐命名方式`：
>
>1  见名知意，使用具有意义的单词取名
>
>2  驼峰命名法
>
>​		大驼峰：每个单词首字母都大写，如：`FirstLove`
>
>​		小驼峰：从第二个单词开始首字母大写，如：`firstLove`
>
>3  使用下划线拼接，如 ：`first_love`

#### 6.3 变量的赋值方式

> `普通赋值`：把右边的数据赋给左边的变量名，如 num = 1
>
> `序列解包赋值`：在一行代码中同时给多个变量赋不同的值，变量名与值一一对应，如 num1, num2, num3 = 1, 2, 3
>
> `链式赋值`：在一行代码中同时给多个变量赋同一个值，如 name1 = name2 = name3 = "zhangsan" 

### 7 运算符

#### 7.1 基础运算符

```python
# 四则运算
print(1+2)
print(4-2)
print(1*2)
print(4/2)        # 在Python3中整数相除，结果是浮点数
print(int(4/2))   # 类型转换
# 特殊情况
print('老师'+'学生')  # 拼接字符串
print("老师"*10)  # 复制字符串

print(10//3)  # 取整数
print(10%3)   # 取余数
print(2**3)   # 幂
```

#### 7.2 复合运算符

> `num = num + 1`  等于 `num += 1`
>
> 所有基础运算符都可与写成`复合预算符`

#### 7.3 比较运算符

> `<`：小于
>
> `<=`：小于等于
>
> `>`：大于
>
> `>=`：大于等于
>
> `==`：等于
>
> `!=`：不等于

#### 7.4 逻辑运算符

> `and`:并
>
> `or`：或
>
> `not`：非
>
> `in（）`：范围，包括

#### 7.5 运算符的优先级

> 使用（）提升优先级



### 8 字符串

#### 8.1 字符串的定义

> 字符串由 `一对单引号/双引号/三单引号/三双引号` 包围

#### 8.2 字符串的特点

> 1  有序：有索引值
>
> 2  不可变

#### 8.3 字符串的取值

**`索引值`**

![image-20200809155648926](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200809155648926.png)

**`取单个值`**

语法：` 变量名[索引值] `

**`切片`**

> 语法：` 变量名[起始索引：结束索引：步长]`
>
> 注意：切片是左闭右开型，即表示包含开始不包含结束
>
> 起始索引：结束索引    的顺序是从做往右，不区分大小，比如string[-2: -1]

```python
string = "HelloWorld"
# 切片
print(string[0:3])  # 取出Hel
print(string[-2:-1])  # 取出ld
print(string[5:7])  # 取出Wo
print(string[:])    # 从头取到尾
print(string[::2])  # 从头取到尾，每隔两个取一个，包括本身
print(string[::3])  # 从头取到尾，每隔三个取一个，包括本身
print(string[::-1]) # 反转字符串
```

#### 8.4 转义字符

> 定义：用`\`加上一些字符来表示特殊键位
>
> 常见的转义字符：
>
> ​		换行：`\n`
>
> ​		制表符：`\t`
>
> 如何使转义字符不转义
>
> ​		方法1：在每个转义字符的斜线后面再加一个斜线
>
> ​		方法2：直接在整个转义字符前面加`r`  
>
> ​        `print(r'D:\n\t\tashikeji.txt')`

#### 8.5 输入字符串

> - 输入字符串使用`input("输入提示")`函数，可以从键盘输入数据
> - 注意：在Python3中，输入人和数据，都会被保存成`字符串`类型

#### 8.6 格式化填充

> - 字符串的格式化是指将字符串按照一定的格式打印或者填充
>
> - 字符串的格式化方法有如下两种：
>
>
> 方法一：`使用百分号格式化`
>
> 先用下面的占位符占好位置，再将值传入：
>
> `%s `：字符串
>
> `%d` ：整数
>
> `%f`：浮点数，若要指定精度，则为 `%.nf `，` n `是一个整数，保留几位就写数字几
>
> print("your personal messages is your name :%s, password =%s, age=%d, height=%.2f"`%`(username,password,age,height) )   //没有逗号，用`%`连接
>
> 方法二：`使用  .format函数格式化`
>
> 统一使用 `{ } `占位，无需考虑数据的类型   
>
> {}里面是  . format（）里面变量的索引值（`从0开始计`），可重复

```python
# 输入字符串
print("Welcome to my system~")
username = input("please input your name: ")
password = input ("please input your password: ")
age = int(input("please input your age :"))
height = float(input ("please input your height(m):"))

# 格式化填充   #百分号%格式化
print("your personal messages is your name :%s, password =%s, age=%d, height=%.2f"%(username,password,age,height) )

# 格式化填充   # .format 函数格式化   #推荐使用
print("your pesonal messages is your name :{0} ,password :{1},age:{2},height{3}".format(username ,password,age,height))
```

#### 8.7  字符串的常用方法

- 替换：`replace (旧值，新值)`

- 切割：`split (切割标志)`，返回列表

- 查找：`find（查找的字符）`，返回`第一个找到的字符`的索引值，`找不到返回 -1`


```python
# 字符串操作替换、切割、查找
string = 'hellowordhhhhh'
string1 = string.replace('h','H',1)     # 1 的位置代表替换几次
print(string1)

string2 = string.split('o',1)   # 1 代表切割几次
print(string2)

print(string.find('l'))
```



### 9 列表(list)

#### 9.1 列表的定义

- 列表是Python中的一种基础数据结构，由` [ ] `包围
- 列表中可以存放任意类型的数据，每个数据称作一个元素，元素之间用逗号隔开

#### 9.2 快速生成数字列表

- `list(range(起始值，结束值，步长))`
- 注意：range也是`左闭右开型`，即包含开始不包含结束

```python
# 定义列表
nums = []
print(type(nums))

# 生成一个1-100 的列表
nums2 = list(range(1,101))   # rnage 是左闭右开区间
print(nums2)
# 生成一个1-100 所有偶数列表
nums3 = list (range(2,101,2))
print(nums3)
# 生成一个1-100 所有奇数列表
nums4 = list(range(1,101,2))
print(nums4)
```

#### 9.3 列表的特点

- 有序：有索引值
- 可变：可以修改自身

#### 9.4 列表的取值

- 取单个值

```python
num = [1,2,3]
print (num[0])  # 取出1
```

- 嵌套取值

```python
# 嵌套取值
foods = [['湖南','小龙虾',['50元','100元']],['湖北','热干面',['5元','免费']],
         ['河南','烩面',['10元','20元']]]
print(foods[1][2][0])   # 取出5元
print(foods[0][2][1])   # 取出100元
```



#### 9.5 列表的常用方法

**1 增加**

- 追加：`append ( )`

- 插入：`insert （索引值，元素值）`

**2 删除**

- 删除指定索引的元素：	`pop（索引） `，**不填**索引`默认删除最后一个`
- 根据值删除指定的元素： `remove（元素值）`

```python
# 常用方法
# 增
num = [1,2,3]
num.append("a")                       # 追加
num.insert(0,"666")                    # 插入
num.insert(0,0)
print(num)
# 删
num.pop(0)                          #根据索引值删除元素，如果不填索引值，默认删除最后一个元素
num.remove("666")             # 根据元素值删除元素
print(num)
```

**3 修改**：先取值再重新赋值

**4 统计**：

- 长度（元素的个数）：` len（）`
- 最大值： `max（）`
- 最小值： `min（）`
- `注意`：`统计函数，参数写在括号里面，不是通过点调用`

**5 反转**：` reverse()`

```python
# 修改
num2 = [1,2,3,4]
num2[0]=100         # 先取值，再赋值
print(num2)
# 统计
print(len(num2))     # length 长度
print(max(num2))     # 最大值
print(min(num2))     # 最小值
# 反转
print(id(num2))
num2.reverse()
print(id(num2))
print(num2)
```

**6 排序**

- 从小到大： `sort ( )`
- 从大到小： `sort ( reverse = True ) `

```python
# 排序
num3 = [4,4,7,2,8,7,6]
num3.sort()
print(num3)
num3.sort(reverse=True)
print(num3)
```

### 10  元组（tuple）

#### 10.1 元组的定义

- 元组是Python中的一种基础数据结构，由` ( ) `包围
- 元组中可以存放任意类型的数据，每个数据称作一个元素，元素之间用逗号隔开
- `注意`：如果元组中`有且只有`一个元素，那么必须要`用逗号结尾`，否则不是元组

#### 10.2 元组的特点

- 有序
- 不可变

#### 10.3 元组与列表相互转换

```python
# 元组与列表之间的转换
num3 = (1,2,3,4)
num3 = list(num3)  # 需要修改元组时，先将元组转换成列表
num3.append(5)
num3 = tuple(num3)   # 修改完成后，再转换会元组
print(num3)
```

#### 10.4 元组的常用方法

```python
print(len(nums)) 
print(max(nums)) 
print(min(nums))
```

### 11 字典（dict）

#### 1  字典的定义

- 字典是Python中一种基础数据结构，由 `{ }` 包围
- 字典中的数据以`键值对`的形式存在，键值之间用`冒号`连接，每个键值对称作一个元素，元素间用`逗号`隔开
- `注意`：字典中的键`不能重复`，否则只会保留最后一个；`键不能是可变类型`(比如list)，否则会报错

#### 2  字典的特点

- 无序
- 可变

#### 3  字典的取值

```python
student = {"name":"zhangsan", "sex":"boy", "age":19} 
print(student["name"])                     # 通过键取值
```

#### 4. 字典的常用方法

- 根据键修改值 : `字典[键] = 值 `, 如果键值对不存在则自动添加
- 根据键删除键值对 : `pop( 键 )`
- 获取所有键 : `keys( )`
- 获取所有值 : `values( )`
- 获取所有键值对 : `items( )`

```python
print(student["name"])    # 通过键取值
student["sex"]="girl"     # 通过键修改值
student["phone_number"]=12345678901   # 通过键修改不存在的内容，会自动添加到字典中
print(student)

student.pop("sex")      # 通过键 删除 键值对
print(student)

print(student.keys() )     # 获取所有键   dict_keys  是对象不是列表
print(student.values())    # 获取所有值
print(stuednt.items())         # 获取所有键值对
```



### 12 条件语句（if）

#### 1  基础格式

```python
if  条件: 
    条件满足时做的事情1 
    条件满足时做的事情2 
    ... 
else:
    条件不满足时做的事情1 
    条件不满足时做的事情2 
    ...
```

#### 2  if 嵌套

#### 3  elif

格式

```python
if 条件1: 
    条件1满足时做的事情 
    ... 
elif 条件2: 
    条件2满足时做的事情 
    ... 
elif 条件3: 
    .... 
else:
    以上条件都不满足时做的事情
```

案例1:

```python
# BMI 计算器
# BMI = 体重/身高的平方
print("welcome to use the TS-BMI~")
weight = float(input("please input your weight(kg):"))
height = float(input("please input your height(m):"))
BMI = round(weight/(height**2),1)
print("your BMI is {0}".format(BMI))
if BMI<=18.4:
    print("you are so skinny~")
elif 18.5<=BMI<=23.9:
    print("you are in normal shape,please keeping~")
elif 24.0<=BMI<=27.9:
    print("you are overweiht！please pay attention to your diet~")
elif 28.0<=BMI:
    print("you are fat,please pay more attention to your diet and exercise!")
else:
    print("input error,pelease re-input~")
```

案例2：

```python
# 猜拳游戏
import random  # 导入随机数模块
print("欢迎来到猜拳游戏~")
player = int(input("石头请输入0\n剪刀请输入1\n布请输入2\n请输入您的出的："))
com = random.randint(0,2)
if (player==0 and com == 1)or(player == 1 and com == 2)or(player == 2 and com == 0):
    print("你赢了~")
elif player == com:
    print("平局！")
else:
    print("你输了~")
```

### 13  循环语句

#### 13.1  程序的执行方式

- 顺序执行
- 条件选择执行
- 循环执行

#### 13.2  while 循环

**格式**

```python
while 条件: 
    条件满足时重复做的事情
    ...
```

案例1：打印1-10 之间所有的整数

案例2：打印1-10之间所有偶数

**嵌套循环**



#### 13.3  for 循环（也叫 迭代）

1  格式

```python
for 临时变量 in 对象/序列:     # 只要是遍历对象都可以使用for...in 遍历
    循环体
```

2 怎么判断是可迭代对象

方法是通过`collections`模块的`Iterable`类型判断：

```python
from collections import Iterable

print(isinstance("abdddf",Iterable))
print(isinstance([23,356,"df","34"],Iterable))
```

3 如同java一样，使用下表循环：

Python内置的`enumerate`函数可以把一个list变成索引-元素对，这样就可以在`for`循环中同时迭代索引和元素本身：

```python
for key,value in enumerate(['a','c','c']):
    print(key,value)
```





案例

```python
# 遍历字典 student = {"name":"zs", "age":19}
for i in student.keys(): 
    print(i)
for i in student.values(): 
    print(i)
    
# 有一段数据：student = {"name":"zs", "age":19... ...}，请用你熟悉的编 程语言，将其输出成name=zs,age=19...
for k, v in student.items(): 
    print("{ }= { }". format ( k, v))
    
    
# 4. 斐波那契数列 # 从1开始，后面的数是前面两数之和
#  双层循环
# 生成24个斐波那契数列 a, b = 0, 1 nums = []
for i in range(24): 
    nums.append(b) 
    a, b = b, a+b       # 两个 变量相互交换
print(nums)

# 嵌套循环
# 打印九九表
for i in range(1, 10):
	for j in range(1, i+1): 
        	print("{}*{}={}".format(j,i,j*i), end="\t") 
        print()
```

### 14  函数

#### 14.1 函数的定义

- 函数是将具有独立功能的代码块封装成一个模块
- 函数定义好后，可以通过 `函数名()` 来调用
- 函数定义好后可以无限次、在不同文件中调用

#### 14.2  函数的格式

```python
def 函数名(): 
    代码块
```

#### 14.3  文档注释

- 文档注释是用来解释说明函数的作用
- 文档注释一般用`多行注释`来表示
- 使用` help() `可以查看函数的文档注释

#### 14.4  函数参数

- **形式参数：** 函数定义时的参数
- **实际参数：** 函数调用时传入的参数



#### 14.5  参数的传递方式

- **位置传递：**形参与实参按照位置关系一一对应
- **参数的默认值：**形参可以拥有默认值，有默认值的形参如果不传入实参则使用默认值，`有默认值的形参必须要放到没有默认值的形参的后面`，否则会报错
- **关键字传递：**通过指定形参名来传入值，可以不受位置关系的影响

```python
add(2, 9) # 位置传递 
add(b=10, a=12, c=1) # 关键字传递 
add(c=2, a=1) # 默认值
```

#### 14.6  函数的返回值

- 使用 `return` 将函数的执行结果返回给调用者
- 如果函数中没有` return` ，则返回值为空
- 函数一旦执行到 `return` 后，就`不会继续往下执行`

#### 14.7  全局变量和局部变量

- **局部变量：** 定义在`函数内部`的变量，只在函数内部生效
- **全局变量：** 定义在函数外部的变量，在`整个代码文件中生效`
- 可以使用 `global` 将局部变量声明成全局变量

### 15  异常处理

#### 15.1  捕获异常

程序在执行过程中如果出现了异常就会终止运行。如果希望程序暂时跳过这个异常然后继续往后执行，则需要捕获异常

**格式**：

```python
try:
    可能会出现异常的代码 
except Exception as e: 
    出现异常后执行的代码 
else:
    没有异常时执行的代码
finally: 
    无论是否有异常都会执行的代码
```



**案例**：

```python
print("程序开始执行了") 
name = 'xx' 
try:
    print(name) 
except Exception as e: 
    print("程序出现异常了，异常信息是：{}".format(e)) 
    print("tashi") 
else:
    print("一切ok~")
finally: 
    print("我始终都会执行") 
print("程序结束了")
```



#### 15.2 抛出异常

如果希望程序在指定的情况下停止运行，则可以抛出异常

**格式**：

```python
raise Exception(异常提示)
```



**案例**：

```python
# 要求用户输入一个大于100的整数，如果不是大于100就会报错 
print("程序开始了") 
num = int(input("请输入一个大于100的整数：")) 
if num>100: 
    print("成功") 
else:
    raise Exception("您的输入有误！") 
print("程序结束了")
```



### 16  模块

#### 16.1  导入模块

```python
import 模块名
from 文件/模块 import 函数
from 文件/模块 import *
```

#### 16.2  安装模块

**在线安装**

- 打开命令行，输入：` pip install `模块名 ，回车
- 查看所有已安装模块及版本号，输入 `pip list`

**本地安装**

- 首先，去官网下载好需要安装的模块的包，地址：` https://pypi.org/`
- 解压下载好的安装包，并且进入解压好的目录
- 在解压好的目录中，打开命令行（在当前位置打开命令行）
- 在命令行中输入：` python setup.py install `安装模块
- 查看所有已安装模块及版本号，输入 `pip list `



#### 16.3  常用模块

time

```python
import time 


# 获取当前时间 
print(time.ctime()) 
# 暂停/休眠 
time.sleep(2) 
# 获取当前时间，并且指定格式，如2020-08-14 14:04:01 year month day hour minute second
print(time.strftime("%Y/%m/%d %H:%M:%S"))
```

OS

```python
import os 


# 获取当前文件所在路径 
print(os.getcwd()) 
# 创建目录 
os.mkdir("tashi") 
# 删除目录 
os.rmdir("tashi") 
# 删除文件 
os.remove("Python基础（xxx）.png")
```

json

json数据和字典极为相似，`区别在于，json数据是字符串类型，大括号{}外面有一对单引号或双引号包裹`

json 里面只能用`双引号`

```python
import json 

student = '{"name":"zs", "age":18}' # json数据 

student_dict = json.loads(student) # str-->dict 

student_json = json.dumps(student_dict) # dict-->str(json)
```

### 17  文件操作

#### 1  **打开文件**

打开文件使用 `open（file，mode）` 函数，该函数参数定义如下：

- file：文件名，可以是包含路径的文件名
- mode：文件打开模式
  - r：只读模式，文件不存在则报错
  - w：写入模式，文件不存在可以自动创建，会覆盖原内容
  - a：追加模式，文件不存在可以自动创建

#### 2 **写入**

- 写入使用 `write()` 函数
- 注意只能写入字符串类型

#### 3  **读取**

1. 读取所有内容：` read（）`
2. 读取前n个字符：` read( n ) `，多次使用会从上次读取位置继续往后读取
3. 读取一行： `readline()` ，多次使用会从上次读取位置继续往后读取
4. 按行读取所有内容： `readlines()` ，`返回列表`



#### 4  **关闭文件** 

- `close（） `
- `closed `，判断文件是否关闭，已关闭返回 `True `，未关闭返回 `False `

#### 5  **中文处理**

如果在读写文件时，出现了中文乱码的问题，则可以在打开文件时指定编码格式为 `utf8 `

```python
f = open("hello.txt", 'a', encoding="utf-8") 
f.write("它石科技") 
f.close()
```

#### 6  **自动关闭文件** 

```python
with open("hello.txt", encoding="utf-8") as f: 
    print(f.read()) 
print(f.closed)
```

#### 7  **应用：文件备份** 

```python
# 输入需要备份的文件名
file = input("请输入需要备份的文件名：") 
# 新文件名 
new_file = file.replace(".", "-副本.") 
# dian = file.find(".") 
# new_file = file[:dian] + "-副本" + file[dian:] 
# 打开源文件 
with open(file, encoding="utf-8") as f: 
    res = f.read() 
# 创建新文件 
with open(new_file, 'w', encoding="utf-8") as f: 
    f.write(res)
```

### 18  面向对象

#### 1  面向过程与面向对象

- 面向过程：按照业务逻辑从上往下编写代码，所有步骤都要亲力亲为（制作过程）
- 面向对象：将数据与函数绑定到一起，定义成`类`，通过类生成`对象`，减少代码编写，提高开发效率



#### 2  类和对象

- 类：泛指一类事物
- 对象：单指某一个具体事物

#### 3  类的组成

- 类名：一类事物的总称
- 属性：生而具有的特征
- 行为：具备的功能

#### 4  定义类

```python
class Dog():     # 类名 最好使用 大驼峰
    # pass  #占位符
    # 属性
    def eat(self):
        print("狗正在吃东西~")
        
    def run(self):
        print("狗正在跑~")
xiaohei = Dog()  # 实例化一个叫xiaohei的Dog（）对象
xiaohei.eat()       # 实例对象调用类中的函数（方法）
xiaohei.run()
```



#### 5  初始化

```python
class Dog():     # 类名 最好使用 大驼峰
    # pass  #占位符
    # 属性
    def __init__(self,weight,color="黑色"):     # 初始化函数，会在类的实例化的时候自动执行，如果没有写，默认会执行，函数体是pass
        self.weight=weight
        self.weight=color
        
    def eat(self):
        print("{}的狗正在吃东西~".format(self.color))
        
    def run(self):
        print("{}斤的狗正在跑~".format(self.weight))
xiaohei = Dog()  # 实例化一个叫xiaohei的Dog（）对象
xiaohei.eat()       # 实例对象调用类中的函数（方法）
xiaohei.run()
```



#### 6  继承

如果一个类属于一个大类中的一个小类，则这个小类可以继承大类，小类叫子类，大类叫父类

子类继承父类后，有如下特点：

- 子类可以使用父类中的所有方法
- 子类可以修改父类中的方法（覆盖父类同名方法，优先执行子类中的方法）
- 子类可以新增父类中没有的方法

```python
class Dog():
    def __init__ (self,weight,color="黑色"):
        self.weight = weight
        self.color = color
    def eat(self):
        print("{}的狗正在吃东西~".format(self.color))
    def run(self):
        print("{}斤的狗正在跑~".format(self.weight))
# xiaohe = Dog(20)
# xiaohe.eat()
# xiaohe.run()

class HaShiQi(Dog):   # HaShiQi 继承了Dog（）类
    def chaijia(self):    # 子类中新增父类中没有的方法
        print("{}的哈士奇正在拆家".format(self.color))
    def eat(self):   # 子类定义一个与父类同名的函数，可以达到修改父类函数的效果
        print("{}的哈士奇在吃骨头".format(self.color))
xiaoha = HaShiQi(20)
xiaoha.eat()
xiaoha.chaijia()
```

