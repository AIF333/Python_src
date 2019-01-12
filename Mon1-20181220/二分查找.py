l=[1,2,7,8,12,45,56,61,68,76,83,34,45,35,3,6,99,120]
sl=sorted(l)

def search(l,num):#查找的列表和被查找的数字
    lenth=len(l)
    if not lenth:
        print("列表为空，无法查找")
        return
    d_lenth=(lenth//2)
    print(l)

    if l[d_lenth] == num:
        print("已找到! ")
    elif d_lenth == 1:
        print("找不到")
    elif l[d_lenth]<num:
        l=l[d_lenth+1:]
        search(l,num)
    elif l[d_lenth]>num:
        l=l[:d_lenth]
        search(l, num)

def mainf():
    while True:
        num=int(input("请输入要查找的数字1—300："))
        search(sl,num)

if __name__ == '__main__':
   mainf()