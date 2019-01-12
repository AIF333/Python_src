dic={"name":"AIF333","age":36,"career":"BaseketBall"}

import json
print(dic)
json.dump(dic,open('d1.json','w'))

dic2=json.load(open('d1.json','r'))
print(dic2)

##pickle类似，但需注意的是在序列化函数等，pickle序列的是函数地址，也即在
##反序列化时，需地址存在