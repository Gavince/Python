"""
函数的综合小结
"""

def get_infor(name, age, heigh, score=''):
    """

    :param name:
    :param age:
    :param heigh:
    :return:
    """
    stu_infor = {"Name": name, "Age": age, "Heigh": heigh}
    if score:
        stu_infor["score"] = score
    else:
        return stu_infor

    return stu_infor


#主函数
name = input("Please enter you name:")
age = int(input("Please enter you age:"))
heigh = int(input("Please enter you heigh:"))
inform = get_infor(name, age, heigh)
print(inform)

flag = input("Do you want to delete your information?(yes/no)")
while flag == "yes":
    """starting"""

    del inform["Age"]
    flag = input("Do you want to try again? (yes/no)")
