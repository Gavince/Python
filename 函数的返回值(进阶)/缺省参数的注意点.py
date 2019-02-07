def Pri_info(name ,age = "" ,gender = True): #缺省参数的值必须放在最后面(没有默认值的参数要放在前面)
    """

    :param name:姓名
    :param age: 年龄
    :param gender: 性别
    """
    gender = "male"

    if not gender:
        gender = "female"

    print("%s is %s %s"%(name, gender, age))

Pri_info("Gavin", 45)
Pri_info("xm", 45, False)
Pri_info("kk", gender = False)

