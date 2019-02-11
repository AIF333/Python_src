import multiprocessing

q=multiprocessing.Queue(3) # 队列最大个数 3,不指定则为无限大
# 队列实际也是一个共享进程；可以存放任意的python对象，如字典，字符串，类等，
# 底层应该是通过 pickle 序列化然后反序列化实现

str1="hello world"
list1=['aaa','bbb','ccc']
dic1={'name':'Iverson','age':24}

q.put(str1)
q.put(list1)
q.put(dic1)

'''此处会一直等待，直到有其他进程get出去，也可用put_nowait,不等待直接抛异常
 也可设置 q.put(dic1,timeout=1)  超时时间，get类似'''
q.put(dic1)

print(q.get())
print(q.get())
print(q.get())
