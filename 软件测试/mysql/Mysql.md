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

### 7.3 存储过程

1 `定义`：存储过程也叫存储程序，它是一条或者多条SQL的集合

2 创建存储过程：

```mysql
delimiter // 
create procedure   test_pro() -- test_pro是一个存储过程的名字 
begin   select   *   from   student; -- 这里写SQL语句 
end // 
```

3 调用存储过程：

```mysql
call 存储过程名() 
-- 例 
call test_pro()
```

4 总结：

- 存储过程其实就是一个「可重复执行」的SQL语句的集合
- 存储过程只需编译一次，然后被缓存起来，下次直接运行
- 存储过程可以减少网络交互，减少网络访问量



### 7.4 视图

1  定义

> 本质上是对`查询的封装`，对于经常需要在多个地方「重复」使用的查询语句，可以将其定义成「视图」，方便使用。

2  创建视图

```mysql
create  view  视图名称  as  查询语句;
```

3  查看视图

```mysql
show  tables;
```

`注意`：查看视图与查看表格是同一命令，所以在创建视图时，尽量使用特定的标志去标识视图，比如在视图名称前面

加上一个 v （以后看到v开头的表格，就知道是一个视图）

4  使用视图

```mysql
select  *  from  视图名称; 
-- 例 
select  *  from  v_test;
```

5  删除视图

```mysql
drop  view  视图名称;
```

### 7.5  事务

1  定义

> 事务是一个操作序列，这些操作要么「都执行」，要么「都不执行」

对数据进行操作才会产生事务，查询不会产生事务

truncate产生事务

2  开启事务

> 在事务中的操作会存在缓存中

```mysql
begin;
```

3  提交事务

> 将缓存中的数据变更到物理表中

```mysql
commit;

自动提交开关：

SHOW   VARIABLES   LIKE   '%AUTOCOMMIT%'; 
set   autocommit = 0;
```

4  回滚事务

> 放弃缓存中的数据变更

```mysql
rollback;
```



### 7.6  索引

`作用`：在数据库中建立「索引」，可以大大提高数据查询的速度。相当于目录。

`注意`：1 一旦表中有主键，那么主键就是索引值。

​			2  创建索引后在一定程度上会提高数据的`查询速度`，但同时，每次对数据表进行增删改都`需要重建索引`，所以也会对增删改的速度有一些`影响`，所以，只有在需要`大量查询数据`的时候，推荐去创建索引。



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

### 附  命令行中乱码

1  首先在命令行中登录数据库；

2  执行如下命令：

```mysql
set   character_set_client  =  gb2312; 

set   character_set_results  =  gb2312;
```

