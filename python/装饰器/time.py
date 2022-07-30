import time

def time_consume(fun):
    def wrapper():
        t1 = time.time()
        fun()
        print(time.time() - t1)
    return wrapper

def fun1():
    t1 = time.time()
    print("您好")
    print(time.time() - t1)

def fun2():
    print("北京")


@time_consume
def fun3():
    count = 0
    for i in range(10000):
        count += 1
    print(count)


if __name__ == "__main__":
    
    fun1()
    fun2()
    fun3()
