a = '123'
b = '123'

print(id(a))
print(id(b))
print(a == b)
print(type(a))

# Python中一个对象，分为3个区域，(id，type,value),一个对象创建后，id就不会再变，类似身份证号。这个id其实就像是一个指针。
# 将a改为123后，其实内存中就新创建了个123的对象，而原来的'123'对象，是没有变化的，相当于只是改变了指针的指向。
a = 123

print(id(a))
print(id(b))
print(a == b)
print(type(a))





