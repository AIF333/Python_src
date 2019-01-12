# class O:
#     def test(self):
#         print('OOO')

class A():
     def test(self):
         super().test()
         #print('AAA')
         #super().test()
class B:
    def test(self):
        print('BBB')

class C(A,B):
    # def test(self):
    #     print('CCC')
    pass

c=C()
c.test()
print(C.mro()) #查看子类的继承关系，supper将按照这个列表调用