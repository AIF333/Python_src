'''

调用进程模块，在window下面必须放在  if __name__ == '__main__': 下面，因为在
 window下不加这个容易在引用时引发无线递归循环，把资源耗尽
'''
import multiprocessing
import time
import os

def lock_work(name1,mutex): #进程上锁，顺序执行
    mutex.acquire()
    print("<%s> is running" % name1)
    time.sleep(2)
    print("<%s> is done" % name1)
    mutex.release()

def work(name1):
    print("<%s> is running" % name1)
    time.sleep(2)
    print("<%s> is done" % name1)

if __name__ == '__main__':
    mutex=multiprocessing.Lock() #同步锁

    p1=multiprocessing.Process(target=work,args=('AIF333',),name='AifProcess') # name可以定义进程名
    p1.daemon=True # 守护进程，在主进程的代码执行完毕后则会被干掉，需定义在start前
    p1.start() # 由于定义成了守护进程，可能打印不了，因为主代码一结束就被干掉
    p1.terminate() # 强制结束进程，但慎用，因为如果子进程还有子进程，则其子进程会成为僵尸进程
    print(p1.is_alive()) # 看进程是否还有效，注意由于进程的 start,terminate 方法
      #均是操作系统来执行，什么时候执行，执行多长时间都不收我们控制。所以这里前面
      #有 terminate也会打印true,加个 sleep就可以看到成为 false
    p1.join() # 调用join方法，则主进程需等待p1执行完毕才能继续
    print(p1.pid) #查看p1进程号 等同于 os模块里
    print(os.getpid()) # 查看主进程的进程号，可以将这个方法放在 work里，查看p1的
    print(os.getppid()) # 查看（主进程）的父进程号，就 pycharm的进程号

    # 启用同步锁，则顺序执行 lock_work
    p2=multiprocessing.Process(target=lock_work,args=('LebronJames',mutex)) # name可以定义进程名
    p3=multiprocessing.Process(target=lock_work,args=('Iverson',mutex)) # name可以定义进程名
    p2.start()
    p3.start()


    print("主进程running")

