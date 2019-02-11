'''通过 manger模块启用共享内存，多个进程可以同时操作'''
import multiprocessing

def subtract(dic,mutex):
    with mutex:
        dic['count']-=1
    #  mutex.acquire()    mutex.release()的简写，类似 file.open()  file.close()

if __name__ == '__main__':
    mutex=multiprocessing.Lock()

    m=multiprocessing.Manager() #共享内存,多个进程可以访问
    # dict1是普通字典，子进程在初始化时有一份拷贝，但是无法调整主进程的
    # mdic 是共享字典，子进程可以直接访问修改
    dic1={'count':100}
    mdic=m.dict(dic1)
    print(mdic)
    p_l=[]
    for i in range(100):
        # 自动取名Process-1 ，Process-2 ...
        p=multiprocessing.Process(target=subtract,args=(mdic,mutex))
        p_l.append(p)
        p.start()

    for p in p_l:p.join()

    print(mdic)