#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# filename:
# author:
# description: 04.python基础

# ---------------------------*************数据类型和变量*************---------------------------
# 数据类型
# 整数：python可以处理任意大小的整数，当然包括负整数
# 浮点数：因为按照科学记数法表示时，一个浮点数的小数点位置是可变的，如：1.23e9和12.3e8是完全相等的。
# 字符串：使用''或""括起来的任意文本，''或""只是一种表示方式，不是字符串的一部分


# ---------------------------*************字符串和编码*************---------------------------
# 字符串和编码
# python3的字符串是以Unicode编码的，故python是支持多语言的
print('字符串str')

# 单个字符的编码：
# ord()函数获取字符的整数表示
print(ord('A'))
print(ord('a'))
print(ord('中'))
# chr()函数把编码转换为对应的字符
print(chr(20013) + chr(25991))

# 字符类型转化处理
# python字符串类型是str，在内存中以Unicode表示，在网络上传输或保存到磁盘上需要将str变为以字节为单位的bytes.
# python对bytes类型的数据用带b前缀的单引号或双引号表示
x = b'ABC'
print(x.decode())
# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
# 如果bytes中包含无法解码的字节，decode()方法会报错(如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节)
print(b'\xe4\xb8\xad\xe6\xff'.decode('utf-8', errors='ignore'))

# 计算字节数
print(len('ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'))
print(len('中文'.encode('utf-8')))


# 格式化字符串
print("Hi, %s, you have $%d" % ('Crisimple', 10000000))
# 常见的占位符
# 占位符：      %d      %f      %s        %x
# 替换内容：   整数    浮点数  字符串   十六进制整数
# 注意：用%%来表示一个%

# format()---它会用传入的参数依次替换字符串内的占位符{0}, {1}, ......
print("Hello, {0}, 确定过眼神, 高感度提高了{1:.1f}%".format('XXX', 100.001))


# ---------------------------*************使用list和tuple*************---------------------------
# list: python内置的一种数据类型，是一种"可变"有序的集合，可以随时添加和删除其中的元素
# 列出一个班的某些学生：
classmates = ['gyf', 'yt', 'wl', 'hyr', 'zy', 'snn']
print(classmates)

# 列表索引
print(classmates[0])
# 如果索引超出了范围，python会报IndexError错误，为了确保列表索引不越界，则列表索引的最后一个元素的下标为：len(classmates) - 1
# print(classmates[6])
print(len(classmates)-1)
print(classmates[len(classmates)-1])

# 列表追加
# 追加到列表的末尾，使用append()
classmates.append('xj')
# 把元素插入到指定的位置，使用insert()
classmates.insert(1, 'll')
print(classmates, classmates[1])

# 删除list末尾的元素，使用pop()；同时如果要删除指定位置的元素，使用pop(i)
print(classmates.pop())
print(classmates)
print(classmates.pop(4))
print(classmates)

# 把某个元素替换成别的元素
classmates[1] = 'zj'
print(classmates)

# 列表的嵌套
p = [1, 2, 3]
s = ["A", "B", p, "C"]
print(s)

# 空列表的长度为0
list_empty = []
print(list_empty)
print(len(list_empty))


# 元组tuple：和list非常类似，但是tuple一旦初始化就不能修改了
# 元组是没有append()、insert()方法的，因为tuple不可变，所以代码更安全
solid_t = (1, 2, 3)
print(solid_t)

# 定义一个空的tuple
t = ()
print(t)

# 定义只有一个元素的tuple，要这么定义才行：
first_t = (1, )
print(first_t)

# "一个可变"的tuple，表面上下面这个例子tuple的元素变了，实际上变的是list里的元素
# tuple所谓的不变是说tuple的每个元素的指向永远不变，指向list就不能指成指向其他对象，但指向的这个list本身是可变的！
t = ('a', 'b', ['A', 'B'])
t[2][0] = "X"
t[2][1] = "Y"
print(t)


# ---------------------------*************条件判断*************---------------------------
# 简单的条件判断
age = 23
print(age)
if age >= 18:
    print("adult")
elif age >= 6:
    print("teenager")
else:
    print("kid")

# 再议input
# birth = int(input("请输入年份："))
# if birth < 2000:
#     print("90后")
# else:
#     print("00后")
# BMI指数判断
# height = float(input("请输入你的身高："))
# weight = float(input("请输入你的体重："))
# BMI = weight / (height * height)
# print("您的BMI指数为：%d" % BMI)
# if BMI > 32:
#     print("严重肥胖")
# elif BMI >= 28:
#     print("肥胖")
# elif BMI >= 25:
#     print("过重")
# elif BMI >= 18.5:
#     print("正常")
# else:
#     print("过轻")


# ---------------------------*************循环*************---------------------------
# for...in...
names = ('gyf', 'll', 'lf')
for name in names:
    print(name + ",")


he = 0
for x in [1, 2, 3, 4, 5]:
    he = he + x
print(he)

# 随机数生成列表
print(list(range(10)))


# ---------------------------*************使用dict和set*************---------------------------
# dict: python内置了字典，在其他语言中称为map，使用键-值（key-value）存储，具有极快的查找速度。
class_name = ['A', 'B', 'C', 'D', 'E']
class_score = [98, 97, 95, 98, 97]
d = {'A': 98, 'B': 97, 'C': 95, 'D': 98, 'E': 97}
print(d['A'])
d['A'] = 99
print(d['A'])

# 判断字典的的key是否存在的方法
print('A' in d)
print(d.get('B', True))

# 删除一个key，这样对应的value也会从dict中删除
d.pop('B')
print(d)

# dict与list的对比：
#   dict-查找和插入的速度极快，不会随key的增加而变慢；list-查找和插入的时间随着元素的增加而增加
#   dict-需要占用大量的内存，内存浪费多【用空间换取时间】；     list-占用空间小，浪费内存很少。
# 注意：dict的key必须是不可变的对象

# set: 和dict类似，也是一组key的集合，但不存储value。由于key不能重复。所以在set中没有重复的key
# 自动去重
set_num = set([1, 1, 2, 2, 3, 3])
print(set_num)

# add(key)添加元素到set中，可以重复添加但不会有效果
set_num.add(4)
set_num.add(4)
set_num.add(5)
print(set_num)

# remove(key)方法可以删除元素
print(set_num.remove(5))
print(set_num)
print(set_num.pop())
print(set_num)

# 再议不可变对象
# str是不可变对象，而list是可变对象
# 对于可变对象如list进行操作，list内部的内容是会发生变化的
a = ['c', 'b', 'a']
a.sort()
print(a)
# 对于不可变对象，注意a是变量
a = 'abc'
b = a.replace('a', 'A')
print(b)
print(a)
# 所以，对于不可变的对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样就保证了不可变对象本身永远是不可变的

