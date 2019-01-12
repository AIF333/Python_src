import settings
import uuid
#uuid模块能生成唯一的id

class Mysql:
    def __init__(self,host,port):
        self.host=host
        self.port=port
        self.id=self.getid()

    #类方法与类绑定，如此例中从配置文件读取 Mysql端口配置来实例化类，这个与具体对象无关
    #就可以定义为类方法
    @classmethod
    def from_conf(cls):
        return cls(settings.HOST,settings.PORT)

    #静态方法，做工具包使用，与谁都不绑定
    @staticmethod
    def getid():
        return str(uuid.uuid1())

    #绑定给对象
    def showhost(self):
        print('=====>',self.host,self.port,self.id)
        print('**************',self.from_conf,self.getid,self.showhost)

conn1=Mysql('120.1.10.1','6666')
conn2=Mysql.from_conf()

conn1.showhost()
conn2.showhost()