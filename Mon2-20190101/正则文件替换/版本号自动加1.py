'''
此脚本主要是实现版本号自动加1，对格式如 ver=10.20.3.T07 自动加1
成 ver=10.20.3.T08
'''
import re
import os

# 定义版本号自动+1的方法 参数:1.修改文件
# 2.修改标志 如 ver=   3.加1的位数（如本列，默认是后两位）
# 4.版本号自动加的位数 默认是 1 eg:ver=10.20.3.T07 => ver=10.20.3.T08
def verAdd(file,flagstr,changeLength=-2,addValue=1):
    with open(file,'r') as f1,open("%s.bak" % file,'w') as f2:
        # print("======>",file,flagstr,type(file),type(flagstr))
        for line in f1:
            # re进行匹配，line.strip 会剔除 行首未空格
            oldstr=re.search('^%s(.*)' % flagstr,line.strip())

            #如果匹配上版本号，则自动 +addValue=1
            if oldstr:
                oldstr=oldstr.groups()[0].strip()
                # 截取后 changeLength=-2 位，如 07 变为整型加后 zfill填充成 08
                oldstr_ver=oldstr[changeLength:]
                newstr_ver=str(int(oldstr_ver)+addValue).zfill(abs(changeLength))
                old_num=len(oldstr)
                newstr=oldstr[:old_num-2]+newstr_ver
                print("文件'%s' 的版本号<%s> ,已自动加%s,新的版本号为<%s>" %
                      (file,oldstr,addValue,newstr))
                #写入f2文件
                f2.write(line.replace(oldstr,newstr))
            else:
                f2.write(line)

        f1.close()
        f2.close()
        if os.path.exists("%s.bak" % file):
            overFile("%s.bak" % file,file)
        else:
            print("%s.bak 文件不存在！" % file)

# 定义文件覆盖方法 newfile 覆盖 oldfile
def overFile(oldfile,newfile):
    os.remove(newfile)
    os.rename(oldfile,newfile)

# 通过配置文件实现批量替换,参数：1.文件名  2.分隔符 默认是','
def delWithCofig(file,split_flag=','):
    with open(file,'r') as f:
        for line in f:
            if not line.startswith("#"):
                delFile=line.split(split_flag)[0].strip()
                # 读取配置文件是最后一个会有换行符需剔除
                delPat=line.split(split_flag)[1].replace('\n','')
                verAdd(delFile,delPat)

pzFile='E:\\Lern\\python\\Lsrc\\Mon2-20190101\\正则文件替换\\pz.txt'
delWithCofig(pzFile)
