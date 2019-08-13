def demo(*args, **kwargs):#一个*表示元组, 两个**表示字典
    """
    :param args: nums
    :param kwargs: dic
    :return: NULL
    """
    print("----------------")
    print(args)
    print(kwargs)
    print("----------------")


gl_nums = (1, 2, 3, 4, 5)
gl_dics = {"name": "gavin",
           "age": 18,
           "sex": "female"}


demo(gl_nums, gl_dics) #未开始拆包　所有的参数都属于元组类型
demo(*gl_nums, **gl_dics) #数据类型一一对应　开始拆包