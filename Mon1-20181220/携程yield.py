#定义一个能初始化的装饰器，因为不用next初始化生成器，无法使用send调用
def init(func):
    def warrper(*args,**kwargs):
        g=func(*args,**kwargs)
        next(g)
        return g
    return warrper

@init  # eater=init_eater(eater)
def eater():
    print("Yeteng beign eat:")
    food_list=[]
    while True:
        food=yield food_list  #相当于一个return yield 后面没跟，则默认None
        food_list.append(food)
        print("%s eatend by yeteng!"%food)


def producer():
    rs=eater() #返回一个生成器
    #print(next(rs)) #初始化生成器，为了通用，用装饰器做了
    while True:
        food=input("请输入要吃的食物>：").strip()
        if not food :
            continue
        print(rs.send(food))

producer()