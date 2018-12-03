import time

# 不改动源代码，统计下执行时间
def timmer(func):
    def wrapper(*args,**kwargs): #这就意味着可以接收任意长度、任意格式的参数
        start = time.time()
        res = func(*args,**kwargs) #这个参数接收了本质是给这个func用的，怎么收的就原封不动给回func
        stop = time.time()
        print('run time is %s' % (stop - start))
        return res #实际就是被装饰函数的返回值，如果返回值是none，就返回none也没有问题。这样就不管有没有返回值，wrapper都给它返回一下
    return wrapper

@timmer #index=timmer(index)
def index():
    time.sleep(3)
    print('welcome to index')
    return 123 #带返回值

@timmer #home=timmer(home)
def home(name): #带参数
    time.sleep(2)
    print('welcome to %s home page' %name)

res=index()
print("--------------------",res)
res1=home('egon')
print("--------------------",res1)


