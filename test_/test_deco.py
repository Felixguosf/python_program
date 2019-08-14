# coding=utf-8
#装饰器练习
def myfunc():
    print "This is a function"

def deco(func):
    def _deco(*args,**kwargs):
        print 'this is deco start'
        ret=func(*args,**kwargs)
        print 'this is deco over'
        return ret  #此处的return值对应调用此装饰器的函数的返回值
    return _deco  #暂时理解为装饰器的处理结果，作用是标识装饰器是否被调用

@deco
def myfunc1(number):
    print "I have a niumber {}".format(number)
    return number
print myfunc1(1)






















