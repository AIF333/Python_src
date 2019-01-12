#功能 找到指定路径下的文件是否含有特定字符，有则输出文件绝对路径，
#     类似  grep -rl "xxxx"  /dir/

# 此python脚本是面向过程的编程，优点结构清晰，复杂问题简单化流程化
# 缺点：可扩展性差，一条流水线只能解决一个问题


#初始化生成器
def init(func):
    def warpper(*args,**kwargs):
        g=func(*args,**kwargs)
        next(g)
        return g
    return warpper
#1.列出所有的文件绝对路径
import os
def list_file_path(target):
    path="F:\yeteng\简历\python"
    g=os.walk(path)
    for (filedir, _,files) in g:
        for file in files:
            filepath="%s\%s" %(filedir,file)
            target.send(filepath)

#list_file_path()
#2.打开文件，读出每一行
@init
def openfile(target):
    while True:
        filepath=yield
        with open(filepath,mode='rb') as f:
            for line in f:
                res=target.send((line,filepath))
                if res:break

#3.判断是否含有指定字符
@init
def patcheck():
    tag=False
    while True:
        #print("------tag = %s----" % tag)
        (line,filepath)=yield tag
        tag = False
        if 'AIF'.encode('utf-8') in line:
            print(filepath)
            tag=True

list_file_path(openfile(patcheck()))