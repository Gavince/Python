# 记录每个人的信息
card_list = []


def show_menu():
    """显示菜单"""
    print("*"*50)
    print("欢迎使用名片管理系统")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("0.退出系统")
    print("")
    print("*"*50)


def new_card():

    """新增名片"""
    print("-" * 50)
    print("新增名片")
    name_str = input("请输入姓名： ")
    phone_str = input("请输入电话号码： ")#注意此时输出的数据类型为str
    qq_str = input("请输入QQ: ")
    email_str = input("请输入Enail: ")

    #添加用户信息
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}

    #追加数据
    card_list.append(card_dict)
    print(card_list) #是否把信息添加成功
    print("你已经输入完成！")


def show_all():

    """显示所有名片"""
    if len(card_list) != 0:
        print("-" * 50)
        print("显示所有名片")
        # 打印表头
        for name in ["姓名","电话","QQ","邮箱"]:
            print(name, end="\t\t")

        print("")#可以有效去除多余的空格

        print("="*50)
        # 遍历所有数据并且输出结果
        for card_dic in card_list:

            print("%s\t\t%s\t\t%s\t\t%s" % (card_dic["name"],
                                          card_dic["phone"],
                                          card_dic["qq"],
                                          card_dic["email"]))

    else:
        print("当前无数据,请你输入数据！")


def serach_card():

    """搜索名片"""
    print("-" * 50)
    print("搜索名片")
    #查询
    find_name = input("请输入要查找的姓名：")
    #遍历
    for card_dic in card_list:

        if card_dic["name"] == find_name:

            print("找到了%s的数据"%find_name)
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dic["name"],
                                          card_dic["phone"],
                                          card_dic["qq"],
                                          card_dic["email"]))
            #增加一个函数　来消除一段代码的复杂性
            deal_card(card_dic)

            break

    else:#for...else 语句的使用

        print("抱歉,尚未查找到%s的数据"%find_name)


def deal_card(find_card):
    """修改和删除"""
    action_str = input("请输入要执行的操作 "
                       "[1] 修改 [2] 删除 [0] 返回上级菜单")

    if action_str == "1":

         print("开始修改所查找的信息")

         find_card["name"] = input_card_info(find_card["name"], "姓名")
         find_card["phone"] = input_card_info(find_card["phone"], "电话")
         find_card["qq"] = input_card_info(find_card["qq"], "QQ")
         find_card["email"] = input_card_info(find_card["email"], "邮箱")
         print("修改信息完成")

    elif action_str == "2":

         card_list.remove(find_card)
         print("删除名片完成！")

    elif action_str == "0":

         return

    else:

        print("输入错误！请重新输入！")

def input_card_info(modify_value, TipMessage):
    """修改其中一项的值"""

    result = input(TipMessage + "( tip: 按回车不修改 ):")

    if len(result) > 0: #表示用户是否正式输入

        return result

    else:

        return modify_value
