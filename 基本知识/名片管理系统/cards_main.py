
import cards_tools #引入包

while True:

    cards_tools.show_menu()
    action = input("请你输入希望执行的操作：")

    if action in ["1","2","3","4"]:

        """
        1.pass占位符 表示此时先不操作　等以后开发时再补充功能 保持代码的完整型
        2.python中没有switch/case语句
        """
        if action == "1":
            cards_tools.new_card()  #新增名片
        elif action == "2":
            cards_tools.show_all()  #显示全部
        elif action == "3":
            cards_tools.serach_card()  #修改信息
        else:
            pass
    elif action == "0":
        print("欢迎您再一次使用名片管理系统！")
        break
    else:
        print("你输入的不正确,请重新输入:")

