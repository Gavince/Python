import Assign1_基本概念
import numpy

def input_password():
    """
    输入密码
    :return:
    """
    pwd = input("Please enter password:")

    if len(pwd) >= 8:

        return pwd
    else:

        ex = Exception("密码长度不够！")
        raise ex

Assign1_基本概念.num
print(numpy.__file__)

print(Assign1_基本概念.__file__)
try:
    pwd = input_password()
    print("Password:%s" % pwd)
except Exception as result:
    print("异常错误类型:%s" % result)