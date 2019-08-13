def sum_fun(num):

    print(num)
    if num == 1: #必须要终止自己的
        return

    sum_fun(num-1) #函数自己调用自己


sum_fun(3)