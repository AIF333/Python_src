class Foo:
    y=333
    def __getitem__(self, item):
        print('-----getietm---->',self,item,type(item))
        return getattr(self,item,'None')
        #也可写成return self.__dict__[item]但是需注意的是只能是dict中有的
        #如类中的变量y，以及这些方法，不会在实例对象的dict中存在，所以这两种并不等价，推荐使用getattr
        #item是字符串，不能直接返回 self.item
    def __setitem__(self, key, value):
        print('----setitem------->',self,key,value,type(key),type(value))
        setattr(self,key,value) #同理 self.__dict__[key]=value，推荐使用setattr
        ##key是字符串，不能直接self.key=value
    def __delitem__(self, key):
        print('------delitem----->',self,key,type(key))
        delattr(self,key) # 类似del self.__dict__[key]，推荐使用 delattr
f=Foo()
f.x=2
print(f.x)
print(f['x'])
f['x']=1
print(f.__dict__)
print(f['x'])

del f['x']
print(f.__dict__)

print(f.y)
print(f['y'])