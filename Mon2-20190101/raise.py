#raise TypeError('哈哈哈哈')
print('啦啦啦啦啦')

class YtException(BaseException):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return '<%s>'%self.msg
raise YtException('Yt定义的异常')