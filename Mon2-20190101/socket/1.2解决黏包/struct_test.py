import struct

#格式化输出数字长度，参数 i 表明格式化输出为4个字节
#pack 转换成固定字节
#unpack 转换成数字元祖
p1=struct.pack('i',123)
p2=struct.pack('i',1244543)

t1=struct.unpack('i',p1)
t2=struct.unpack('i',p2)

print(type(p1) ,'     ',p1,'-----',p2)
print(type(t1) ,'     ',t1,'-----',t2)

