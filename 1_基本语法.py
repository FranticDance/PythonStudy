# 打印语句,可以打印多个，打印结果每个之间将自动用空格分隔
print("hello python", "welcome")
print(None)

# 变量定义
a = 3

# 检查类型,type()函数,type函数是一个内置函数
a1 = 123
a2 = '123'
print(a1 == a2)
print(type(a1))
print(type(type(a1)))

# 语句的多行定义
total = 3 + \
        2 + \
        4

# if语句块
if a == 3:
    # 同一个语句块，不用使用{}来包围，但是需要保持相同的缩进
    print("a等于3")
    print("a == 3")
elif a > 3:
    print("a大于3")
else:
    print("a<3")


# 类型转换,不同的类型，不可以进行运算。注意，整数和小数同属数值类型，可以直接操作。
# 类型转换函数 int() float() str() bool()。
# 对于bool()函数，参数不为0，则返回为True,比如不为0的数，字符串等等。 0,空串，None会被转化为False
# 对于int()函数，参数如果为小数，则直接舍弃小数部分，不做四舍五入等等。

c = "hello"
d = 123
e = 123.22
f = True
g = 0
print(c + str(d))
print(d + e)
print(int(f))
print(int(22.66))
print(int(22.21))
print(bool(d))
print(bool("fff"))
print(bool(None))
print(bool(""))
print(bool(''))