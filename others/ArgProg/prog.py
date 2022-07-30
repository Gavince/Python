"""
参考网址：https://www.jianshu.com/p/fef2d215b91d
"""
import argparse


def get_parse():

    # step1: 申请对象
    parse = argparse.ArgumentParser(description="This is a test file")

    # step2: 添加参数
    parse.add_argument("level", type=int, choices=[1, 2, 3, 4, 5], help="等级")  # 位置参数(不以-和--开头的参数)，必须配置，否则出错
    parse.add_argument("-n", "--name", choices=["Pytorch", "tf", "Caffe"], type=str, help="填写名字", required=True)
    parse.add_argument("-a", "--age", type=int, help="填写年龄")
    parse.add_argument("-s", "--sex", type=str, default="male",help="填写性别")
    # 不填写值为False, 否则为True
    parse.add_argument("-v", "--version", action="store_true", help="显示版本号")
    parse.add_argument("--gpu", action="store_true", help="是否使用GPU")
    # step3: 解析参数
    return parse.parse_args()


if __name__ == "__main__":
    args = get_parse()
    print(args.name)
    print(args.age)
    print(args.level)
    print(args.version)
    print(args.sex)
    print(args.gpu)

