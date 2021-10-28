import time


def time_consume(fun):
    def wrap(*args, **kwargs):
        t0 = time.time()
        fun(*args, **kwargs)
        print(time.time() - t0)
    return wrap  

def fun():
    t0 = time.time()
    print("A")
    print(time.time() - t0)

def fun1():
    t0 = time.time()
    for i in range(100):
        print(i, end="")
    print("\n", time.time() - t0)

@time_consume
def fun2(*args):
    for i in range(1000):
        print(end="")
    print(args)
    print("A")

    
if __name__ == "__main__":
    #fun()
    #fun1()
    fun2(2, 5, 5)
