msg="我爱你Fdd"
encode_msg=msg.encode('utf-8') #将unicode转换成utf-8,即二进制格式,可放在二进制查找中
decode_msg=encode_msg.decode('utf-8') #将其他格式(utf-8)转换成unicode

print("msg= %s" %msg)
print("encode_msg= %s" %encode_msg)
print("decode_msg= %s" %decode_msg)