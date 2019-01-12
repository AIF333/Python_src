#匿名函数
f=lambda x,y,z:x+y+z
print (f(1,2,3))

#用匿名函数取 value最大的key
dic={'a':3,'b':2,'c':1}
print(max(dic,key=lambda x:dic[x])) #按照value值取最大 等价于下面的
print(max(zip(dic.values(),dic.keys()))[1]) #也等价于下面的有名函数 key等于的是函数地址

def get_value(key):
    return dic[key]
print(max(dic,key=get_value))

#将列表中非 AIF的值后面加一个 333
l1=['AIF','BIF','CIF','DIF']
print(list(map(lambda x:x if x == 'AIF' else x+'333' ,l1)))
#需要注意两点：1.lambda x:x  第二个 x相当于 return x 即上面的表达式相当于：
# lambda x:x if x == 'AIF' else x+'333'  == lambda x:rettun(x if x == 'AIF' else x+'333' )
# 2 .map返回的是一个迭代器，迭代器只能一次从前都后即
g=map(lambda x:x if x == 'AIF' else x+'333' ,l1)
print(list(g)) #有值
print(list(g)) #空列表

print(list(range(3 )))

eval("print(x)",{'x':1},{'x':2}) #三个参数 待执行字符串 全局 局部作用域 ，先局部再全局