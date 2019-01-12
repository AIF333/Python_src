#实现不论是否有无参数，有无返回值都可接受
import time

def warrie(func):
    def timeer(*args,**kwargs):#任何参数都可以接手，不论有无
        start=time.time()
        time.sleep(0.5)
        aa="AIF333"
        res=func(*args,**kwargs)
        end=time.time()
        print("program is running %s" % str(end-start))
        return  res
    return timeer

@warrie  #sayHi=warrie(sayHi)
def sayHi(x):
    print("Hi,%s" % str(x))
@warrie
def sayHello():
    print("Hello,world")
    return "Fdd"



sayHi('Allen Iverson')
sayHello()

yt=sayHello()
print(yt)

yt=sayHi(3)
print(yt)