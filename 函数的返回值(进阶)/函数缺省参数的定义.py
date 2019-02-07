def pri_info(name, age=12, gender=True): #缺省参数的值必须放在最后面
    """

    :param name:姓名
    :param age: 年龄
    :param gender: 性别
    """
    gender = "male"

    if not gender:
        gender = "female"

    print("%s is %s %d"%(name, gender, age))


pri_info("Tom")
pri_info("Gavin", 45)
pri_info("xm", 45, False)
pri_info("kk", gender=False)

