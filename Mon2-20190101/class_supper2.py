class A:
    def f1(self):
        self.f2()
        #self.__f2()

    def f2(self):
        print('A==>f2')
class B:
    def f2(self):
        print('B==>f2')

class C(B,A):
    pass

c=C()

#说明先从实例c的自己__dict__找是否有f1,没有则从C类中找，没有则找B，再找A
#所以A的f2会被B中同名覆盖，若不想被覆盖可以加双下划线，变为私有，在解析时会替换加类名
c.f1()
print(C.mro())