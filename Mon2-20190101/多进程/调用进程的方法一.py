'''
调用多进程的方法一：调用 multiprocessing.Process 模块，target目标是方法名，注意没有单引号
参数可以用两种方式传入，如 跑p1,p2

此程序执行时会启动三个进程 主进程，子进程p1和p2,需要理解的是 p1.start p2.start
只是python告诉操作系统开启进程的请求，至于操作系统什么时候开启由操作系统决定！
子进程全部执行完毕后，主进程才会退出，子进程的内存由父进程来释放

调用进程模块，在window下面必须放在  if __name__ == '__main__': 下面，因为在
 window下不加这个容易在引用时引发无线递归循环，把资源耗尽
'''
import multiprocessing
import time
def work(name1):
    print("<%s> is running" % name1)
    time.sleep(2)
    print("<%s> is done" % name1)

if __name__ == '__main__':
    p1=multiprocessing.Process(target=work,args=('AIF333',))
    p2=multiprocessing.Process(target=work,kwargs={'name1':'Iverson'})
    p1.start()
    p2.start()
    p1.join() # 调用join方法，则主进程需等待p1执行完毕才能继续
    print("主进程running")