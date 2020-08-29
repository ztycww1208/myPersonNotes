# Mysql

## 1 概念

### 1.1 数据库的定义

- 数据库是按照「数据结构」来组织，存储，管理数据的仓库
- 相对于传统的数据存储方式（图书，excel表格... ...）会更加利于分享，查询，管理

### 1.2 关系型数据库

- RDBMS（Relational DataBase Management System，关系型数据库管理系统）
- 关系型数据库，采用关系模型（一对一，多对一，一对多... ....）来组织、存储数据库

### 1.3 排名与分类

`分类`:

> **关系型：**
>
> \- `Oracle`：甲骨文公司开发，收费，一般用于大型项目。（银行，电信... ...） 
>
> 
>
> \- `MySQL`：甲骨文公司收购sun而来，开源，免费。在web项目中广泛使用 
>
> 
>
> \- `Microsoft SQL Server`：微软研发的，只在微软项目中使用 
>
> 
>
> \-`DB2`:大型数据库,处理海量数据的能力较强,一般用于银行或者金融行业,收费. 
>
> 
>
> oracle:大型数据库 
>
> mysql:小型数据库 
>
> sqlserver:中大型 
>
> DB2:大型数据库 
>
> 备注:数据库的处理能力取决于处理的数据的数量和DBA的能力.

> **非关系型：**
>
> \- `Redis：`高性能的缓存数据库 
>
> \- `SQLite：`轻量级数据库，一般用移动端 
>
> \- `MongoDB`

「关系型数据库的`核心元素`」：

- 数据仓库：常常被简称数据库，一个数据库系统可以有多个数据仓库
- 数据表：一个数据仓库可以有多个数据表
- 数据列：列数据，称作字段
- 数据行：一条数据

### 1.4 Mysql的特点

- 支持多平台（Windows，Linux，macOS）
- 免费，开源（但是目前已经出了收费版本）
- 支持sql语法
- 是学习数据库的首选

## 2 安装Mysql

> 1.找到D:\Tools_V9.7.3\U.环境搭建\window\阿木虚拟机.rar ---右键---解压到当前文件夹
>
> 2.进入解压出来的阿木虚拟机文件夹,找到阿木虚拟机.vmx----双击---开启此虚拟机---我已复制该虚拟机--确定---等待windows开机---开机后提示立即重新启动---点击立即重新启动
>
> 3.将解压工具和mysql的安装包复制到阿木虚拟机
>
> 4.在阿木虚拟机里面安装解压工具:双击--安装--完成--确定.弹出的文件夹关闭
>
> 5.在阿木虚拟机里面选择mysql安装包---右键--解压到当前文件夹
>
> 6.双击解压出来的mysql安装软件--双击--接受协议--下一步,一直到 fifinish
>
> 7.设置mysql服务器--详见截图
>
> 验证mysql安装是否ok:
>
> > 1.win +r --cmd ---输入:mysql -uroot -p ---Enter键--输入密
> >
> > 码:123456---Enter键----出现mysql> 表示ok
> >
> > 2.退出:exit
>
> window安装mysql之后无法远程连接的 报1130错误
>
> 解决方法：在服务器命令行输入
>
> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123456' WITH GRANT OPTION;

## 3 用户的操作

### 3.1 创建用户

```mysql
create   user    '用户名'@'ip地址'    identified    by    '密码';
```

> 解释: 
>
> 1.用户名,ip地址,密码 都要用英文的单引号引起来 ，也可以是 `%`代表所有的ip地址
>
> 2.句子结尾用英文的分号; 表示结束 
>
> 3.每一个单词之间有空格

### 3.2 查看用户

```mysql
select   *   from   user;
```

### 3.3 用户赋权

```mysql
grant   权限1,权限2   on   *.*   to   '用户名'@'ip地址';
```

> 权限:create, insert ,delete,update,select,drop等 
>
> 第一个*表示数据库,泛指所有, 
>
> 第二个*指数据库里面所有的表 
>
> to :表示给与的对象

### 3.4 查看权限

```mysql
show   grants   for   '用户名'@'ip地址';
```

### 3.5 收回权限

```mysql
revoke   权限1,权限2   on   *.*   from   '用户名'@'ip地址';
```

### 3.6 修改用户名

```mysql
rename   user   '旧用户名'@'ip地址'   to   '新用户名'@'ip地址';
```

### 3.7 修改用户密码

```mysql
set   password   for   '用户名'@'ip地址'=password('新密码');
```

### 3.8 删除用户

```mysql
drop   user   '用户名'@'ip地址';
```

### 3.9 创建可以远程连接的用户

1.在navicate创建用户create user 'abc'@'%' identifified by 'tashi123';       --创建abc适用于任何ip

2.在服务器命令行	用`mysql -uroot -p `登录，      --直接加密码  mysql  -uroot   -p123456    

​								执行赋权：`grant  all  PRIVILEGES  on  * . *  to   'abc'@'%';`

3.刷新权限：`flush  privileges;`

4.可以在navicate上远程登录

> mysql  -uroot  -p123456  -h192.168.0.153  远程连接其他ip的数据库



## 4 常见的数据类型和约束

### 4.1 常用的数据类型

**整数（int）**：有符号范围（-2147483 648，2147483 647），无符号（0，4294967295）

​						int类型不声明则默认为有符号,即上下限是固定的,不管int(1)还是int(11),上下限都是（-2147483 648， 

​						2147483 647）

**小数（decimal）**：如decimal(5, 2)表示该小数一共有5位，小数占2位，整数占3位

**字符串（varchar）**：范围（0-65535），如varchar（3），表示最多可以存3个字符，中文与字母都是占一个

**char(n) :**定长字符类型,字符长度固定为n,不足长度的用空格补齐---浪费资源

**日期时间（datetime）**：如2020-04-02 15:04:05

**日期（date）**：如2020-04-02



> 对于INT型，MySQL支持指定显示宽度
> 例如：
> int(5)：表示如果数值宽度小于5位，则填满宽度，保证总宽度为5位。
> 默认为int(11)，配合zerofill可以看到效果。

### 4.2 常用的约束

**主键（primary key）**：物理存储上的顺序，用来标识唯一的一行数据,非空

**非空（not null）**：此字段不允许填空值（不能不填）

**唯一（unique）**：此字段的值不允许重复

**默认值（default）**：此字段可以不填，不填时使用默认值

**外键（foreign key）**：维护两张表之间的关系（一张表的字段是另外一张表的主键）【了解】



## 5 数据表的操作

### 5.1创建表

```mysql
create table 表名(
    字段名1 类型 约束, 
    字段名2 类型 约束,
    ... ... 
);
```

### 5.2 查看表结构

```mysql
desc 表名;
```

### 5.3 备份表

备份`数据`，不备份`表结构`

```mysql
create   table   新表   as   (select   *   from   旧表)
```

### 5.4 改表名

```mysql
rename   table   旧表名   to   新表名;
```

### 5.5 删除表

1.直接删除（不存在的话会报错）

```mysql
drop   table   表名;
```

2.先判断再删除（表不存在不会报错）

```mysql
drop   table   if   exists   表名;
```

3.清空表（截断表）

```mysql
truncate   table   表名;
```

4.delete  和  truncate , drop 的区别

- drop: 删除表,`表结构`和`表数据`一起删除 
- truncate:清空表,`只清空数据`,表结构还在 
- delete:`只删除数据` 



truncate 和 delete的区别: 

> 1.truncate 是一次性删除所有数据, 
>
> delete 可以准确的删除某一部分或者某一条数据 
>
> 2.数据量超过1000,使用truncate较好 
>
> 数据量较少,使用delete 
>
> 3.工作中用的较多的是delete,如果要清空整张表,才会用truncate.



## 6 数据的增删改查

### 6.1 增

```mysql
#全量插入
insert   into  表名   values(值1,值2...);
#部分插入
insert   into   表名(字段1, 字段2...)   values(值1, 值2...);
#批量插入
insert   into   表名   values (),(),()...;
```

### 6.2 删

```mysql
delete from 表名 where 条件;
```

### 6.3 改

```mysql
update 表名 set 列=值，列2=值2 where 条件;
```

### 6.4 查

#### 6.4.1 基础查询

```mysql
select * from student;
```



#### 6.4.2 逻辑查询

- `and` :并且的意思,经过and 筛选数据越来越少--要求条件都满足才显示,and优先级高于or,通常使用小括号进行提高优先级
- `or` :或者的意思,经过or的筛选数据越来越多--只要满足其中一个就可以了 
- `not` :否定的意思 

`优先级`：not > and > or --混用时,要用小括号提高优先级



#### 6.4.3 比较运算

> \> :大于 
>
> < :小于 
>
> = :大于等于 
>
> <= :小于等于 
>
> != :不等于 
>
> <>:不等于 



#### 6.4.4 范围查询

- in () : 在...里面,括号里面是一个个的
- not in (): 不在...里面,跟in 相反



#### 6.4.5 模糊查询

举例：

```mysql
select * from student where sname like '刘%';
```

- like :像.... 
- %:代表[0,~) ---最少代表0个字 
- _:代表1个字



模糊查找分类: 

1. 前模糊: %值 
2. 后模糊: 值% 
3. 前后模糊: %值 





#### 6.4.6 边界值查询

举例：

```mysql
select   *   from   student   where   studentid   between  1  and  5;
```

`列 between A and B`: 某一列的值在A和B 之间,`包含A 和B` ,也就是 列>=A and 列<=B; 





#### 6.4.7 空值查询

空值:null --空值不等于任何值 

- is null :是空值 
- is not null :非空值 





#### 6.4.8 去重查询

在 select 后查询字段前使用 distinct 可以查询出消除重复行后的结果

```mysql
select   distinct   sname   from   student;
```

`注意`：使用 distinct 对多个字段去重查询时，`只有多个字段组合值重复时，才会去重`，反之不会。

```mysql
select  distinct   sname,sex   from   student ;
```





#### 6.4.9 查询排序

- 关键字： order by
- 升序： asc （默认升序）
- 降序： desc 

举例：

```mysql
select   *   from   student   order by   studentid   asc;
```





#### 6.4.10 日期查询

1 datetime格式：YYYY-MM-DD HH:mm:ss

2 查询系统时间：select now();

```mysql
-- 3 查找具体时间点：--
select   *   from   student   where   birthday ='2013-11-06 10:31:57';
--  4 按年份查找:--
select  *   from   student   where   year(birthday)='2013';
-- 5 按月份查找: --
select * from student  where month(birthday)='2';
-- 6 按日期查找: --
select * from  student where day(birthday)='12' ;

select * from  student where dayofmonth(birthday)='12' ;
```

7 组合查找:

```mysql
DATE_FORMAT(日期的列,'日期格式') -- %Y-%m-%d %H:%i:%s
-- 按 年 + 月 组合查找:--
select * from student where date_format(birthday,'%Y-%m')='2014-05';
-- 按 年 + 月 + 日 + 时 + 分 + 秒 进行查找:--
select * from student where date_format(birthday,'%Y-%m-%d %H:%i:%s')='2013-07-14 10:31:57'; -- %Y-%m-%d
```

#### 6.4.11 聚合函数

MySQL预设的一些函数，可以快速实现「数据统计」

1  count		计算总行数

```mysql
-- 1  count		计算总行数 --
select count(*) as 学生总数 from student;

-- 2  max		统计最大值--
select max(studentid) from student;

-- 3  min		统计最小值--
select min(studentid) from student;

-- 4  sum		求此列的和 --
select sum(studentid) from student;

-- 5  avg		求此列平均值 --
select avg(studentid) from student where sex='女'; 
select round(avg(studentid),2) from student where sex='女'; --保留两位学号
```

#### 6.4.12 多表查询

> `分类`: 
>
> 笛卡尔积 
>
> 等值连接 
>
> 内连接 
>
> 外连接: 左连接 右连接

##### 6.4.12.1 笛卡尔积

- 定义:两张表中的数据做乘法
- 备注:一般不使用笛卡尔积,因为会产生无效的垃圾数据

##### 6.4.12.2 内连接==等值连接

`内连接语法`：

```mysql
select 列 from 表1 
inner join 表2 
on 表1.列=表2.列 
where 条件;          -- 内连接
```

`等值连接语法`：

```mysql
select 列 from 表1 ,表2 
where 表1.列=表2.列 -- 等值连接 
```

##### 6.4.12.3 外连接

`左连接`：在内连接的基础上,找出`左边表有`,而`右边表没有`的数据,右边表没有的数据用 null 表示. 

`右连接`：在内连接的基础上,找出`右边表有`,而`左边表没有`的数据,左边表没有的数据用 null表示. 



```mysql
select * from student2 st left join class2 cl on st.classid=cl.classid;  -- 左连接

select * from student2 st right join class2 cl on st.classid=cl.classid;  -- 由连接
```







#### 6.4.13 分组查询

1  什么情况下用要用到分组？

答：当所求的结果存在多个分类的时候,就要分组.一般当出现:每个 每种 ,不同 之类的词就要分组



2  分组的语法：

```mysql
select   分组的列,聚合函数   from   表名 
where   分组前条件 
group by   分组的列 
having   分组后条件 
order by   列   asc /desc;
```

3  注意：

- select 后面的 分组的列 跟group by 后面的必须保持一致 
- 聚合函数只能放在having 分组后的条件里面,不能放在where后面 
- order by 永远放在SQL语句的最后面 





#### 6.4.14 子查询

1 `定义`：在一个 select 中嵌入另外一个 select ，这就是子查询

- 一般情况下，第一个 select 是「主查询」
- 子查询一般充当数据源
- 子查询是可以独立存在，是一条完整的查询语句

`注意`：子查询中表不能和外层表相同，只有查询不报错，不建议

2 标量子查询（判断语句和返回一个数据）

```mysql
select * from student where birthday<(select birthday from student where sname='蔡学森');

select score from score where studentid=(select studentid from student where sname="蔡学森");
```

3 列子查询

```mysql
select score from score where studentid in (select studentid from student where sname like '刘%' or sname like '张%');
```

4 limit 用法

- 查询时，用于返回前几条或中间几条数据
- 接受两个参数：第一个是「起始值」，第二是「返回数目值」。注意起始值是从0开始的！

```mysql
select * from student where sex="男" order by studentid desc limit 0,1; -- 起始值0，可以 省略不写
```

5 表子查询

```mysql
-- 首先查出Linux课程的courseid 
select * from course where coname in ("Linux"); 
-- 然后拿着查到的课程编号去成绩表查询成绩 
select score from score where courseid in (1); 
-- 组合成子查询（列子查询）
select score from score where courseid in (select courseid from course where coname in ("Linux"));
```



## 7 高级操作

### 7.1 命令行的使用

1. 登录数据库： mysql -uroot -p123456
2. 查看所有数据仓库： show databases;
3. 使用某个数据库： use 仓库名;
4. 查看当前使用的仓库： select database();
5. 创建数据库：create database 仓库名 charset=utf8;
6. 删除数据库： drop database 仓库名;



### 7.2 备份与恢复

1 `备份`

1. 用「管理员」用户打开命令行窗口

2. 输入备份命令

```mysql
mysqldump    -uroot    -p123456    mysql>D:\mysql_bak.sql 

-- [windows下，不是mysql环境下] 

-- mysql是需要备份的数据仓库名字 
-- D:\mysql_bak.sql
```

2 `恢复`

1. 登录「MySQL」，创建一个新的数据仓库去接收之前备份数据文件

2. 以「管理员」身份运行命令行，输入恢复命令

```mysql
mysql   -uroot   -p123456   新数据仓库名字<备份文件存放的路径 
-- 例 :
mysql -uroot -p123456 tashi_bak<D:\mysql_bak.sql 

-- [windows下，不是mysql环境下]
```

### 7.3 存储过程（Storee Procedure）

#### 1 存储过程简介

`定义`：存储过程也叫存储程序，它是一条或者多条SQL的集合，MySQL 5.0以前并不支持存储过程

sql语句是需要`先编译然后再执行`的，而存储过程是经过`编译后`存储在数据库中的。



`优点`：

1. **增强sql语言的功能和灵活性**
2. **标准组件式编程**：存储过程被创建后，可以在程序中被多次调用，而不必重新编写该存储过程的SQL语句。而且数据库专业人员可以随时对存储过程进行修改，对应用程序源代码毫无影响。
3. **较快的执行速度**
4. 减少网络流量：针对同一个数据库对象的操作（如查询、修改），如果这一操作所涉及的Transaction-SQL语句被组织进存储过程，那么当在客户计算机上调用该存储过程时，网络中传送的只是该调用语句，从而大大减少网络流量并降低了网络负载。
5. 作为一种安全机制来充分利用：通过对执行某一存储过程的权限进行限制，能够实现对相应的数据的访问权限的限制，避免了非授权用户对数据的访问，保证了数据的安全。

#### 2 mysql存储过程的创建

**语法：**

**CREATE PROCEDURE** **过程名([[IN|OUT|INOUT] 参数名 数据类型[,[IN|OUT|INOUT] 参数名 数据类型…]]) [特性 ...] 过程体**

举例：

```mysql
DELIMITER //
  CREATE PROCEDURE myproc(OUT s int)
    BEGIN
      SELECT COUNT(*) INTO s FROM students;
    END
    //
DELIMITER ;

delimiter // 
create procedure   test_pro() -- test_pro是一个存储过程的名字 
begin   select   *   from   student; -- 这里写SQL语句 
end // 
```

**分隔符：**

mysql是以“；”作为分隔符的，没有分隔符。没有分隔符mysql就会把存储过程当做sql语句一起执行

所以，要在存储过程开始用  “DELIMITER //”声明当前段分隔符，让编译器把两个"//"之间的内容当做存储过程的代码，不会执行这些代码；

“DELIMITER ;”的意为把分隔符还原。

**参数：**

1. **IN**参数的值必须在调用存储过程时指定，在存储过程中修改该参数的值不能被返回，为默认值
2. **OUT****:**该值可在存储过程内部被改变，并可返回
3. **INOUT****:**调用时指定，并且可被改变和返回

**过程体：**

过程体的开始与结束使用BEGIN与END进行标识。

#### 3 **变量**

**语法：**DECLARE 变量名1[,变量名2...] 数据类型 [默认值];

**数据类型有：**

数值类型：INT/INTEGER  ,   FLOAT,   DOUBLE , DCIMAL ...

日期和时间类型：DATE , YEAR , DATETIME

字符串类型：CHAR , VARCHAR , BLOB....



**变量赋值：**

**语法：**SET 变量名 = 变量值 [,变量名= 变量值 ...]



**用户变量**

用户变量一般以`@`开头

`注意`：滥用用户变量会导致程序难以理解及管理

```mysql
#在MySQL客户端使用用户变量
SELECT 'Hello World' into @x;
SELECT @x;      -- Hello World--
SET @y='Goodbye Cruel World';
SELECT @y;    -- Goodbye Cruel World--
SET @z=1+2+3;
SELECT @z;   -- 6 --

#在存储过程中使用用户变量
CREATE PROCEDURE GreetWorld() SELECT CONCAT(@greeting,' World');
SET @greeting='Hello';
CALL GreetWorld();    # Hello World

#在存储过程间传递全局范围的用户变量
CREATE PROCEDURE p1() SET @last_proc='p1';
CREATE PROCEDURE p2() SELECT CONCAT('Last procedure was ',@last_proc);
CALL p1();
CALL p2();    # 执行结果 ：Last procedure was p1

```



**注释**

MySQL存储过程可使用两种风格的注释：

双杠：--，该风格一般用于单行注释

C风格： 一般用于多行注释



#### 4mysql存储过程的调用

用call和你过程名以及一个括号，括号里面根据需要，加入参数，参数包括输入参数、输出参数、输入输出参数。

```mysql
call 存储过程名() 
-- 例 
call test_pro()
```



#### 5 mysql 存储过程的查询

```mysql
#查询存储过程
SELECT name FROM mysql.proc WHERE db='数据库名';
SELECT routine_name FROM information_schema.routines WHERE routine_schema='数据库名';
SHOW PROCEDURE STATUS WHERE db='数据库名';

#查看存储过程详细信息
SHOW CREATE PROCEDURE 数据库.存储过程名;
```



#### 6 mysql存储过程的修改

ALTER PROCEDURE 更改用CREATE PROCEDURE 建立的预先指定的存储过程，其不会影响相关存储过程或存储功能。

```mysql
ALTER {PROCEDURE | FUNCTION} sp_name [characteristic ...] 

characteristic:   # 参数指定存储函数的特性
{ CONTAINS SQL |  # 表示子程序包含SQL语句，但不包含读或写数据的语句
NO SQL |               # 表示子程序中不包含SQL语句
READS SQL DATA |     #  表示子程序中包含读数据的语句
MODIFIES SQL DATA }   #  表示子程序中包含写数据的语句
| SQL SECURITY { DEFINER | INVOKER }  # 指明谁有权限来执行，DEFINER表示只有定义者自己才能够执行；INVOKER表示调用者可以执行。
| COMMENT 'string'   # 是注释信息

# 举例
#将读写权限改为MODIFIES SQL DATA，并指明调用者可以执行。
ALTER  PROCEDURE  num_from_employee
  MODIFIES SQL DATA
  SQL SECURITY INVOKER ;
#将读写权限改为READS SQL DATA，并加上注释信息'FIND NAME'。
ALTER  PROCEDURE  name_from_employee
  READS SQL DATA
  COMMENT 'FIND NAME' ;
```



#### 7 mysql存储过程的删除

语法：

```mysql
DROP PROCEDURE [过程1[,过程2…]]
```

#### 8  mysql存储过程的控制语句

##### 1 变量作用域

内部变量在其作用域范围内享有更高的优先权，当执行到`end`时，内部变量消失，不再可见了，在存储过程外再也找不到这个内部变量

但是可以通过`out参数`或者将其值指派给`会话变量`来保存其值。

```mysql
#变量作用域
DELIMITER //
  CREATE PROCEDURE proc()
    BEGIN
      DECLARE x1 VARCHAR(5) DEFAULT 'outer';
        BEGIN
          DECLARE x1 VARCHAR(5) DEFAULT 'inner';
          SELECT x1;
        END;
      SELECT x1;
    END;
    //
DELIMITER ;
#调用
CALL proc();
```



##### 2 条件语句

```mysql
#条件语句IF-THEN-ELSE
DROP PROCEDURE IF EXISTS proc3;
DELIMITER //
CREATE PROCEDURE proc3(IN parameter int)
  BEGIN
    DECLARE var int;
    SET var=parameter+1;
    IF var=0 THEN
      INSERT INTO t VALUES (17);
    END IF ;
    IF parameter=0 THEN
      UPDATE t SET s1=s1+1;
    ELSE
      UPDATE t SET s1=s1+2;
    END IF ;
  END ;
  //
DELIMITER ;

#CASE-WHEN-THEN-ELSE语句
DELIMITER //
  CREATE PROCEDURE proc4 (IN parameter INT)
    BEGIN
      DECLARE var INT;
      SET var=parameter+1;
      CASE var
        WHEN 0 THEN
          INSERT INTO t VALUES (17);
        WHEN 1 THEN
          INSERT INTO t VALUES (18);
        ELSE
          INSERT INTO t VALUES (19);
      END CASE ;
    END ;
  //
DELIMITER ;
```

##### 3 循环语句

```mysql
# 1  WHILE-DO…END-WHILE 
DELIMITER //
  CREATE PROCEDURE proc5()
    BEGIN
      DECLARE var INT;
      SET var=0;
      WHILE var<6 DO
        INSERT INTO t VALUES (var);
        SET var=var+1;
      END WHILE ;
    END;
  //
DELIMITER ;

# 2
#REPEAT...END REPEAT
#此语句的特点是执行操作后检查结果
DELIMITER //
  CREATE PROCEDURE proc6 ()
    BEGIN
      DECLARE v INT;
      SET v=0;
      REPEAT
        INSERT INTO t VALUES(v);
        SET v=v+1;
        UNTIL v>=5
      END REPEAT;
    END;
  //
DELIMITER ;

#3
#LOOP...END LOOP
# LABLES标号
# 标号可以用在begin repeat while 或者loop 语句前，语句标号只能在合法的语句前面使用。可以跳出循环，使运行指令达到复合语句的最后一步。
DELIMITER //
  CREATE PROCEDURE proc7 ()
    BEGIN
      DECLARE v INT;
      SET v=0;
      LOOP_LABLE:LOOP
        INSERT INTO t VALUES(v);
        SET v=v+1;
        IF v >=5 THEN
          LEAVE LOOP_LABLE;
        END IF;
      END LOOP;
    END;
  //
DELIMITER ;


#4
#ITERATE迭代
#通过引用复合语句的标号,来从新开始复合语句
DELIMITER //
  CREATE PROCEDURE proc8()
  BEGIN
    DECLARE v INT;
    SET v=0;
    LOOP_LABLE:LOOP
      IF v=3 THEN
        SET v=v+1;
        ITERATE LOOP_LABLE;
      END IF;
      INSERT INTO t VALUES(v);
      SET v=v+1;
      IF v>=5 THEN
        LEAVE LOOP_LABLE;
      END IF;
    END LOOP;
  END;
  //
DELIMITER ;
```



#### 9 mysql存储过程的基本函数

###### 字符串类

> CHARSET(str) //返回字串字符集
> CONCAT (string2 [,... ]) //连接字串
> INSTR (string ,substring ) //返回substring首次在string中出现的位置,不存在返回0
> LCASE (string2 ) //转换成小写
> LEFT (string2 ,length ) //从string2中的左边起取length个字符
> LENGTH (string ) //string长度
> LOAD_FILE (file_name ) //从文件读取内容
> LOCATE (substring , string [,start_position ] ) 同INSTR,但可指定开始位置
> LPAD (string2 ,length ,pad ) //重复用pad加在string开头,直到字串长度为length
> LTRIM (string2 ) //去除前端空格
> REPEAT (string2 ,count ) //重复count次
> REPLACE (str ,search_str ,replace_str ) //在str中用replace_str替换search_str
> RPAD (string2 ,length ,pad) //在str后用pad补充,直到长度为length
> RTRIM (string2 ) //去除后端空格
> STRCMP (string1 ,string2 ) //逐字符比较两字串大小,
> SUBSTRING (str , position [,length ]) //从str的position开始,取length个字符,
> 注：mysql中处理字符串时，默认第一个字符下标为1，即参数position必须大于等于1
>
> TRIM([[BOTH|LEADING|TRAILING] [padding] FROM]string2) //去除指定位置的指定字符
> UCASE (string2 ) //转换成大写
> RIGHT(string2,length) //取string2最后length个字符
> SPACE(count) //生成count个空格

###### 数学类：

> ABS (number2 ) //绝对值
> BIN (decimal_number ) //十进制转二进制
> CEILING (number2 ) //向上取整
> CONV(number2,from_base,to_base) //进制转换
> FLOOR (number2 ) //向下取整
> FORMAT (number,decimal_places ) //保留小数位数
> HEX (DecimalNumber ) //转十六进制
> 注：HEX()中可传入字符串，则返回其ASC-11码，如HEX('DEF')返回4142143
> 也可以传入十进制整数，返回其十六进制编码，如HEX(25)返回19
> LEAST (number , number2 [,..]) //求最小值
> MOD (numerator ,denominator ) //求余
> POWER (number ,power ) //求指数
> RAND([seed]) //随机数
> ROUND (number [,decimals ]) //四舍五入,decimals为小数位数] 注：返回类型并非均为整数
>
> SIGN (number2 ) // 正数返回1，负数返回-1

###### 日期时间类：

> ADDTIME (date2 ,time_interval ) //将time_interval加到date2
> CONVERT_TZ (datetime2 ,fromTZ ,toTZ ) //转换时区
> CURRENT_DATE ( ) //当前日期
> CURRENT_TIME ( ) //当前时间
> CURRENT_TIMESTAMP ( ) //当前时间戳
> DATE (datetime ) //返回datetime的日期部分
> DATE_ADD (date2 , INTERVAL d_value d_type ) //在date2中加上日期或时间
> DATE_FORMAT (datetime ,FormatCodes ) //使用formatcodes格式显示datetime
> DATE_SUB (date2 , INTERVAL d_value d_type ) //在date2上减去一个时间
> DATEDIFF (date1 ,date2 ) //两个日期差
> DAY (date ) //返回日期的天
> DAYNAME (date ) //英文星期
> DAYOFWEEK (date ) //星期(1-7) ,1为星期天
> DAYOFYEAR (date ) //一年中的第几天
> EXTRACT (interval_name FROM date ) //从date中提取日期的指定部分
> MAKEDATE (year ,day ) //给出年及年中的第几天,生成日期串
> MAKETIME (hour ,minute ,second ) //生成时间串
> MONTHNAME (date ) //英文月份名
> NOW ( ) //当前时间
> SEC_TO_TIME (seconds ) //秒数转成时间
> STR_TO_DATE (string ,format ) //字串转成时间,以format格式显示
> TIMEDIFF (datetime1 ,datetime2 ) //两个时间差
> TIME_TO_SEC (time ) //时间转秒数]
> WEEK (date_time [,start_of_week ]) //第几周
> YEAR (datetime ) //年份
> DAYOFMONTH(datetime) //月的第几天
> HOUR(datetime) //小时
> LAST_DAY(date) //date的月的最后日期
> MICROSECOND(datetime) //微秒
> MONTH(datetime) //月
> MINUTE(datetime) //分返回符号,正负或0
> SQRT(number2) //开平方

10 总结：

- 存储过程其实就是一个「可重复执行」的SQL语句的集合
- 存储过程只需编译一次，然后被缓存起来，下次直接运行
- 存储过程可以减少网络交互，减少网络访问量
- 参考网址：https://www.cnblogs.com/mark-chan/p/5384139.html
- 案例：https://www.jianshu.com/p/97d0f5f04193
- 系统学习数据库：http://c.biancheng.net/view/7232.html





### 7.4 视图

#### 1  定义

> 本质上是对`查询的封装`，对于经常需要在多个地方「重复」使用的查询语句，可以将其定义成「视图」，方便使用。
>
> 要`注意区别视图和数据表的本质`，即视图是基于真实表的一张`虚拟的表`，其数据来源均建立在真实表的基础上。

#### 2视图的优点

视图与表在本质上虽然不相同，但视图经过定义以后，结构形式和表一样，可以进行查询、修改、更新和删除等操作。同时，视图具有如下优点：

1) `定制用户数据，聚焦特定的数据`

在实际的应用过程中，不同的用户可能对不同的数据有不同的要求。

2) `简化数据操作`

在使用查询时，很多时候要使用聚合函数，同时还要显示其他字段的信息，可能还需要关联到其他表，语句可能会很长，如果这个动作频繁发生的话，可以创建视图来简化操作。

3) `提高数据的安全性`

视图是虚拟的，物理上是不存在的。可以只授予用户视图的权限，而不具体指定使用表的权限，来保护基础数据的安全。

4) `共享所需数据`

通过使用视图，每个用户不必都定义和存储自己所需的数据，可以共享数据库中的数据，同样的数据只需要存储一次。

5) `更改数据格式`

通过使用视图，可以重新格式化检索出的数据，并组织输出到其他应用程序中。

6) `重用 SQL 语句`

视图提供的是对查询操作的封装，本身不包含数据，所呈现的数据是根据视图定义从基础表中检索出来的，如果基础表的数据新增或删除，视图呈现的也是更新后的数据。视图定义后，编写完所需的查询，可以方便地重用该视图。

#### 3  创建视图

```mysql
create  view  视图名称  as  查询语句;
```

#### 4  查看视图

```mysql
show  tables;
```

`注意`：查看视图与查看表格是同一命令，所以在创建视图时，尽量使用特定的标志去标识视图，比如在视图名称前面

加上一个 v （以后看到v开头的表格，就知道是一个视图）

#### 5 使用视图

```mysql
select  *  from  视图名称; 
-- 例 
select  *  from  v_test;
```

#### 6  删除视图

```mysql
drop  view  视图名称;
```

### 7.5  事务

#### 1  定义

> 事务是一个操作序列，这些操作要么「都执行」，要么「都不执行」

对数据进行操作才会产生事务，查询不会产生事务

truncate不产生事务

#### `2 事务的四大特性（ACID）`

事务具有 4 个特性，即原子性（Atomicity）、一致性（Consistency）、隔离性（Isolation）和持久性（Durability），这 4 个特性通常简称为 ACID。

> ### 1. 原子性
>
> 事务是一个完整的操作。事务的各元素是不可分的（原子的）。事务中的所有元素必须作为一个整体提交或回滚。如果事务中的任何元素失败，则整个事务将失败。
>
> 以银行转账事务为例，如果该事务提交了，则这两个账户的数据将会更新。如果由于某种原因，事务在成功更新这两个账户之前终止了，则不会更新这两个账户的余额，并且会撤销对任何账户余额的修改，事务不能部分提交。
>
> ### 2. 一致性
>
> 当事务完成时，数据必须处于一致状态。也就是说，在事务开始之前，数据库中存储的数据处于一致状态。在正在进行的事务中. 数据可能处于不一致的状态，如数据可能有部分被修改。然而，当事务成功完成时，数据必须再次回到已知的一致状态。通过事务对数据所做的修改不能损坏数据，或者说事务不能使数据存储处于不稳定的状态。
>
> 以银行转账事务事务为例。在事务开始之前，所有账户余额的总额处于一致状态。在事务进行的过程中，一个账户余额减少了，而另一个账户余额尚未修改。因此，所有账户余额的总额处于不一致状态。事务完成以后，账户余额的总额再次恢复到一致状态。
>
> ### 3. 隔离性
>
> 对数据进行修改的所有并发事务是彼此隔离的，这表明事务必须是独立的，它不应以任何方式依赖于或影响其他事务。修改数据的事务可以在另一个使用相同数据的事务开始之前访问这些数据，或者在另一个使用相同数据的事务结束之后访问这些数据。
>
> 另外，当事务修改数据时，如果任何其他进程正在同时使用相同的数据，则直到该事务成功提交之后，对数据的修改才能生效。张三和李四之间的转账与王五和赵二之间的转账，永远是相互独立的。
>
> ### 4. 持久性
>
> 事务的持久性指不管系统是否发生了故障，事务处理的结果都是永久的。
>
> 一个事务成功完成之后，它对数据库所作的改变是永久性的，即使系统出现故障也是如此。也就是说，一旦事务被提交，事务对数据所做的任何变动都会被永久地保留在数据库中。

#### 3 执行事务的语法和流程

1  开启事务

> 在事务中的操作会存在缓存中

```mysql
begin;
```

2  提交事务

> 将缓存中的数据变更到物理表中

```mysql
commit;

自动提交开关：

SHOW   VARIABLES   LIKE   '%AUTOCOMMIT%'; 
set   autocommit = 0;
```

3  回滚事务

> 放弃缓存中的数据变更

```mysql
rollback;
```

#### 4 注意事项

> MySQL 事务是一项非常消耗资源的功能，大家在使用过程中要注意以下几点。
>
> #### 1) 事务尽可能简短
>
> 事务的开启到结束会在数据库管理系统中保留大量资源，以保证事务的原子性、一致性、隔离性和持久性。如果在多用户系统中，较大的事务将会占用系统的大量资源，使得系统不堪重负，会影响软件的运行性能，甚至导致系统崩溃。
>
> #### 2) 事务中访问的数据量尽量最少
>
> 当并发执行事务处理时，事务操作的数据量越少，事务之间对相同数据的操作就越少。
>
> #### 3) 查询数据时尽量不要使用事务
>
> 对数据进行浏览查询操作并不会更新数据库的数据，因此应尽量不使用事务查询数据，避免占用过量的系统资源。
>
> #### 4) 在事务处理过程中尽量不要出现等待用户输入的操作
>
> 在处理事务的过程中，如果需要等待用户输入数据，那么事务会长时间地占用资源，有可能造成系统阻塞。

#### 5 事务的隔离级别

待学习

### 7.6  索引

#### 1 定义

在数据库中建立「索引」，可以大大提高数据查询的速度。相当于目录。

顺序访问是要全表扫描，每条数据都要遍历一遍，直到找到想要的数据，而索引访问是只访问索引列

`创建索引其实就是映射了一张表，每个索引值以指针的方式指向表中对应的行的数据`



优点

索引的优点如下：

- 通过创建唯一索引可以保证数据库表中每一行数据的唯一性。
- 可以给所有的 MySQL 列类型设置索引。
- 可以大大加快数据的查询速度，这是使用索引最主要的原因。
- 在实现数据的参考完整性方面可以加速表与表之间的连接。
- 在使用分组和排序子句进行数据查询时也可以显著减少查询中分组和排序的时间

缺点

增加索引也有许多不利的方面，主要如下：

- 创建和维护索引组要耗费时间，并且随着数据量的增加所耗费的时间也会增加。
- 索引需要占磁盘空间，除了数据表占数据空间以外，每一个索引还要占一定的物理空间。如果有大量的索引，索引文件可能比数据文件更快达到最大文件尺寸。
- 当对表中的数据进行增加、删除和修改的时候，索引也要动态维护，这样就降低了数据的维护速度。



1  查看索引：

```mysql
show   index   from   表名;
```

2  创建索引

```mysql
-- 方法一： 
create  table  girl ( 
		id  int  primary  key,        -- 给某个字段指定为主键，那么该字段就是索引 
		name  varchar(10) );

-- 方法二： 
-- create index 索引名称 on 表名(字段) 

create  index  id_index  on  girl(id);           -- 手动创建索引
```

3  删除索引

```mysql
drop  index  索引名称  on  表名;              -- 索引名称对应key_name
```



### 8 事件（event）

事件（Event）也可称为事件调度器（Event Scheduler），是用来执行定时任务的一组 SQL 集合，可以通俗理解成 MySQL 中的`定时器`。一个事件可调用一次，也可周期性的启动。



### 9 日志

日志操作是数据库维护中最重要的手段之一

如果 MySQL 数据库系统意外停止服务，我们可以通过错误日志查看出现错误的原因。还可以通过二进制日志文件来查看用户分别执行了哪些操作、对数据库文件做了哪些修改。然后，还可以根据二进制日志中的记录来修复数据库。

在 MySQL 所支持的日志文件里，除了二进制日志文件外，其它日志文件都是文本文件。默认情况下，MySQL 只会启动`错误日志`文件，而其它日志则需要手动启动。



使用日志有优点也有`缺点`。启动日志后，虽然可以对 MySQL 服务器性能进行维护，但是会`降低 MySQL 的执行速度`。例如，一个查询操作比较频繁的 MySQL 中，记录通用查询日志和慢查询日志要`花费很多的时间`。

日志文件还会`占用大量的硬盘空间`。对于用户量非常大、操作非常频繁的数据库，日志文件需要的存储空间甚至比数据库文件需要的存储空间还要大。因此，是否启动日志，启动什么类型的日志要根据具体的应用来决定。

#### 9.1 日志的分类

- `二进制日志`：该日志文件会以二进制的形式记录数据库的各种操作，但不记录查询语句。
- `错误日志`：该日志文件会记录 MySQL 服务器的启动、关闭和运行错误等信息。
- `通用查询日志`：该日志记录 MySQL 服务器的启动和关闭信息、客户端的连接信息、更新、查询数据记录的 SQL 语句等。
- `慢查询日志`：记录执行事件超过指定时间的操作，通过工具分析慢查询日志可以定位 MySQL 服务器性能瓶颈所在。

#### 9.2 错误日志

`错误日志`（Error Log）是 MySQL 中最常用的一种日志，主要记录 MySQL 服务器启动和停止过程中的信息、服务器在运行过程中发生的故障和异常情况等。

##### 9.2.1  启动和设置错误日志

`错误日志默认是启动的`

在 MySQL 配置文件中，错误日志所记录的信息可以通过` log-error`和 log-warnings 来定义，其中，log-err 定义是否启用错误日志功能和错误日志的存储位置，log-warnings 定义是否将警告信息也记录到错误日志中。

将 log_error 选项加入到 MySQL 配置文件的 [mysqld] 组中，形式如下：

```mysql
[mysqld]
log-error=dir/{filename}
```

> 注意：错误日志中记录的并非全是错误信息，例如 MySQL 如何启动 InnoDB 的表空间文件、如何初始化自己的存储引擎等，这些也记录在错误日志文件中。

##### 9.2.2 查看错误日志

查找日志文件路径命令：

```mysql
SHOW VARIABLES LIKE 'log_error';
```

##### 9.2.3 删除错误日志

mysqladmin 命令的语法如下：

`mysqladmin -uroot -p flush-logs`

执行该命令后，MySQL 服务器首先会自动创建一个新的错误日志，然后将旧的错误日志更名为 filename.err-old。(这是在windows下的情况)



#### 9.3 二进制日志

```mysql
SHOW VARIABLES LIKE 'log_bin';
```

#### 9.4 通用查询日志

```mysql
SHOW VARIABLES LIKE '%general%';
```

#### 9.5 慢查询日志

```mysql
SHOW VARIABLES LIKE 'slow_query%';
```

### 附  命令行中乱码

1  首先在命令行中登录数据库；

2  执行如下命令：

```mysql
set   character_set_client  =  gb2312; 

set   character_set_results  =  gb2312;
```

