import re
## 测试字符串 re 替换
# aaa="ver=10.1.T.T18  aaa"
# bbb="ver=10.1.T.T18  "
#
# flag='ver='
# \S 包括 数字 字母 以及符号，不包括空格
# r1=re.search('^%s(\S*)' % flag,aaa)
# r2=re.search('^ver=(\S*)',bbb)
#
# print(r1.groups())
# print(r2.groups())

## 测试数字填充
# a='07'
# b=int(a)+1
# sb=str(b).zfill(2)
# print(sb)
#
# c='12345678'
# l_c=len(c)
# print(l_c)
# print(c[0:l_c-1])

## 测试读取 windows 路径
# str1="'C:\\Users\\lenovo\\Desktop\\Test\\\yt\\lm.cfg','Minver ='"
# file1=str1.split(',')[0]
# file2='C:\\Users\\lenovo\\Desktop\\Test\\\yt\\lm.cfg'
# print (file1,file2)
#
#
# with open(file2,'r') as f:
#     for line in f:
#         print(line)

dict1={'name':'AIF333','age':18}
print('name' in dict1.keys())