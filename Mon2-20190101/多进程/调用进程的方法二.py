'''
方法二：继承Process类 ，需实现 run 方法

'''

from multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self,name2):
        super() .__init__() # 需加上父类的 init方法，以免覆盖，造成某些功能无法使用
        self.name2=name2

    def run(self):
        print("<%s> is running" % self.name2)
        time.sleep(2)
        print("<%s> is done" % self.name2)

if __name__ == '__main__':
    p1=MyProcess('AIF333')
    p2=MyProcess('Iverson')
    p1.start()
    p2.start()
    print("===主进程is running ！===")